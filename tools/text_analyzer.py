import re
from collections import Counter


class TextAnalyzerTool:
    """
    Tool for basic text analysis.

    It cleans the text, extracts frequent keywords, creates a short summary,
    and gives simple study advice.
    """

    STOPWORDS = {
        "the", "and", "is", "in", "to", "of", "a", "an", "for", "on", "with",
        "as", "by", "this", "that", "from", "it", "are", "be", "or", "at",
        "which", "can", "will", "was", "were", "has", "have", "must", "your",
        "you", "we", "they", "their", "our"
    }

    def analyze(self, text: str) -> dict:
        cleaned_text = self._clean_text(text)
        sentences = self._split_sentences(cleaned_text)

        summary = self._summarize(sentences)
        keywords = self._extract_keywords(cleaned_text)
        study_advice = self._create_study_advice(keywords)

        return {
            "summary": summary,
            "keywords": keywords,
            "study_advice": study_advice,
        }

    def _clean_text(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()

    def _split_sentences(self, text: str) -> list:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def _summarize(self, sentences: list) -> str:
        if not sentences:
            return "No summary could be generated."

        selected = sentences[:3]
        return " ".join(selected)

    def _extract_keywords(self, text: str) -> list:
        words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
        filtered_words = [word for word in words if word not in self.STOPWORDS]

        if not filtered_words:
            return ["No clear keywords found"]

        counts = Counter(filtered_words)
        return [word for word, _ in counts.most_common(8)]

    def _create_study_advice(self, keywords: list) -> str:
        if not keywords or keywords[0] == "No clear keywords found":
            return "Read the material again and identify the most repeated concepts."

        return (
            "Focus first on these key concepts: "
            + ", ".join(keywords[:5])
            + ". Then try to explain each concept in your own words."
        )
