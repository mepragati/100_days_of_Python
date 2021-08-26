class QuizBrain:
    score = 0
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def is_correct(self,user_answer,answer):
        if user_answer.lower() == answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's Wrong!")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        answer = input(f"Q.{self.question_number }: {current_question.text} (True/False)? : ")
        self.is_correct(answer,current_question.answer)