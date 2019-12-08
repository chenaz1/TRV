from tinydb import TinyDB, Query

userDB: TinyDB = TinyDB('UserDB.json')


def CheckUser(user, id_num):
    tmp = Query()
    userDB.search((tmp.name == user) & (tmp.id == id_num))
    if userDB.search(tmp.name.exists()):
        return True
    return False


def RegUser(user, id_num):
    user = user.lower()
    user = user.lstrip()


    if id_num[0] == '!':
        role = 1  # Manager
    elif id_num[0] == '*':
        role = 2  # Parent
    else:
        role = 3  # kid
    userDB.insert({'name': user, 'id': id_num, 'role': role})


RegUser('kid', '123456789')
RegUser('adult', '*123456789')
RegUser('man', '!123456789')
