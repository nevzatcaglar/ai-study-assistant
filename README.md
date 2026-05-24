# AI Study Assistant

## Project Description

AI Study Assistant is a Python-based agent system that helps users study written material. The system receives either direct text or a text file, analyzes the content, extracts important keywords, creates a short summary, and generates study questions.

The project demonstrates an AI-assisted workflow with tool usage, input handling, testing, documentation, and deployment preparation.

## Main Features

- Accepts direct text input
- Reads `.txt` files
- Cleans and analyzes text
- Extracts keywords
- Generates a short summary
- Generates study questions
- Includes unit tests
- Includes clear project structure and startup instructions

## Agent-Based Logic

The system uses a simple intelligent agent called `StudyAssistantAgent`.

The agent:
1. receives user input,
2. decides whether the input is a file path or direct text,
3. calls the file reader tool if needed,
4. sends the text to the text analyzer tool,
5. sends the text to the quiz generator tool,
6. returns a structured study result.

## Tools Used

### FileReaderTool
Reads `.txt` files from the local system.

### TextAnalyzerTool
Cleans text, extracts keywords, creates a short summary, and gives study advice.

### QuizGeneratorTool
Generates simple study questions from the input text.

## Project Structure

```text
ai-study-assistant/
│
├── main.py
├── agent.py
├── tools/
│   ├── file_reader.py
│   ├── text_analyzer.py
│   └── quiz_generator.py
│
├── tests/
│   ├── test_file_reader.py
│   ├── test_text_analyzer.py
│   └── test_agent.py
│
├── sample_files/
│   └── sample_text.txt
│
├── requirements.txt
├── README.md
└── journal.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd ai-study-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the main program:

```bash
python main.py
```

Example input:

```text
sample_files/sample_text.txt
```

You can also paste direct text instead of a file path.

## How to Test

Run:

```bash
pytest
```

## Data Porting and Conversion

The system accepts either direct text or a `.txt` file. If a file path is entered, the FileReaderTool reads the file and converts it into a plain Python string. The text is cleaned by removing unnecessary whitespace. Then it is passed to the analyzer and quiz generator tools.

This keeps the data format consistent between components.

## Deployment Preparation

This project is prepared as a local command-line application. Another user can run it by cloning the GitHub repository, installing the dependencies from `requirements.txt`, and running `python main.py`.

## Proposed Deployment Strategy

The most suitable deployment strategy for this project is a local command-line tool. In a future version, it could be deployed as a web service using Flask or FastAPI.
