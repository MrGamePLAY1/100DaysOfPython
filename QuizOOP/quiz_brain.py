class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        # Retrieve the question at the give question number
        current_question = self.question_list[self.question_number]

        # Using input to then show the question
        user_answer = input(f'Q.{self.question_number}: {current_question.text} (True / False): ')
        self.question_number += 1