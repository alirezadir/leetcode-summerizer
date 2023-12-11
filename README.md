# Leetcode-Summarizer 1.0
Summarize and collect into a DB a collection of LeetCode problems (Description, Solutions, Code, Analysis)

## 📣 News

- My new e-book 📚  **LLMs: An Intro and System Design (2023 Edition)** will appear soon (by this Christmas 🎄, will be brought by Santa 🎅). 
  - It will cover the foundations of LLMs, LLMs System Design,  and Latest Tools and Updates in Generative AI technology.
  - Stay tuned! 🎁

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

6. **File Structure and Data Schemas:**
   - `logs/app.log`: Logs all runtime information, including progress updates and errors. Data schema: Timestamp, Log Level, Message.
   - `logs/prompts.log`: Stores detailed prompt templates used for each request. Data schema: Prompt Template, Problem.
   - `prompt_arguments.csv`: Input file containing LeetCode problem descriptions. Should have a header named "problem" followed by rows containing individual problem descriptions or titles.

### Open AI Platform Issues

- **ChatGPT API Setup Challenges**
  - **New API endpoint updates:**
      - The current endpoint used in this code is "https://api.openai.com/v1/chat/completions".
      - This endpoint is one of the options for both "gpt-3.5-turbo" (default in this code) and "gpt-4" models.
      - Each endpoint supports only a certain class of models.
      - Explore the latest "endpoints" and their compatible models in [Open AI's platform documentation](https://platform.openai.com/docs/models/model-endpoint-compatibility).
  - **New format for request message (currently ChatML format).**
  - **You have to upgrade to a paid account and add credits to your account:**
      - There’s a known bug with the payment system. You may get the `Error 429 Too Many Requests` from Open AI Api while adding your payment method. You may need to install a VPN (as I did as the last solution) to get around this issue ([Link](https://techviral.net/chatgpt-error-429-too-many-requests/)), or wait for it to be resolved, hopefully soon!
  - **You need to re-generate your Open AI key after upgrading the billing account and store the new API key in your bash_profile for use in the python code. Otherwise, you will get the error `404 Client Error: Not Found for url: https://api.openai.com/v1/completions`**.

## 💻 Recommended Code Editor

- Suggestion is using [Visual Studio Code](https://code.visualstudio.com/) for an enhanced coding experience with this project.

## 🎶 A Fun Fact

- 🎧: This README and the accompanying code were crafted while listening to some energetic techno beats! 🎶 Techno is love ❤️. 
  - <img src="imgs/soundlcloud.png" alt="Alt text" style="width: 15px; height: 15px;">  Check out some of my DJ mixes (Organic House, Melodic House and Techno) [here on Soundcloud](https://soundcloud.com/alirezadir)!
  - 🎧🎵 My current favorite track: [Simulation](https://open.spotify.com/playlist/3p52wFvY1hYMzjQJnkkfxW) *by "Anyma & Chris Avantgarde".*

## 🙌 Credits

- This project was created with assistance from my ChatGPT assistant, who was indispensable in writing the code and crafting this README.

## 🌟 Gratitude 

- 🙏 I am deeply grateful for being where I am today and for the opportunity to share this work with you all. 🌍 It's been a long, challenging journey filled with excitement from the start to this point. I am thankful for all the gifts that the universe has brought to me, and I've discovered that living with gratitude is a profoundly transformative way of life. 🌈

> To speak gratitude is courteous and pleasant, to enact gratitude is generous and noble, but to live gratitude is to touch Heaven. – Johannes A. Gaertner (*German Art Historian, Professor of Art History*)

- 🙏 Special thanks go to my very close friends who have always supported me throughout my journey. 

- 🙏 I am also eternally grateful to all my teachers who have guided me from the very beginning until now. Their wisdom and support have been invaluable.

