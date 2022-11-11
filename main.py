from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.animation import Animation
from kivy.graphics import Color
from kivy.uix.textinput import  TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView
import json
from random import randint as rd
from datetime import datetime


Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "270")
Config.set("graphics", "height", "480")
Builder.load_file('Widgets.kv')

QuestionLine = 'Question'
global logs
logs = ""
global score
score = 0
global testcount
testcount = 0
global readingCount
readingCount = 0
global readingScore
readingScore = 0
global Time
time = ""
class MyLayout(Widget):
    def restart(self, *args):
        return MyApp().run()
    def Animate_it(self, widget, *args):

        animate = Animation(
            pos_hint = {"x": 1, "y": .45},
            background_color = (0,0,0,0),
            back_color = (0, 0, 0, 0),
            color = (0,0,0,0),
            duration = 1,
            disabled = True
        )
        animate.start(widget)
        animate.bind(on_complete = self.MainText)
    def Step1(self, *args):
        current_datetime = datetime.now()
        global Time
        Time = str(current_datetime)
        r_data = read("/Users/MacBook/Desktop/HeadStart Test/venv/ReadingTest.json")
        global reading
        reading = r_data['users']
        global score
        score = 0
        global testcount
        testcount = 0
        global readingCount
        readingCount = 0
        global readingScore
        readingScore = 0
        animLeftLabel = Animation\
            (
                pos_hint = {"center_x": -1},
                color = (0.1, .55, .05, 0),
                duration = 1.5,
                disabled=True
            )
        animLeftButton = Animation \
                (
                pos_hint={"center_x": -1},
                color=(0.1, .55, .05, 0),
                back_color = (0.1, .55, .05, 0),
                duration= 1.5,
                disabled=True
            )
        animLeftLabel.start(self.ids.second_main)
        animLeftButton.start(self.ids.Step1button)
        animRight = Animation\
            (
                pos_hint = {"center_x" : 1},
                color = (0.1, .55, .05, 0),
                duration=1.5,
                disabled=True

            )
        animRight.start(self.ids.main_text)
        animRight.start(self.ids.Info)
        animRight.bind(on_complete = self.step1)
    def step1(self, *args):
        n_data = read("/Users/MacBook/Desktop/HeadStart Test/venv/GeneralTest.json")
        global tests
        tests = n_data['users']
        anim_label1 = Animation\
            (
                pos_hint = {"x": -0.1, "y": .3},
                color = (0.1, .55, .05, 1)
            )
        anim_label1.start(self.ids.step1_0)
        anim_label2 = Animation\
            (
                pos_hint = {"x": 0, "y": .2},
                color = (.04, .1, .17, 1)
            )
        anim_label2.start(self.ids.step1_1)
        anim_Textinput1 = Animation\
            (
                pos_hint = {"x": .35, "y": .55},
                background_color = (.04, .1, .17, .3)
            )
        anim_Textinput1.start(self.ids.step1_2)
        anim_label3 = Animation\
            (
                pos_hint = {"x": 0, "y": -0.02},
                color=(.04, .1, .17, 1)
            )
        anim_label3.start(self.ids.step1_3)
        anim_Textinput2 = Animation\
            (
                pos_hint = {"x": .35, "y": .35},
                background_color=(.04, .1, .17, .3)
            )
        anim_Textinput2.start(self.ids.step1_4)
        anim4 = Animation\
            (
                pos_hint = {"x": 0.35, "center_y": 0.3},
                color=(0.1, .55, .05, 1),
                back_color = (0.1, .55, .05, 1)
            )
        anim4.start(self.ids.Step2)
    def Step2(self, *args):
        anim = Animation\
            (
                pos_hint = {"x": -.1, "y": .25},
                color=  (0.1, .55, .05, 1),
                duration = 2
            )
        anim.start(self.ids.step2_0)
        anim2 = Animation\
            (
                duration=2,
                color= (.04, .1, .17, 1),
                pos_hint= {"x": .075, "y": .076},

            )
        anim2.start(self.ids.step2_1)
        anim3 = Animation\
            (
                pos_hint = {"x": 1, "y": .3},
                color = (0.1, .55, .05, 0),
                disabled=True
            )
        anim3.start(self.ids.step1_0)
        anim4 = Animation\
            (
                color = (.04, .1, .17, 0),
                pos_hint = {"x": -1,},
                disabled=True

            )
        anim4.start(self.ids.step1_1)
        anim4.start(self.ids.step1_3)
        anim5 = Animation\
            (
                pos_hint = {"x": 1},
                background_color = (.04, .1, .17, 0),
                disabled = True,
                opacity = 0
            )
        anim5.start(self.ids.step1_2)
        anim5.start(self.ids.step1_4)
        anim6 = Animation\
            (
                pos_hint = {"x": 1},
                background_color = (.04, .1, .17, 0),
                disabled = True,
                opacity = 0,
                back_color = (0,0,0,0)
            )
        anim7 = Animation\
            (
                pos_hint = {"x": .35},
                background_color = (0,0,0,0),
                back_color = (0.1, .55, .05, 1),
                disabled = False,
                duration = 2
            )
        anim6.start(self.ids.Step2)
        anim7.start(self.ids.step2_2)
    def MainText(self, *args):
        anim = Animation(
            pos_hint={"center_y": 0.67, "center_x": 0.25},
            color = (.04, .1, .17, 1)
        )
        anim.start(self.ids.main_text)
        anim2 = Animation(
            pos_hint ={"center_y": 0.635, "center_x": 0.35},
            color = (0.1, .55, .05, 1)
        )
        anim2.start(self.ids.second_main)
        anim3 = Animation\
            (
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
                color = (.04, .1, .17, 1)
            )
        anim3.start(self.ids.Info)
        anim4 = Animation\
            (
                pos_hint = {"center_x": 0.5, "center_y": 0.3},
                color=(0.1, .55, .05, 1),
                back_color = (0.1, .55, .05, 1)
            )
        anim4.start(self.ids.Step1button)
        print("completed")

    def GrammarTestAnimationStart(self, *args):
        anim = Animation\
            (
                duration=2,
                color= (.04, .1, .17, 0),
                pos_hint= {"x": 1, "y": .076},

            )
        anim.start(self.ids.step2_1)
        anim1 = Animation \
                (
                pos_hint={"x": -1},
                background_color=(0, 0, 0, 0),
                back_color=(0.1, .55, .05, 0),
                disabled=True,
                duration=2
            )
        anim1.start(self.ids.step2_2)
        anim2 = Animation \
                (
                pos_hint={"x": -1, "y": .25},
                color=(0.1, .55, .05, 0),
                duration=2
            )
        anim2.start(self.ids.step2_0)
        anim.bind(on_complete = self.GeneralTest)
        anim.bind(on_complete = self.ChangeTest)
    def GeneralTest(self, *args):

        anim = Animation\
            (
                pos_hint =  {"x": .15},
                disabled=False,
                color = (0,0,0,1),
                back_color= (0.1, .55, .05, 1)

            )
        anim2 = Animation\
            (
                pos_hint = {"x": 0},
                disabled = False,
                color = (0,0,0,1)
            )
        anim2.start(self.ids.General_0)
        anim.start(self.ids.General_2)
        anim.start(self.ids.General_1)
        anim.start(self.ids.General_3)
    def Check1(self, *args):
        global SelectedAnswer
        SelectedAnswer = "Button 1"
        global Selected
        global question
        global score
        global logs
        answer = str(question['answer1'])
        selection = str(self.ids.General_1.text)
        if selection == answer:
            score += 1
            IsCorrect = "Right"
        else:
            IsCorrect = "Wrong" + "!" * 100
        Selected = f"{IsCorrect}\nID : {question['ID']} \nQuestion : {question['question']} \nAnswer 1 : {question['answer1']} \nAnswer 2 : {question['answer2']}\nAnswer 3 : {question['answer3']}\nSelected : {selection}\nScore : {score}\n\n\n"
        logs += Selected
        print(Selected)

    def Check2(self, *args):
        global SelectedAnswer
        SelectedAnswer = "Button 2"
        global Selected
        global question
        global score
        global logs
        answer = str(question['answer1'])
        selection = str(self.ids.General_2.text)
        if selection == answer:
            score += 1
            IsCorrect = "Right"
        else:
            IsCorrect = "Wrong" + "!" * 100
        Selected = f"{IsCorrect}\nID : {question['ID']} \nQuestion : {question['question']} \nAnswer 1 : {question['answer1']} \nAnswer 2 : {question['answer2']}\nAnswer 3 : {question['answer3']}\nSelected : {selection}\nScore : {score}\n\n\n"
        logs += Selected
        print(Selected)
    def Check3(self, *args):
        global SelectedAnswer
        SelectedAnswer = "Button 3"
        global Selected
        global question
        global score
        global logs
        answer = str(question['answer1'])
        selection = str(self.ids.General_3.text)
        if selection == answer:
            score += 1
            IsCorrect = "Right"
        else:
            IsCorrect = "Wrong" + "!" * 100
        Selected = f"{IsCorrect}\nID : {question['ID']} \nQuestion : {question['question']} \nAnswer 1 : {question['answer1']} \nAnswer 2 : {question['answer2']}\nAnswer 3 : {question['answer3']}\nSelected : {selection}\nScore : {score}\n\n\n"
        logs += Selected
        print(Selected)

    def CheckTest(self, *args):
        global testcount

        anim = Animation\
            (
                pos_hint = {"x": 1},
                back_color =  (0.1, .55, .05, 0),
                color = (0,0,0,0),
                duration = 1.5
            )
        if testcount < 40:
            anim += Animation\
                (
                    pos_hint={"x": .15},
                    disabled=False,
                    color=(0, 0, 0, 1),
                    back_color=(0.1, .55, .05, 1),
                    duration = 1.5
                )
        anim2 = Animation\
            (
                pos_hint = {"x": -1},
                back_color = (0.1, .55, .05, 0),
                color = (0, 0, 0, 0),
                duration = 1.5
            )
        if testcount < 40:
            anim2 += Animation\
                (
                    pos_hint={"x": .15},
                    disabled=False,
                    color=(0, 0, 0, 1),
                    back_color=(0.1, .55, .05, 1),
                    duration = 1.5
                )
        anim3 = Animation\
            (
                pos_hint = {"x": 1},
                color = (0,0,0,0),
                duration = 1.5
            )
        anim3.bind(on_complete=self.ChangeTest)
        if testcount < 40:
            anim3 += Animation\
                (
                    pos_hint = {"x": 0, "y": .35},
                    color = (0,0,0,1),
                    duration= 1.5
                 )

        anim.start(self.ids.General_2)
        anim2.start(self.ids.General_1)
        anim2.start(self.ids.General_3)
        anim3.start(self.ids.General_0)
        global SelectedAnswer
    def ChangeTest(self, *args):
        global tests
        global testcount
        if testcount != 0:
            global SelectedAnswer
        else:
            SelectedAnswer = ""
        if testcount < 40:
            testcount += 1
            lentest = len(tests)
            lentest = lentest - 1
            rand = rd(0, lentest)
            global question
            question = tests[rand]
            self.ids.General_0.text = str(question['question'])
            for i in range(3):
                answers = [str(question['answer1']), str(question['answer2']), str(question['answer3'])]
                r_ans = rd(0,2)
                self.ids.General_1.text = str(answers[r_ans])
                answers.pop(r_ans)
                r_ans = rd(0, 1)
                self.ids.General_2.text = str(answers[r_ans])
                answers.pop(r_ans)
                self.ids.General_3.text = str(answers[0])
                answers.pop(0)

            print(f"questions left : {lentest}")

            tests.pop(rand)
        else:
            anim = Animation\
                (
                    pos_hint = {"x": -.2, "y": .3},
                    color = (0.1, .55, .05, 1)
                )
            anim2 = Animation\
                (
                    color = (0,0,0,1),
                    pos_hint = {"x": 0, "y": .15}
                )
            anim3 = Animation\
                (
                    back_color = (0.1, .55, .05, 1),
                    pos_hint = {"x": .15, "y": .15},
                    color = ( 0.1, .55, .05, 1),
                    disabled = False
                )
            anim.start(self.ids.Reading_StartText)
            anim2.start(self.ids.Reading_Information)
            anim3.start(self.ids.Reading_StartButton)
            anim3.bind(on_complete = self.ChangeReading)
    def Start_Reading(self, *args):
        anim = Animation\
            (
                color = (0, 0, 0, 0),
                pos_hint = {"x": 1, "y": .15}
            )
        anim2 = Animation \
                (
                color=(0.1, .55, .05, 0),
                pos_hint={"x": -1, "y": .3}
            )
        anim3 = Animation\
            (
                pos_hint = {"x": -1, "y": .15},
                back_color =  (0.1, .55, .05, 0),
                color =  (0.1, .55, .05, 0),
                disabled = False
            )
        anim4 = Animation\
            (
                pos_hint = {"x": 0.05},
                disabled = False
            )
        anim5 = Animation\
            (
                color = (0, 0, 0, 1)
            )
        anim6 = Animation \
                (
                pos_hint={"x": .15},
                disabled=False,
                color=(0, 0, 0, 1),
                back_color=(0.1, .55, .05, 1)

            )
        anim7 = Animation\
            (
                pos_hint = {"x": 0, "y": -.325},
                color = (0, 0, 0, 1)
            )
        anim.start(self.ids.Reading_Information)
        anim2.start(self.ids.Reading_StartText)
        anim3.start(self.ids.Reading_StartButton)
        anim4.start(self.ids.Reading_Text)
        anim5.start(self.ids.Reading_Label)
        anim6.start(self.ids.Reading_1)
        anim6.start(self.ids.Reading_2)
        anim6.start(self.ids.Reading_3)
        anim7.start(self.ids.Reading_Question)
    def CheckReading(self, *args):
        global readingCount

        anim = Animation\
            (
                pos_hint = {"x": 1},
                back_color =  (0.1, .55, .05, 0),
                color = (0,0,0,0),
                duration = 1.5
            )
        if readingCount <= 5:
            anim += Animation\
                (
                    pos_hint={"x": .15},
                    disabled=False,
                    color=(0, 0, 0, 1),
                    back_color=(0.1, .55, .05, 1),
                    duration = 1.5
                )
        anim2 = Animation\
            (
                pos_hint = {"x": -1},
                back_color = (0.1, .55, .05, 0),
                color = (0, 0, 0, 0),
                duration = 1.5
            )

        if readingCount <= 5:
            anim2 += Animation\
                (
                    pos_hint={"x": .15},
                    disabled=False,
                    color=(0, 0, 0, 1),
                    back_color=(0.1, .55, .05, 1),
                    duration = 1.5
                )
        anim3 = Animation\
            (
                pos_hint = {"x": 1},
                color = (0,0,0,0),
                duration = 1.5
            )
        anim3.bind(on_complete=self.ChangeReading)

        if readingCount <= 5:
            anim3 += Animation\
                (
                    pos_hint = {"x": 0, "y": -.325},
                    color = (0,0,0,1),
                    duration= 1.5
                 )
        anim4 = Animation \
            (
                color = (0,0,0,0),
                duration = 1.5
            )
        if readingCount <= 5:
            anim4 += Animation\
                (
                    color=(0, 0, 0, 1),
                    duration = 1.5
                )
        anim5 = Animation\
            (
                pos_hint = {"x": -1, "y": .25},
                disabled = True,
                duration = 1.5,
                opacity = 0
            )
        if readingCount <= 5:
            anim5 += Animation(
                pos_hint={"x": 0.05},
                duration=1.5,
                disabled=False,
                opacity = 1
            )
        anim.start(self.ids.Reading_2)
        anim2.start(self.ids.Reading_1)
        anim2.start(self.ids.Reading_3)
        anim3.start(self.ids.Reading_Question)
        anim4.start(self.ids.Reading_Label)
        anim5.start(self.ids.Reading_Text)

    def Reading_Check1(self, *args):
        global SelectedReading
        SelectedAnswer = "Button 1"
        global r_question
        global readingScore
        global logs
        answer = str(r_question['answer1'])
        selection = str(self.ids.Reading_1.text)
        if selection == answer:
            readingScore += 5
            IsCorrect = "Right"
        else:
            IsCorrect = "Wrong" + "!" * 100
        Selected = f"{IsCorrect}\nID : {r_question['ID']} \nText : {r_question['readingText']} \nAnswer 1 : {r_question['answer1']} \nAnswer 2 : {r_question['answer2']}\nAnswer 3 : {r_question['answer3']}\nSelected : {selection}\nReading Score : {readingScore}\n\n\n"
        logs += Selected
        print(Selected)
    def Reading_Check2(self, *args):
        global SelectedReading
        SelectedAnswer = "Button 2"
        global r_question
        global readingScore
        global logs
        answer = str(r_question['answer1'])
        selection = str(self.ids.Reading_2.text)
        if selection == answer:
            readingScore += 1
            IsCorrect = "Right"
        else:
            IsCorrect = "Wrong" + "!" * 100
        Selected = f"{IsCorrect}\nID : {r_question['ID']} \nText : {r_question['readingText']} \nAnswer 1 : {r_question['answer1']} \nAnswer 2 : {r_question['answer2']}\nAnswer 3 : {r_question['answer3']}\nSelected : {selection}\nReading Score : {readingScore}\n\n\n"
        logs += Selected
        print(Selected)
    def Reading_Check3(self, *args):
        global SelectedReading
        SelectedAnswer = "Button 3"
        global r_question
        global readingScore
        global logs
        answer = str(r_question['answer1'])
        selection = str(self.ids.Reading_3.text)
        if selection == answer:
            readingScore += 5
            IsCorrect = "Right"
        else:
            IsCorrect = "Wrong" + "!" * 100
        Selected = f"{IsCorrect}\nID : {r_question['ID']} \nText : {r_question['readingText']} \nAnswer 1 : {r_question['answer1']} \nAnswer 2 : {r_question['answer2']}\nAnswer 3 : {r_question['answer3']}\nSelected : {selection}\nReading Score : {readingScore}\n\n\n"
        logs += Selected
        print(Selected)
    def ChangeReading(self, *args):

        global reading
        global readingCount
        print("Reading Counter : " + str(readingCount))
        if readingCount != 0:
            global SelectedAnswer
        else:
            SelectedAnswer = ""
        if readingCount <= 5:
            readingCount += 1
            lentest = len(reading)
            lentest = lentest - 1
            rand = rd(0, lentest)
            global r_question
            r_question = reading[rand]
            self.ids.Reading_Label.text = str(r_question['readingText'])
            self.ids.Reading_Question.text = str(r_question['question'])
            for i in range(3):
                answers = [str(r_question['answer1']), str(r_question['answer2']), str(r_question['answer3'])]
                r_ans = rd(0,2)
                self.ids.Reading_1.text = str(answers[r_ans])
                answers.pop(r_ans)
                r_ans = rd(0, 1)
                self.ids.Reading_2.text = str(answers[r_ans])
                answers.pop(r_ans)
                self.ids.Reading_3.text = str(answers[0])
                answers.pop(0)

            print(f"questions left : {lentest}")

            reading.pop(rand)
        else:
            global score
            global readingScore
            global Time
            global logs
            name = self.ids.step1_2.text
            self.ids.Grammar_Score.text = f"Name : {name}\nGrammar Test Score : {score}\nReading Score : {readingScore}\nLevel : Soon"
            anim = Animation\
                (
                    pos_hint = {"x": -.2, "y": .3},
                    color = (0.1, .55, .05, 1)
                )
            anim2 = Animation\
                (
                    color = (0,0,0,1),
                    pos_hint = {"x": 0, "y": .15}
                )
            anim3 = Animation\
                (
                    back_color = (0.1, .55, .05, 1),
                    pos_hint = {"x": .15, "y": .15},
                    color = ( 0.1, .55, .05, 1),
                    disabled = False
                )

            anim6 = Animation\
                (
                    pos_hint = {"x": .06, "y": 0},
                    color = (0, 0, 0, 1),
                )

            anim8 = Animation\
                (
                    pos_hint = {"x": .35},
                    back_color = (0.1, .55, .05, 1)
                )

            anim6.start(self.ids.Grammar_Score)
            anim8.start(self.ids.Restart)
            with open(f"Name : {name}, Time : {Time}.txt", 'w', encoding="utf-8") as file:
                file.write(logs)
                file.close()


def read(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
class MyApp(App):
    def build(self):
       return MyLayout()

if  __name__ == "__main__":
    MyApp().run()