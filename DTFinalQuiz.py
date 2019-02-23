#Programmer: Neva Buttrey   March 2018  version 1.0
#Modified from code I wrote in 2017 that randomized answers for a Bible Challenge
#Written to honor God and for students at Discipleship Tutorial, Murfreesboro, TN


#--------import modules
import random
from random import shuffle
from tkinter import *
import tkinter.messagebox as box
import tkinter.font as tkFont
import sqlite3


#--------Class Definition for Game
class DTQuiz:
    connection=0
    cursor=0
    rows=0
    location=0
    myverse = ' '
    selLocation = ' '
    rightans = 0
    wrongans = 0    
    rannum = 0
    moveforward = 'T'


#--------This method runs after the initializer completes and when the "Next Verse" button is clicked
    ''' this function randomly selects a question from the database and the generates 3 possible answers
    '''
    def  nxtQuestion(self):
        sql_file='DTFinalQuiz.db'
        self.table_name = 'Questions'
        self.id_column = 'PID'
        self.label.config(text = " ")
        self.selectedrows = " "
        selectionlist = [ ]
        self.loclist = [[ ],[ ]]
        self.rannum = random.randint(1,23)
                    
                
        # get one random record from database, store values in loclist
        self.connection = sqlite3.connect(sql_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * from Questions ORDER BY RANDOM() Limit 1")
        self.loclist = [list(item) for item in self.cursor.fetchall()]

 
##        for row in self.loclist:
##            print(self.loclist)


        self.txtQuestion.delete('1.0', END)
        self.r1.config(state='normal')
        self.r2.config(state='normal')
        self.r3.config(state='normal') 
            
        var.set(0)


        #print(self.chosen)          
        self.txtQuestion.insert(END, self.loclist[0][1])

        self.r1.config( text="",   value="")
        self.r1.config( text=self.loclist[0][2],  value=self.loclist[0][2])
        self.r2.config( text="",   value="")
        self.r2.config( text=self.loclist[0][3],  value=self.loclist[0][3])
        self.r3.config( text="",   value="")
        self.r3.config( text=self.loclist[0][4],  value=self.loclist[0][4])


    
#--------This method runs when the "End Game" button is clicked:
       
    def endgame(self):
        result = box.askquestion("END Game", "Are You Sure You Want to End the Game?", icon='warning')
        if result == 'yes':
            app.destroy()
 

    def sel(self):
        self.selLocation = var.get()
        if self.selLocation==self.loclist[0][5]:
            self.selection = (self.selLocation + " is correct")
            self.label.config(text = self.selection)
            self.rightans=self.rightans + 1
            #self.myscorecard.append(
            self.r1.config(state='disabled')
            self.r2.config(state='disabled')
            self.r3.config(state='disabled')
            moveforward = 'T'
            self.correct_label = Label(app, text =(" # Correct: " + str(self.rightans)) , font=self.customFont12)
            self.correct_label.grid(row = 5, column= 0)
            self.correct_label.configure(background='Sky Blue')
        else:
            self.selection = (var.get() + " is incorrect")
            self.label.config(text = self.selection)
            self.wrongans=self.wrongans + 1
            self.incorrect_label = Label(app, text =(" # Incorrect: " + str(self.wrongans)) , font=self.customFont12)
            self.incorrect_label.grid(row = 5, column= 1)
            self.incorrect_label.configure(background='Sky Blue')
            moveforward = 'F'
##        print(self.rightans )
##        print(self.wrongans )
##        print(self.loclist[self.chosen] [2])
        


#This method runs as soon as an object of this class is instantiated
    '''GUI for DT Quiz Game
    '''
    def __init__(self, app):

        app.title("Ms. Neva's Python Quiz for DT Students")
        app.geometry("800x400")
        app.configure(background='Sky Blue')
        self.customFont12 = tkFont.Font(family="Helvetica", size=12)
        selans=StringVar()
         
       
        # -----1st row ------
        scrollbar = Scrollbar(app)

        self.txtQuestion= Text(app, height=6, width=80, bd=6, relief=GROOVE)
        self.txtQuestion.grid(row=1, column=0, columnspan=3, padx=25, pady=25)
        self.txtQuestion.insert(END, " ")
        self.txtQuestion.configure(font=self.customFont12)

        # -----2nd row ------
        self.r1 = Radiobutton(app, text=" ",  variable=var , value=" ",
                              command=self.sel)
        self.r1.grid(row=2, column=0, padx=10, pady=10)
        self.r1.configure(background='Sky Blue', font=self.customFont12)
        self.r2 = Radiobutton(app, text=" ", variable=var, value=" ",
                              command=self.sel)
        self.r2.grid(row=2, column=1, padx=10, pady=10)
        self.r2.configure(background='Sky Blue', font=self.customFont12)
        self.r3 = Radiobutton(app, text=" ", variable=var, value=" ",
                              command=self.sel)
        self.r3.grid(row=2, column=2, padx=10, pady=10)
        self.r3.configure(background='Sky Blue', font=self.customFont12)
        var.set(0)

        # -----3rd row -------
        self.label = Label(app, )
        self.label.grid(row = 3, column = 1)
        self.label.configure(background='Sky Blue', font=self.customFont12)
        
        
        # -----4th row------
        self.scorelbl = Label(app, text = "Current Score ",  width = 15)
        self.scorelbl.grid(row = 4, column = 0, padx=10, pady=10)
        self.scorelbl.configure(background='Sky Blue', font=self.customFont12)

        # -----5th row------

        self.correct_label = Label(app, text =(" # Correct: " + str(self.rightans)) , font=self.customFont12)
        self.correct_label.grid(row = 5, column= 0)
        self.correct_label.configure(background='Sky Blue')


        self.incorrect_label = Label(app, text =(" # Incorrect: " + str(self.wrongans)) , font=self.customFont12)
        self.incorrect_label.grid(row = 5, column= 1)
        self.incorrect_label.configure(background='Sky Blue')

    

        # -----6th row------
        self.b1 = Button(app, text = "Next Question",  width = 15,
                         command=self.nxtQuestion)
        self.b1.grid(row = 6, column = 0, padx=10, pady=10)
        self.b1.configure(background='Sky Blue', font=self.customFont12)

        self.b2 = Button(app, text = "End Game",  width = 15,
                         command=self.endgame)
        self.b2.grid(row = 6, column = 1, padx=10, pady=10)
        self.b2.configure(background='Sky Blue', font=self.customFont12)



# Get the app window object
app = Tk()
var = StringVar()

#create the DTQuiz class instance
Neva=DTQuiz(app)
Neva.nxtQuestion()


# Run the app and keep visible until exited by user
app.mainloop()




