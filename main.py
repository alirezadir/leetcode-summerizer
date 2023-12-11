"""
LeetCode Problem Summarizer

Author: Alireza Dirafzoon
Co-author: ChatGPT
Email: alireza.dirafzoon@gmail.com
GitHub: https://github.com/alirezadir

This script uses OpenAI's GPT models to summarize LeetCode problems.
It helps in making interview preparation more efficient and engaging.

License: MIT License

Prerequisites:
- A valid 'prompt_arguments.csv' file in the same folder containing the problem inputs.
- OpenAI API key set as an environment variable.

Usage:
- Run the script using: python3 main.py

Enjoy practicing LeetCode more than ever!
"""

import requests
import pandas as pd
import os
import logging
import csv

INPUT_FILE = 'input/prompt_arguments.csv'
OUTPUT_FILE = 'output/chatgpt_responses.csv'
LOG_FILE = 'logs/app.log'
PROMPT_LOG_FILE = 'logs/prompts.log'

# Setup logging with different levels for file and console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# File handler for detailed logging to a file
fh = logging.FileHandler(LOG_FILE)
fh.setLevel(logging.DEBUG)  # Set to DEBUG for more detailed logging
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(file_formatter)

# Console handler for logging to the console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # Set to INFO for less detailed logging
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(console_formatter)

logger = logging.getLogger()
logger.addHandler(fh)
logger.addHandler(ch)

# Create directories for logs and output if they do not exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Function to log the prompt templates and arguments
def store_prompt_log(prompt_template, problem, filename=PROMPT_LOG_FILE):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([prompt_template, problem])
        logger.info("Prompt template and argument logged.")

# Function to construct the prompt with detailed summarization tasks
def construct_prompt(problem):
    prompt_template = (
        f"Task: Summarize the following coding problem and provide solutions.\n"
        f"Input Description: The problem input can be a URL link to a coding problem on leetcode.com, "
        f"or the name of a problem on leetcode.com, "
        f"or a brief description of the coding problem.\n"
        f"Problem: {problem}\n\n"
        f"Output Requirements:\n"
        f"1. Provide a very short summary of the problem description in plain language.\n"
        f"2. Include 1-2 very short examples to describe the problem.\n"
        f"3. Present 1-3 solution approaches.\n"
        f"   For each solution approach:\n"
        f"   a) Write a simple overview of the solution, highlighting the data structures and main algorithms used.\n"
        f"   b) Provide the solution as Python code, optimized for a Google interview.\n"
        f"   c) Include some test cases and the results of these test cases in a clean format.\n"
        f"   d) Walk through the code with one of the test cases.\n"
        f"   e) Briefly describe the Time and Space complexity of each algorithm."
    )
    store_prompt_log(prompt_template, problem)
    return prompt_template

# Function to call the ChatGPT API for GPT-4 model
def call_chatgpt_api(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        logger.error("API key not found. Set the OPENAI_API_KEY environment variable.")
        raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")
    try:
        logger.info("Request sent to OpenAI API. Waiting to hear back...")
        response = requests.post(
            url='https://api.openai.com/v1/chat/completions',
            headers={'Authorization': f'Bearer {api_key}'},
            json={
                # 'gpt-4' is set as the default model
                # 'gpt-3.5-turbo' can also be used as an option
                # you can switch to 'gpt-4' if available and preferred
                'model': 'gpt-4',  # model name
                # Using ChatML format for the request:
                # ChatML allows for structured conversation-like exchanges.
                # 'messages': a list where each entry represents one message in the conversation.
                # Each message is a dict with 'role' and 'content'.
                # 'role': 'user' signifies this message is from the user to the model.
                # 'content': The actual content of the message, here being the prompt.
                'messages': [{'role': 'user', 'content': prompt}]
            }
        )
        response.raise_for_status()
        logger.info("Response received. Now start processing ...")
        response_text = response.json()['choices'][0]['message']['content'].strip()

        # Formatting response with markdown for Python code
        formatted_response = response_text
        if "Python code:" in formatted_response:
            formatted_response = formatted_response.replace("Python code:", "\n```python\n") + "\n```"

        logger.debug(f"Response snippet: {formatted_response[:100]}")  # Logs first 100 characters of the response

        return formatted_response
    except requests.RequestException as e:
        logger.error(f"An error occurred while calling the API: {e}")
        return None

# Function to store the response in a CSV file
def store_response_csv(problem_no, title, difficulty, response, filename=OUTPUT_FILE):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)  # QUOTE_ALL to quote all fields
        # Escape double quotes in the response
        escaped_response = response.replace('"', '""')
        writer.writerow([problem_no, title, difficulty, escaped_response])
        logger.info("Current prompt processing successfully finished!")


def main():
    logger.info("Starting main function")

    try:
        prompts_df = pd.read_csv(INPUT_FILE)
        prompts_df.fillna({
            'Problem No': 'N/A',
            'Title': '',
            'Difficulty': 'Unknown',
            'Tags': 'N/A',
            'Status': 'N/A',
            'Sort Order': 0
        }, inplace=True)

        if 'Title' not in prompts_df.columns:
            raise Exception("Title column missing in the input file.")

        with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Problem No', 'Title', 'Difficulty', 'response'])

        total_rows = len(prompts_df)
        batch_size = 5  # Adjustable batch size
        for i in range(0, total_rows, batch_size):
            batch = prompts_df.iloc[i:i+batch_size]
            for index, row in batch.iterrows():
                problem = row['Title']
                prompt = construct_prompt(problem)
                logger.info(f"Processing problem: {problem}")
                response = call_chatgpt_api(prompt)
                if response:
                    store_response_csv(row['Problem No'], problem, row['Difficulty'], response)

            processed = min(i + batch_size, total_rows)
            bar_length = 20
            bar = '#' * int(bar_length * (processed / total_rows)) + '.' * (bar_length - int(bar_length * (processed / total_rows)))
            logger.info(f"Progress: {processed}/{total_rows} [{bar}] ({(processed / total_rows) * 100:.2f}%)")

        logger.info("Main function finished successfully!")
    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
