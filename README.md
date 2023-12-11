# leetcode-summerizer
Summarize and collect into a DB a collection of LeetCode problems (Description, Solutions, Code, Analysis)

## 📣 News

- My new e-book "LLMs Intro and System Design (2023 Edition)" covering the foundations of LLMs as well as System Design and Latest Updates in generative AI technology will appear soon [planned by Christmas 🎄]. Stay tuned!

# 🚀 AI-Powered LeetCode Problem Summarizer

This project harnesses the power of OpenAI's GPT models to summarize LeetCode problems, making interview preparation more efficient and engaging. Whether you're gearing up for a big interview or just brushing up on your coding skills, this tool is your go-to assistant!

## 🌟 Features

- Summarizes LeetCode problems using OpenAI's GPT models.
- Efficient batch processing of problems.
- Easy-to-use command-line interface.
- Outputs stored neatly in CSV format.

## 📚 Setup Instructions

1. **Get OpenAI API Access:**
   - You'll need access to OpenAI's API. Check out [OpenAI's Platform](https://openai.com/api/) for subscription details and how to obtain API credits.

2. **Clone the Repository:**
   - `git clone https://github.com/your-username/leetcode-summarizer.git`
   - Navigate to the repository directory: `cd leetcode-summarizer`

3. **Install Required Python Packages:**
   - Make sure you have Python installed on your system.
   - Install necessary packages: `pip install requests pandas`

4. **Set Up Your API Key:**
   - Store your OpenAI API key as an environment variable for security.
   - In your terminal, set the API key: `export OPENAI_API_KEY='your_api_key_here'`

5. **Running the Application:**
   - Run the main script: `python main.py`
   - Make sure you have your problem inputs ready in `prompt_arguments.csv`.

### Open AI Platform Issues

#### ChatGPT API Setup Challenges
- **New API endpoint updates:**
    - The current endpoint used in this code is "https://api.openai.com/v1/chat/completions".
    - This endpoint is one of the options for both "gpt-3.5-turbo" (default in this code) and "gpt-4" models.
    - Each endpoint supports only a certain class of models.
    - Explore the latest "endpoints" and their compatible models in [Open AI's platform documentation](https://platform.openai.com/docs/models/model-endpoint-compatibility).
- **New format for request message (currently ChatML format).**
- **You have to upgrade to a paid account and add credits to your account:**
    - There’s a known bug with the payment system. You may get the "Error 429 Too Many Requests" from Open AI Api while adding your payment method. You may need to install a VPN (as I did as the last solution) to get around this issue [Link: https://techviral.net/chatgpt-error-429-too-many-requests/], or wait for it to be resolved, hopefully soon.
- **You need to re-generate your Open AI key after upgrading the billing account and store the new API key in your bash_profile for use in the python code. Otherwise, you will get the error "404 Client Error: Not Found for url: https://api.openai.com/v1/completions".**

## 💻 Recommended Code Editor

- Suggestion is using [Visual Studio Code](https://code.visualstudio.com/) for an enhanced coding experience with this project.

## 🎶 A Fun Fact

- This README and the accompanying code were crafted while listening to some energetic techno beats! Techno is love ❤️. Check out some of my DJ mixes (Organic House, and Melodic House and Techno) [here on Soundcloud](https://soundcloud.com/alireza_deer)!

## 🙌 Credits

- This project was created with assistance from my ChatGPT assistant, who was indispensable in writing the code and crafting this README.
