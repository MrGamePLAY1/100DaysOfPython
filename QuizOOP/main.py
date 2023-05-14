from question_model import Quiz
from data import question_data
from quiz_brain import QuizBrain

# Creating the question bank from the data file
question_bank = []

# Loop through all the questions in the data file
for question in question_data:
    # Variable to hold the question and answer
    text = question['text']
    # print(text)
    answer = question['answer']

    # Creating my new question object
    new_question = question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
