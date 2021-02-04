'''Develop an application called Quiz. Store 7 pairs of questions and answers in a dictionary.
The task is to ask 5 questions. The user enters the answers. For every correct answer 1 mark
is awarded. Finally, display the total score of the user.'''


print("Welcome to APP Quiz! Good luck! :)\n")
n = int(input("Please choose a question set [1 ; 2 ; 3 ; 4 ; 5]   :  "))
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What color are apples?\n(a)Red\n(b)Orange\n",
     "What color are bananas?\n(a)White\n(b)Yellow\n",
     "Who is the CEO of SpaceX?\n(a) Narendra Modi\n(b)Elon Musk\n",
     "Who is captain of Indian Football Team?\n(a) Virat Kohli\n(b)Sunil Chettri\n",
     "What is a Katana?\n(a)A sword\n(b)A rifle\n",
     "Who is the founder of Coca Cola?\n(a)Asa Griggs Candler\n(b)St. Lowda Lassan\n",
     "How many years from now can we see the Halley's Comet?\n(a)40 years\n(b)50 years\n",
     
]
if (n==1):
    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "a")
        
    ]
elif(n==2):
    questions = [
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "a"),
        Question(question_prompts[5], "a"),
        Question(question_prompts[6], "a")
        
    ]
elif(n==3):
    questions = [
        Question(question_prompts[1], "b"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "a"),
        Question(question_prompts[5], "a"),
        Question(question_prompts[6], "a")
        
    ]
elif(n==4):
    questions = [
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "a"),
        Question(question_prompts[5], "a"),
        Question(question_prompts[0], "a")
        
    ]
elif(n==5):
    questions = [
        Question(question_prompts[2], "b"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[5], "a"),
        Question(question_prompts[6], "a")
        
    ]
else:
    print("\nInvalid question set. Please choose between 1 to 5")
    
if(n==1 or n==2 or n==3 or n==4 or n==5):
    
    def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               
     if(score==len(questions)):
         print("Congrats! you got", score, "out of", len(questions))
     elif(score==len(questions)-1):
         print("Good! you got", score, "out of", len(questions))
     else:
         print("you got", score, "out of", len(questions))

    run_quiz(questions)
else:
    print("Error 505! Set not found")
