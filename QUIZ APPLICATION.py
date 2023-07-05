import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore

widgets={
    "button1": [],
    "button2": [],
    "question1": [],
    "option1": [],
    "Pause": [],
    "Resume": [],
    "Next/End": [],
    "Back": [],
    "score": [],
    }

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Quiz Application")
window.setFixedWidth(1000)
window.setStyleSheet("background: white;")

grid=QGridLayout()
flo=QFormLayout()

option1=QLineEdit()
answerLst=['c','d','a','c','b']
list=[]

def useranswer():
    global option1
    text=option1.text()
    list.append(text)
    print(list)
    """
    fw=open("useranswer.txt","a+")
    fw.write(text)
    fw.close()
    """
    
def clear_widgets():
    for widget in widgets:
        if widgets[widget]!=[]:
            widgets[widget][-1].hide()
        for i in range(0,len(widgets[widget])):
            widgets[widget].pop()

def show_frame1():
    clear_widgets()
    frame1()

def start_question1():
    clear_widgets()
    frame2()

def start_question2():
    clear_widgets()
    frame3()

def start_question3():
    clear_widgets()
    frame4()

def start_question4():
    clear_widgets()
    frame5()

def start_question5():
    clear_widgets()
    frame6()

def start_displayscore():
    clear_widgets()
    frame7()

def create_buttons(answer,l_margin,r_margin):
        button=QPushButton(answer)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(300)
        button.setStyleSheet(
        "*{background-color: #4169E1;" +
        "margin-left: " + str(l_margin) +"px;" +
        "margin-right: " + str(r_margin) +"px;" +
        "border: 4px solid blue;" +
        "border-radius: 15px;" +
        "font-size: 16px;" +
        "color: 'white';" +
        "padding: 10px 0;" +
        "margin-top: 5px;}" +
        "*:hover{background: solid blue;}"
        )
        button.clicked.connect(show_frame1)
        return button

def frame1():
    #button widget
    button1=QPushButton("START QUIZ")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button1.setStyleSheet(
        "*{background-color: #4169E1;" +
        "border: 4px solid blue;" +
        "border-radius: 30px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 0 250px;}" +
        "*:hover{background: solid blue;}"
        )
    button1.clicked.connect(start_question1)
    widgets["button1"].append(button1)
    
    button2=QPushButton("VIEW")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2.setStyleSheet(
        "*{background-color: #4169E1;" +
        "border: 4px solid blue;" +
        "border-radius: 30px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;"
        "margin: 0 250px;}" +
        "*:hover{background: solid blue;}"
        )
    widgets["button2"].append(button2)

    grid.addWidget(widgets["button1"][-1],0,0)
    grid.addWidget(widgets["button2"][-1],1,0)

def frame2():
    question1=QLabel("1. Who developed Python Programming Language?\n    a)Wick van Rossum\n    b)Rasmus Lerdorf\n    c)Guido van Rossum\n    d)Niene Stom\n\nEnter Option:")
    question1.setAlignment(QtCore.Qt.AlignLeft)
    question1.setWordWrap(True)
    question1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 75px;"
        )
    widgets["question1"].append(question1)
    
    text=""
    
    option1.textChanged.connect(useranswer)
    
    option1.setAlignment(QtCore.Qt.AlignLeft)
    option1.setFixedWidth(100)
    option1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 20px;" +
        "color: 'black';" +
        "padding: 15px;"
        )
    widgets["option1"].append(option1)

    button1=create_buttons("Pause",100,5)
    button2=create_buttons("Resume",5,10)
    button3=create_buttons("Next/End",5,100)
    
    widgets["Pause"].append(button1)
    widgets["Resume"].append(button2)
    widgets["Next/End"].append(button3)
          
    button3.clicked.connect(start_question2)
    
    grid.addWidget(widgets["question1"][-1],0,1,1,3)
    grid.addWidget(widgets["option1"][-1],0,2,17,5)
    grid.addWidget(widgets["Pause"][-1],2,1)
    grid.addWidget(widgets["Resume"][-1],2,2)
    grid.addWidget(widgets["Next/End"][-1],2,3)

def frame3():
    global option1
    question1=QLabel("2. Which type of Programming does Python support?\n    a)object-oriented programming\n    b)structured programming\n    c)functional\n    d)all of the mentioned\n\nEnter Option:")
    question1.setAlignment(QtCore.Qt.AlignLeft)
    question1.setWordWrap(True)
    question1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 75px;"
        )
    widgets["question1"].append(question1)

    option1=QLineEdit()

    text=""
    
    option1.textChanged.connect(useranswer)

    option1.setAlignment(QtCore.Qt.AlignLeft)
    option1.setFixedWidth(100)
    option1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 20px;" +
        "color: 'black';" +
        "padding: 15px;"
        )
    widgets["option1"].append(option1)

    button1=create_buttons("Pause",100,5)
    button2=create_buttons("Resume",5,10)
    button3=create_buttons("Next/End",5,100)

    button3.clicked.connect(start_question3)

    widgets["Pause"].append(button1)
    widgets["Resume"].append(button2)
    widgets["Next/End"].append(button3)
    
    grid.addWidget(widgets["question1"][-1],0,1,1,3)
    grid.addWidget(widgets["option1"][-1],0,2,17,5)
    grid.addWidget(widgets["Pause"][-1],2,1)
    grid.addWidget(widgets["Resume"][-1],2,2)
    grid.addWidget(widgets["Next/End"][-1],2,3)

def frame4():
    global option1
    question1=QLabel("3. Is Python case sensitive when dealing with identifiers?\n    a)no\n    b)yes\n    c)machine dependent\n    d)none of the mentioned\n\nEnter Option:")
    question1.setAlignment(QtCore.Qt.AlignLeft)
    question1.setWordWrap(True)
    question1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 75px;"
        )
    widgets["question1"].append(question1)

    option1=QLineEdit()
    text=""
    
    option1.textChanged.connect(useranswer)
    
    option1.setAlignment(QtCore.Qt.AlignLeft)
    option1.setFixedWidth(100)
    option1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 20px;" +
        "color: 'black';" +
        "padding: 15px;"
        )
    widgets["option1"].append(option1)

    button1=create_buttons("Pause",100,5)
    button2=create_buttons("Resume",5,10)
    button3=create_buttons("Next/End",5,100)

    button3.clicked.connect(start_question4)

    widgets["Pause"].append(button1)
    widgets["Resume"].append(button2)
    widgets["Next/End"].append(button3)
    
    grid.addWidget(widgets["question1"][-1],0,1,1,3)
    grid.addWidget(widgets["option1"][-1],0,2,17,5)
    grid.addWidget(widgets["Pause"][-1],2,1)
    grid.addWidget(widgets["Resume"][-1],2,2)
    grid.addWidget(widgets["Next/End"][-1],2,3)

def frame5():
    global option1
    question1=QLabel("4. Which of the following is the correct extension of the Python file?\n    a).python\n    b).pl\n    c).py\n    d).p\n\nEnter Option:")
    question1.setAlignment(QtCore.Qt.AlignLeft)
    question1.setWordWrap(True)
    question1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 75px;"
        )
    widgets["question1"].append(question1)

    option1=QLineEdit()
    text=""
    
    option1.textChanged.connect(useranswer)

    
    option1.setAlignment(QtCore.Qt.AlignLeft)
    option1.setFixedWidth(100)
    option1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 20px;" +
        "color: 'black';" +
        "padding: 15px;"
        )
    widgets["option1"].append(option1)

    button1=create_buttons("Pause",100,5)
    button2=create_buttons("Resume",5,10)
    button3=create_buttons("Next/End",5,100)

    button3.clicked.connect(start_question5)

    widgets["Pause"].append(button1)
    widgets["Resume"].append(button2)
    widgets["Next/End"].append(button3)
    
    grid.addWidget(widgets["question1"][-1],0,1,1,3)
    grid.addWidget(widgets["option1"][-1],0,2,17,5)
    grid.addWidget(widgets["Pause"][-1],2,1)
    grid.addWidget(widgets["Resume"][-1],2,2)
    grid.addWidget(widgets["Next/End"][-1],2,3)

def frame6():
    global option1
    question1=QLabel("5. Is Python code compiled or interpreted?\n    a)Python code is both compiled and interpreted\n    b)Python code is neither compiled and interpreted\n    c)Python code is only compiled\n    d)Python code is only interpreted\n\nEnter Option:")
    question1.setAlignment(QtCore.Qt.AlignLeft)
    question1.setWordWrap(True)
    question1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 75px;"
        )
    widgets["question1"].append(question1)

    option1=QLineEdit()

    text=""
    
    option1.textChanged.connect(useranswer)
    
    option1.setAlignment(QtCore.Qt.AlignLeft)
    option1.setFixedWidth(100)
    option1.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 20px;" +
        "color: 'black';" +
        "padding: 15px;"
        )
    widgets["option1"].append(option1)

    button1=create_buttons("Pause",100,5)
    button2=create_buttons("Resume",5,10)
    button3=create_buttons("Next/End",5,100)

    button3.clicked.connect(start_displayscore)

    widgets["Pause"].append(button1)
    widgets["Resume"].append(button2)
    widgets["Next/End"].append(button3)
    
    grid.addWidget(widgets["question1"][-1],0,1,1,3)
    grid.addWidget(widgets["option1"][-1],0,2,17,5)
    grid.addWidget(widgets["Pause"][-1],2,1)
    grid.addWidget(widgets["Resume"][-1],2,2)
    grid.addWidget(widgets["Next/End"][-1],2,3)

def frame7():
    total=0
    option1=QLineEdit()
    for i in range(0,len(answerLst)):
        if answerLst[i]==list[i]:
            total=total+1
    print("Total score: ",total,"/ 5")

    """
    score=QLabel("Total Score: ")
    score.setAlignment(QtCore.Qt.AlignLeft)
    score.setWordWrap(True)
    score.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'black';" +
        "padding: 75px;"
        )
    widgets["score"].append(score)
  
    button1=create_buttons("Back",100,5)

    button1.clicked.connect(show_frame1)

    widgets["Back"].append(button1)
    
    grid.addWidget(widgets["score"][-1],0,1,1,3)
    grid.addWidget(widgets["Back"][-1],2,3)
    """

frame1()
window.setLayout(grid)

window.show()
sys.exit(app.exec())

