
import sqlite3
#


import unittest
# import calc
import sqlite3


con = sqlite3.connect("database")
cur = con.cursor()

class IntegerArithmenticTestCase(unittest.TestCase):
    role = []
    name = []
    password = []
    questions = []
    answers = []
    scores = []
    students =[]
    qname=[]
    qtext=[]
    desc=[]
    def read_users_Table(self):
        cur.execute("SELECT * FROM entity")
        Data = cur.fetchall()
        for index,dat in enumerate(Data):
            self.role.append(dat[3])
            self.name.append(dat[1])
            self.password.append(dat[2])

    def check_question_table(self):
        cur.execute("SELECT * FROM entity")
        Data = cur.fetchall()
        for index, dat in enumerate(Data):
            self.qname.append(dat[2])
            # self.qtext.append(dat[4])
            self.desc.append(dat[3])



            #function to test if all the users registered have name, passwords and roles available
    def test_login(self):
        self.read_users_Table()
        self.assertEqual(len(self.role),len(self.name),len(self.password))
        self.check_question_table()
        self.assertEqual(len(self.qname),len(self.desc))




if __name__ == '__main__':
    unittest.main()
