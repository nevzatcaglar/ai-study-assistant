# Project Journal

## Step 1 – 24.04

### Planned System Description and Goal

The planned system is an AI Study Assistant. The goal of the system is to help users study written material more easily. The user can provide either direct text or a `.txt` file. The system analyzes the input and returns a structured study result including a short summary, keywords, study advice, and generated questions.

### AI or Agent-Based Approach

The project uses a single intelligent agent. The agent receives the user input and decides which tools should be used. If the input is a file path, the agent calls the file reader tool. Then it calls the text analyzer tool and the quiz generator tool. Finally, it combines the outputs into one meaningful result.

### Planned Tools

- File reader tool
- Text analyzer tool
- Quiz generator tool

### Required Programming Concepts

The project will require classes, functions, modules, file handling, string processing, lists, dictionaries, error handling, and unit testing.

## Step 2 – 08.05

### Updated System Description

The system has been implemented as a Python command-line application. The user can run `main.py` and enter either a text file path or direct text. The agent checks the input, calls the correct tools, and returns the result.

### Programming Concepts Actually Used

The project uses object-oriented programming with separate classes for the agent and tools. It uses modules to separate responsibilities. It also uses file handling, regular expressions, dictionaries, lists, input validation, and exception handling.

### Tool Integration

The tools are integrated inside the `StudyAssistantAgent` class. The agent creates objects from `FileReaderTool`, `TextAnalyzerTool`, and `QuizGeneratorTool`. During execution, the agent coordinates these tools in a workflow.

## Step 3 – 15.05

### Testing Process

Testing was performed together with implementation. Unit tests were created for file reading, text analysis, and the main agent workflow. The tests check whether the main components work correctly and whether invalid cases are handled properly.

### Test Scenarios

1. Reading a valid `.txt` file  
Expected result: the file content is returned correctly.

2. Reading a missing file  
Expected result: the system raises a `FileNotFoundError`.

3. Reading an unsupported file type  
Expected result: the system raises a `ValueError`.

4. Analyzing normal text  
Expected result: the system returns a summary, keywords, and study advice.

5. Giving empty input to the agent  
Expected result: the system returns an error message.

6. Giving direct text input  
Expected result: the system returns a structured result with summary and questions.

### Deployment Preparation

The project includes a `requirements.txt` file, a README file, startup instructions, and test instructions. This allows another user to install and run the system in a controlled way.

### Data Conversion Explanation

If the user enters a file path, the file is read and converted into a Python string. The text is cleaned by removing extra whitespace. Then the same text format is passed to the analyzer and quiz generator. This ensures consistency between components.

## Final Submission – 22.05

### Final System Description and Goal

The final system is a Python-based AI Study Assistant. It helps users understand study material by producing a short summary, keywords, study advice, and questions. The system is useful for students who want to quickly review written content.

### Final Explanation of Programming Concepts

The project uses object-oriented programming, modular design, file handling, text processing, regular expressions, data structures, input validation, and automated testing. Each concept is used in a practical part of the system.

### Final Description of Tools and Their Role

The FileReaderTool reads local `.txt` files. The TextAnalyzerTool processes and analyzes the text. The QuizGeneratorTool creates study questions. The agent connects all tools and controls the workflow.

### Final Testing Results and Conclusions

The test results show that the main workflow works correctly. Valid input is processed successfully, and invalid cases such as empty input, missing files, and unsupported file types are handled properly.

### Final Deployment Preparation Description

The project can be run locally. The user needs to clone the GitHub repository, install the dependencies with `pip install -r requirements.txt`, and run `python main.py`.

### Proposed Deployment Strategy

The chosen deployment strategy is a local command-line application. This is suitable because the project is small, easy to install, and does not require a server. In the future, it could be converted into a web-based study assistant.
