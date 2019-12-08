from tinydb import TinyDB, Query
import random
questions=TinyDB('QandA.json')
find=Query()
#questions.purge()
def new_question(): #enter new question and 3 answer to DB
    question=input("Enter the question: ")
    ans1=input("Enter first answer: ")
    ans2=input("Enter second answer: ")
    ans3=input("Enter third answer: ")
    questions.insert({
        'questions':question,
        'answer':[ans1,ans2,ans3]
    })
    print("The question stock: ", questions.all())

def find_answer(question,answer):
    if questions.search(find.question==question & find.answer.all == answer ):
        return True
    return False

