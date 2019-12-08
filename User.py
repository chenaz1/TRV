from tinydb import TinyDB, Query

userDB: TinyDB = TinyDB('UserDB.json')


def checkUser(name, id_num):
    # return true if user exist in DB
    tmp = Query()
    if userDB.search((tmp.name == name) & (tmp.id == id_num)):
        return True
    return False


def RegUser(name, id_num):
    # check if user exist, else register
    name = name.lower()
    name = name.lstrip()
    if checkUser(name, id_num):
        print('user exist in DataBase!')
    else:
        if id_num[0] == '!':
            role = 1  # Manager
        elif id_num[0] == '*':
            role = 2  # Parent
        else:
            role = 3  # kid
        userDB.insert({'name': name, 'id': id_num, 'role': role})


def checkPermit(idn, role):
    # return true if user have permit
    tmp = Query()
    if userDB.search((tmp['role'] == role) & (tmp.id == idn)):
        return True
    return False


userDB.purge()
RegUser('man', '!123456')
RegUser('man','!123456')
RegUser('man','!1234')
RegUser('parent', '*123')
RegUser('kid', '123')



