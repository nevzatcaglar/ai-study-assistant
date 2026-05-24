from pathlib import Path

from tools.file_reader import FileReaderTool
from tools.text_analyzer import TextAnalyzerTool
from tools.quiz_generator import QuizGeneratorTool


class StudyAssistantAgent:
    """
    A simple agent-based workflow.

    The agent receives user input, decides whether the input is a file path
    or direct text, calls the correct tools, and returns a structured study result.
    """

    def __init__(self):
        self.file_reader = FileReaderTool()
        self.text_analyzer = TextAnalyzerTool()
        self.quiz_generator = QuizGeneratorTool()

    def run(self, user_input: str) -> str:
        if not user_input or not user_input.strip():
            return "Error: input cannot be empty."

        user_input = user_input.strip()

        if Path(user_input).exists():
            text = self.file_reader.read(user_input)
            input_type = "file"
        else:
            text = user_input
            input_type = "direct text"

        if not text or len(text.strip()) < 20:
            return "Error: the input text is too short to analyze meaningfully."

        analysis = self.text_analyzer.analyze(text)
        quiz = self.quiz_generator.generate_questions(text)

        return self._format_result(input_type, analysis, quiz)

    def _format_result(self, input_type: str, analysis: dict, quiz: list) -> str:
        result = []
        result.append(f"Input type: {input_type}")
        result.append("")
        result.append("Short Summary:")
        result.append(analysis["summary"])
        result.append("")
        result.append("Main Keywords:")
        result.append(", ".join(analysis["keywords"]))
        result.append("")
        result.append("Study Advice:")
        result.append(analysis["study_advice"])
        result.append("")
        result.append("Generated Questions:")
        for index, question in enumerate(quiz, start=1):
            result.append(f"{index}. {question}")
        return "\n".join(result)
