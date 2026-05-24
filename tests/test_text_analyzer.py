from tools.text_analyzer import TextAnalyzerTool


def test_analyze_returns_expected_keys():
    text = (
        "Artificial intelligence helps students study better. "
        "Artificial intelligence can summarize material. "
        "Students can use tools to generate questions."
    )

    tool = TextAnalyzerTool()
    result = tool.analyze(text)

    assert "summary" in result
    assert "keywords" in result
    assert "study_advice" in result
    assert "artificial" in result["keywords"]


def test_short_text_still_returns_result():
    tool = TextAnalyzerTool()
    result = tool.analyze("Python is useful.")

    assert isinstance(result["summary"], str)
    assert isinstance(result["keywords"], list)
