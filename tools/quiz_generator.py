import re


class QuizGeneratorTool:
    """
    Tool for generating simple study questions from text.
    """

    def generate_questions(self, text: str) -> list:
        sentences = self._split_sentences(text)

        questions = [
            "What is the main idea of the text?",
            "Which concepts are repeated most often in the material?",
            "How would you explain the topic in your own words?",
        ]

        for sentence in sentences[:2]:
            important_part = sentence[:80].strip()
            if important_part:
                questions.append(f"Why is this point important: '{important_part}...' ?")

        return questions[:5]

    def _split_sentences(self, text: str) -> list:
        return [
            sentence.strip()
            for sentence in re.split(r"(?<=[.!?])\s+", text)
            if sentence.strip()
        ]
