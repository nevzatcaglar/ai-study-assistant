# AI Study Assistant

This project is a simple Python based study assistant. I made it for the practical task about implementing and testing an AI or agent based Python system.

The program helps a user study a text. The user can either write text directly or give the path of a text file. After that, the system gives a short summary, keywords, study advice, and some study questions.

## How it works

The system uses a simple agent workflow.

First, the agent takes the input from the user. Then it checks if the input is a file path or normal text. If it is a file path, it reads the file. After that, the text is sent to the analyzer and question generator tools.

The result includes:

- short summary
- important keywords
- study advice
- generated questions

## Tools

There are three tools in the project.

FileReaderTool reads text files.

TextAnalyzerTool cleans and analyzes the text. It finds repeated important words and creates a short summary.

QuizGeneratorTool creates simple questions from the text.

## How to run

Clone the project and open the project folder.

Install requirements:

pip install -r requirements.txt

Run the program:

python main.py

Example input:

sample_files/sample_text.txt

The user can also paste normal text directly instead of using a file.

## Testing

The project includes basic tests. The tests check the file reader, text analyzer, and agent workflow.

To run tests:

pytest

If pytest has an import problem, this can also be used:

PYTHONPATH=. pytest

## Data handling

The system mainly works with plain text. If the user gives a file path, the file content is read and converted into a string. Then this text is used by the other tools. This keeps the data flow simple and understandable.

## Deployment

This project is prepared as a local command line application. Another user can run it by downloading the repository, installing the requirements, and running main.py.

For this assignment, local deployment is enough. In the future, the same idea could be improved as a small web application.
