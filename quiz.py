import random
quiz_questions = [
    {
        "question": "What is the capital of India?",
        "choices": ["Mumbai", "Delhi", "Hyderabad", "Banaglore"],
        "answer": "Delhi"
    },
    {
        "question": "Under Akbar, the Mir Bakshi was required to look after",
        "choices": ["military affairs", "the state treasury", "the royal household", "the land revenue system"],
        "answer": "military affairs"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["O", "W", "H2O", "WA"],
        "answer": "H2O"
    },
    {
        "question": "tripitakas are sacred books of",
        "choices": ["Buddhists", "Hindus", "Jains", "None of the above"],
        "answer": "Buddhists"
    },
    {
        "question": "The percentage of irrigated land in india os about",
        "choices": ["45", "65", "35", "25"],
        "answer": "35"
    },
    {
        "question": "Which country did Ravi Shastri play for",
        "choices": ["Glamorgan", "Leicestershire", "Gloucestershire", "Lancashire"],
        "answer": "Glamorgan"
    },
    {
        "question": "Which country did Ravi Shastri play for",
        "choices": ["Glamorgan", "Leicestershire", "Gloucestershire", "Lancashire"],
        "answer": "Glamorgan"
    },
    {
        "question": "Which city is known for known as 'Electronic City of India'",
        "choices": ["Mumbai", "Hyderabad", "Guragon", "Bangalore"],
        "answer": "Bangalore"
    }   
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice or fill-in-the-blank questions on a specific topic.")
    print("Let's get started!\n")

def present_quiz_questions():
    score = 0
    for question_data in quiz_questions:
        print(question_data["question"])
        for i, choice in enumerate(question_data["choices"], 1):
            print(f"{i}. {choice}")

        user_answer = input("Your answer (type the choice number or the answer): ").strip()

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question_data["choices"]):
            user_answer = question_data["choices"][int(user_answer) - 1]

        if user_answer.lower() == question_data["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {question_data['answer']}\n")

    return score

def display_final_results(score):
    print("Quiz Completed!")
    print(f"Your final score: {score}/{len(quiz_questions)}")

    if score == len(quiz_questions):
        print("Congratulations! You got all the questions right!")
    elif score >= len(quiz_questions) // 2:
        print("Good job! You did well.")
    else:
        print("You can do better. Keep practicing!")

def play_again():
    return input("Do you want to play again? (yes/no): ").strip().lower() == "yes"

def main():
    display_welcome_message()
    
    play_game = True
    while play_game:
        random.shuffle(quiz_questions)
        score = present_quiz_questions()
        display_final_results(score)
        play_game = play_again()

    print("Thank you for playing the Quiz Game. Goodbye!")

if __name__ == "__main__":
    main()
