def new_game():
    guesses=[]
    correct_guess=0
    question_num=1
    for key in questions:
       print("--------------")
       print(key)
       for i in options[question_num-1]:
          print(i)
       guess=input("enter (A,B,C,D):")
       guess=guess.upper()
       guesses.append(guess)
       correct_guesses+=check_ans(questions.get(key),guess)
       questions_num+=1

def check_ans(ans,guess):
    if ans==guess:
       print("correct")
       return 1
    else:
       return 0

def display_score():
    pass

def play_again():
    pass


questions={
 "who is father of computer science?" "A"
 "for how many years leap year occurs?" "C"
 "who created python?" "D"
 "is the earth round?" "B"
}
options=[["A.Charles babbage", "B.james"],
        ["A.1", "B.2", "C.4", "D.3"],
        ["A.mark zuckerburg", "B.elon musk", "C.bill gates", "D.guido van rossum"],
        ["A.dopnt know", "B.yes", "C.sometimes", "D.Wt"]]
new_game()