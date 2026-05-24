from agent import StudyAssistantAgent


def test_empty_input():
    agent = StudyAssistantAgent()
    result = agent.run("")

    assert "Error" in result


def test_direct_text_input():
    agent = StudyAssistantAgent()
    text = (
        "Python is a programming language used for automation and data analysis. "
        "It helps developers build useful software systems. "
        "Python projects can include tools, tests, and documentation."
    )

    result = agent.run(text)

    assert "Short Summary" in result
    assert "Generated Questions" in result
