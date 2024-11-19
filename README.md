# Python Streaming with Langchain Agents and Tools. 🧠🤖

This repository contains a chatbot built using Python, LangChain, and OpenAI APIs. The bot leverages LangChain’s agents and tools for dynamic task handling and real-time response streaming to deliver a robust conversational experience.


## Prerequisites

Before you begin, ensure you have the following installed:
	•	Python 3.10 or higher
	•	Pip package manager
	•	An OpenAI API key  


## Installation:
1. Clone the project:
    - git clone https://github.com/ajeetach97701/Personal-Bot.git
2. Create Virtual Environment
    - conda create -p venv python==3.11 -y
3. Activate the environment:
    - conda activate ./venv
4. Install requirements:
    - pip install -r requirements.txt
5. Setup .env file from .env.example
6. Insert Your CV pdf in Data folder with name personal_cv.pdf

## Usage
1. How to run? 
    - uvicorn server:app --reload 
    or 
    - uvicorn server:app --host Your IP --port 8000 --reload
2.	Features in action:
    - The bot streams responses in real-time.
    - It uses LangChain agents to decide when to call external tools.
    - Add tools as per your need. 
        - goto Tools directory and add tool file and make initialize the tool from tools__init__.py






    


