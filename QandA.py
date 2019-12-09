from tinydb import TinyDB,Query,where
db=TinyDB('QandA.json')
find=Query()
db.purge()
def iter():
    it=0
    def iterator():
        nonlocal it
        it=it+1
        return it
    return iterator


def new_question(): #enter new question and 3 answer to DB
    question=input("Enter the question: ")
    ans1=input("Enter first answer: ")
    ans2=input("Enter second answer: ")
    ans3=input("Enter third answer: ")
    db.insert({'number':iter(),'questions':question,'answer1':ans1,'answer2':ans2,'answer3':ans3})

new_question()

def find_answer():
    #question=input("Enter the question to find: ")
    answer=input("Enter the answer to find: ")
    #result=db.search(where('answer1') == answer)
    if (db.search(find['answer1'] == answer)) or (db.search(find['answer2'] == answer)) or (db.search(find['answer3'] == answer)):
        return True
    return False
result=find_answer()
print(result)

