from agent import StudyAssistantAgent


def main():
    print("AI Study Assistant")
    print("------------------")
    print("You can enter either:")
    print("1) a file path, for example: sample_files/sample_text.txt")
    print("2) direct text")
    print()

    user_input = input("Enter file path or text: ").strip()

    agent = StudyAssistantAgent()
    result = agent.run(user_input)

    print("\nRESULT")
    print("------")
    print(result)


if __name__ == "__main__":
    main()
