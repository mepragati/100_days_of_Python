class QuizBrain:
    score = 0
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def is_correct(self,user_answer,answer):
        return user_answer == answer

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        answer = input(f"Q.{self.question_number }: {current_question.text} (True/False)? : ")
        if self.is_correct(answer,current_question.answer):
            score+=1