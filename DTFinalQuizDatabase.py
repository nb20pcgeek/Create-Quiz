import sqlite3

sqlite_file = 'DTFinalQuiz.db'
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()
sql = '''CREATE TABLE IF NOT EXISTS Questions
    (PID INTEGER PRIMARY KEY AUTOINCREMENT,
     Question text(50),
     AnswerOne text(50),
     AnswerTwo text(50),
     AnswerThree text(50),
     CorrectAns text(50))'''

cursor.execute(sql)

sql = "Insert into Questions (Question, AnswerOne, AnswerTwo, AnswerThree, CorrectAns) VALUES  \
('A ______ refers to a location in memory that holds a specific piece of data that can vary', 'function', 'variable', 'loop', 'variable'),\
('There are two types of loops in Python', 'If and Else', 'Function and Module', 'For and While', 'For and While'),\
('The forward(100) command in Turtle moves the cursor', 'Backward by 100 pixels', 'Forward by 100 spaces', 'Forward by 100 pixels', 'Forward by 100 pixels'),\
('Import Tkinter', 'imports Tkinter module', 'Draws a screen', 'Makes the program loop', 'imports Tkinter module'),\
('The While Loop runs as long as the condition', 'is false', 'is true', 'is <100', 'is true'),\
('An if/else statement uses elif when', 'you want to test multiple values', 'you only want to test one value', 'elif is a typo', 'you want to test multiple values'),\
('Everything in Python is', 'a function', 'a integer', 'an object', 'an object'),\
('_____ are written as comma-separated values (items) between square brackets', 'Lists', 'Integers', 'Floats', 'Lists'),\
('________ are positive or negative whole numbers with no decimal point.', 'integers', 'strings', 'floats', 'integers'),\
('Python _______  allows you to save your program and rerun it if you have errors.', 'shell>>>', 'IDLE(editor)', 'integer', 'IDLE(editor)'),\
('Set the size of pen to 10 in Turtle', 'turtle.pen(10)', 'turtle.pensize(10)', 'turtle.big()', 'turtle.pensize(10)'),\
('Set the shape of the pen to Arrow in Turtle', 'turtle.shape(arrow)', 'turtle.arrow(shape)', 'turtle.arrow', 'turtle.shape(arrow)'),\
('Which turtle command will NOT raise the pen so that no line is drawn', 'turtle.up()', 'turtle.pen(up)', 'turtle.penup()', 'turtle.pen(up)'),\
('Who originally created Python?', 'David Lee', 'Guido Van Rossum', 'Bram Moolenar', 'Guido Van Rossum'),\
('a=2 b=3 Which answer is correct for print(a,b)', 'a b', '2 3', '23', '2 3'),\
('c=4 d=6 Which answer is correct for print(a,b)', 'name a is not defined', '4 6', '10', 'name a is not defined'),\
('What SQL statement only reads the database', 'INSERT', 'UPDATE', 'SELECT', 'SELECT'),\
('Which SQL statement reads all records from the Question table', 'SELECT ALL FROM Question', 'SELECT * FROM Question', 'SELECT * from table', 'SELECT * FROM Question'),\
('What Database and Version are we using with Python', 'MySQLite 3', 'Oracle 2012', 'SQLite Version 3', 'SQLite Version 3'),\
('OOP is an acronym for: ', 'Object Online Programming', 'Online Oriented Programming', 'Object Oriented Programming', 'Object Oriented Programming'),\
('A database cursor:', 'Shows where you are on the screen', 'traverses database records', 'deletes records', 'traverses database records')"

cursor.execute(sql)



#This will print the data in the database
#Place sql variable below here:
sql = 'Select * FROM Questions'
cursor.execute(sql)
rows = cursor.fetchall()

for rows in rows:
    print(rows)

connection.commit()
connection.close()
