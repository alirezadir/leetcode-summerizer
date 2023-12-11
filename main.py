"""
LeetCode Problem Summarizer

Author: Alireza Dirafzoon
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

# Create directories for logs and output if they do not exist
os.makedirs('./logs', exist_ok=True)
os.makedirs('./output', exist_ok=True)

# Setup logging to both file and console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('./logs/app.log')  # File handler for logging to a file
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()  # Console handler for logging to the console
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(fh)
logger.addHandler(ch)

# Function to log the prompt templates and arguments
def store_prompt_log(prompt_template, problem, filename='./logs/prompts.log'):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([prompt_template, problem])
        logging.info("Prompt template and argument logged.")

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

# Function to call the ChatGPT API for GPT-3.5-xxx models using the Chat Completion endpoint
def call_chatgpt_api(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        logging.error("API key not found. Set the OPENAI_API_KEY environment variable.")
        raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")
    try:
        logging.info("Request sent to OpenAI API. Waiting to hear back...")
        response = requests.post(
            # chat_completions endpoint (Please check the API documentation for updated endpoints)
            url='https://api.openai.com/v1/chat/completions',
            headers={'Authorization': f'Bearer {api_key}'},
            json={
                # 'gpt-3.5-turbo' is set as the default model
                # you can switch to 'gpt-4' if available and preferred e.g. set 'model': 'gpt-4'
                # each endpoint has a different set of models available to support 
                'model': 'gpt-3.5-turbo',  # model name

                # Using ChatML format for the request:
                # - ChatML: allows for structured conversation-like exchanges.
                #   - 'messages': a list where each entry represents one message in the conversation.
                #   - Each message is a dict with 'role' and 'content'.
                #       - 'role': 'user' signifies this message is from the user to the model.
                #       - 'content': The actual content of the message, here being the prompt.
                'messages': [{'role': 'user', 'content': prompt}]
            }
        )
        response.raise_for_status()
        logging.info("Response received. Now start processing ...")
        response_text = response.json()['choices'][0]['message']['content'].strip()
        # Format response with markdown header and Python code identifier
        formatted_response = "# " + response_text.replace("```python", "\n# python\n```python")
        return formatted_response
    except requests.RequestException as e:
        logging.error(f"An error occurred while calling the API: {e}")
        return None

# Function to store the response in a CSV file with a problem number
def store_response_csv(problem_number, problem, response, filename='./output/chatgpt_responses.csv'):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([problem_number, problem, response])  # Storing problem number, problem, and response
        logging.info("Current prompt processing successfully finished!")

def main():
    logging.info("Starting main function")

    try:
        prompts_df = pd.read_csv('prompt_arguments.csv')

        # Initialize CSV files with headers
        with open('./output/chatgpt_responses.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['No.', 'problem', 'response'])  # Header for response CSV

        with open('./logs/prompts.log', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['prompt_template', 'problem'])  # Header for prompt log CSV

        total_rows = len(prompts_df)
        batch_size = 5  # Adjustable batch size
        for i in range(0, total_rows, batch_size):
            batch = prompts_df.iloc[i:i+batch_size]
            for index, row in batch.iterrows():
                problem = row['problem']
                prompt = construct_prompt(problem)
                logging.info(f"Processing problem: {problem}")
                response = call_chatgpt_api(prompt)
                if response:
                    store_response_csv(index + 1, problem, response)

            # Logging progress
            processed = min(i + batch_size, total_rows)
            percent_complete = (processed / total_rows) * 100
            logging.info(f"Progress: {processed}/{total_rows} rows processed ({percent_complete:.2f}%)")

        logging.info(
           "Main function finished successfully! "
            "Note: this doesn't necessarily indicate task success! "
            "Check the logs/app.log and output/chatgpt_responses.csv file for results!"
        )
    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
