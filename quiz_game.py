
# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "Who is the director of Baahubali Movie?",
        "options": ["A. Rajamouli", "B. Sukumar", "C. Shankar", "D. Koratala Siva"],
        "answer": "A"
    },
    {
        "prompt": "Who is Baahubali?",
        "options": ["A. Raana", "B. Prabhas", "C. SubbaRaju", "D. SatyaRaj"],
        "answer": "B"
    },
    {
        "prompt": "What is Anushka's character name?",
        "options": ["A. Avanthika", "B. Devasena", "C. Sivagaami", "D. Sanga"],
        "answer": "B"
    },
    {
        "prompt": "Who killed Baahubali?",
        "options": ["A. Kattappa", "B. BhallalaDeva", "C. Sethupathi", "D. Kumara Varma"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer is", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")


# Run the quiz
run_quiz(questions)