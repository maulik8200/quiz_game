import json

def main_menu():
    a = " \n====> Welcome to TOPS Quiz Challenge <===="
    print(a.center(40," "))
    print(""" \n Select your role
    -> \t Quiz master  \t (press 1)
    -> \t Quiz Cracker \t (press 2) \n""")

def display_menu():
     b = " \n===============> Welcome Master <==============="
     print(b.center(40," "))
     c = "Shake your Brain & add some Challenging Question.."
     print(c)
     print("\nQuiz Game Menu:")
     print("1. Add Question")
     print("2. View Questions")
     print("3. Delete Question")
     print("4. Exit")

def add_question(questions):
    question = input("Enter the question: ")
    options = input("Enter options separated by commas: ").split(',')
    correct_answer = input("Enter the correct answer: ")

    question_id = len(questions) + 1
    questions[question_id] = {
        'question': question,
        'options': options,
        'correct_answer': correct_answer
    }

def view_questions(questions):
    print("\nList of Questions:")
    for question_id, details in questions.items():
        print(f"{question_id}. {details['question']}")

def delete_question(questions):
    view_questions(questions)
    question_id_to_delete = int(input("Enter the question ID to delete: "))

    if question_id_to_delete in questions:
        del questions[question_id_to_delete]
        print("Question deleted successfully!")
    else:
        print("Invalid question ID. Deletion failed.")

def save_to_log(questions):
    with open('quiz_log.txt', 'a') as log_file:
        log_file.write(json.dumps(questions, indent=2))
        log_file.write("\n")

def quiz_cracker(questions):
    view_questions(questions)
    question_id = int(input("Enter the question ID to answer: "))

    if question_id in questions:
        selected_question = questions[question_id]
        print(f"\n{selected_question['question']}")
        for idx, option in enumerate(selected_question['options'], start=1):
            print(f"{idx}. {option}")

        user_answer = int(input("Enter your answer (option number): "))

        if user_answer == selected_question['options'].index(selected_question['correct_answer']) + 1:
            print("Correct answer!")
        else:
            print("Incorrect answer. The correct answer is:", selected_question['correct_answer'])
    else:
        print("Invalid question ID. Quiz cracking failed.")

def quiz_master():
    questions = {}
    while True:
        main_menu()
        user_input = input("Enter your role: ")

        if user_input == "1":
            display_menu()
            choice = input("\nWhich operations you want to perform: ")
            if choice == '1':
                add_question(questions)
            elif choice == '2':
                view_questions(questions)
            elif choice == '3':
                delete_question(questions)
            elif choice == '4':
                print("Exiting the Quiz Game.")
                save_to_log(questions)
                break
            else:
                print("Invalid choice. Please enter a valid option.")
        elif user_input == "2":
            quiz_cracker(questions)
        else:
            print("Invalid input. Please press 1 or 2.")

if __name__ == "__main__":
    quiz_master()