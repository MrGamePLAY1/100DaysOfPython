class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def next_question(self):
        # Retrieve the question at the give question number
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Using input to then show the question
        answer_by_user = input(f'Q.{self.question_number}: {current_question.text} (True / False): ')

        # Checking answer
        self.check_answer(answer_by_user, current_question.answer)

    def check_answer(self, answer_by_user, correct_answer):
        if answer_by_user.lower() == correct_answer.lower():
            # Increase score by 1
            self.score += 1
            print(f'Correct! {self.score}/12')
        else:
            print('Incorrect \n')
        print(f'The correct answer was {correct_answer}. ')


    def still_has_questions(self):
        # Return true if there are still questions in the list
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f'\n Final score: {self.score}/{self.question_number}')
            return False


