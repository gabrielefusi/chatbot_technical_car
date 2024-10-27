# Car Manual Chatbot using LangChain

This project demonstrates how to create a context-aware chatbot using LangChain with a car manual as the dataset. The chatbot uses RAG (Retrieval-Augmented Generation) to answer user queries based on the car manual's content.

## Setup Instructions

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-username/car-manual-chatbot.git
   cd car-manual-chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your API key in a `.env` file:
   ```
   OPENAI_API_KEY=your-secret-api-key-here
   ```

5. Run the project:
   ```bash
   python src/main.py
   ```

## Project Structure

- `data/`: Contains the car manual HTML file.
- `src/`: Contains the source code for data loading, embedding, and RAG setup.
- `README.md`: Project description and setup instructions.
- `requirements.txt`: Dependencies for the project.

## Requirements

- Python 3.10 or higher
- OpenAI API Key
