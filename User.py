from tinydb import TinyDB, Query
import unittest

userDB: TinyDB = TinyDB('UserDB.json')
userDB.purge()


def checkUser(name, id_num):
    # return true if user exist in DB
    tmp = Query()
    if userDB.search(tmp['name'] == name) and userDB.search(tmp['id'] == id_num):
        return True
    else:
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
    # return true if user have permit 'role'
    tmp = Query()
    if userDB.search((tmp['role'] == role) and (tmp['id'] == idn)):
        return True
    return False


def canSeeQuesion(idn):
    tmp = Query()
    userDB.search(tmp.id == idn)


class TestUser(unittest.TestCase):
    RegUser('tman', '!123')  # test manager user
    RegUser('tpar', '*123')  # test parent user
    RegUser('tkid', '123')  # test kid user

    def test_ability_to_test(self):
        x = 1
        self.assertEqual(x, 1)

    def test_RegUser(self):
        test = Query()
        self.assertTrue(userDB.search((test['name'] == 'tman') and (test['id'] == '!123')))
        self.assertTrue(userDB.search((test['name'] == 'tpar') and (test['id'] == '*123')))
        self.assertTrue(userDB.search((test['name'] == 'tkid') and (test['id'] == '123')))

    def test_CheckPermit(self):
        self.assertTrue(checkPermit('!123', 1))
        self.assertTrue(checkPermit('*123', 2))
        self.assertTrue(checkPermit('123', 3))

    def test_checkUser(self):
        self.assertTrue(checkUser('tman', '!123'))
        self.assertFalse(checkUser('ghost', '!123'))
        self.assertTrue(checkUser('tpar','*123'))
        self.assertFalse(checkUser('roei','!123'))


unittest.main()

RegUser('man', '!123456')
RegUser('man', '!1234')
RegUser('parent', '*123')
RegUser('kid', '123')
