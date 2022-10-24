from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import datetime


class Register(Screen):
    reg_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    matric_number = ObjectProperty(None)

    def submit(self):
        if self.reg_name.text != "" and self.matric_number.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.reg_name.text, self.matric_number.text)

                self.reset()

                sm.current = "Login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "Login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.reg_name.text = ""
        self.matric_number.text = ""


class Login(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            Main.current = self.email.text
            self.reset()
            sm.current = "Main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "Register"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class Main(Screen):
    account_name = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    matric_number = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "Login"

    def on_enter(self, *args):
        password, name, matric_number, created = db.get_user(self.current)
        self.account_name.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.matric_number.text = "Matric Number: " + matric_number
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


Builder.load_string('''

<Register>:
    name: "Register"

    reg_name: namee
    email: email
    password: passw
    matric_number:matnum
    GridLayout:
        cols:1
        
        Label:
            text: "Create an Account"
            size_hint: 0.8, 0.2
            
            font_size: (root.width**2 + root.height**2) / 14**4
        
        GridLayout:
            cols:2

            Label:
                size_hint: 0.5,0.12

                text: "Name: "
                font_size: (root.width**2 + root.height**2) / 14**4

            TextInput:

                size_hint: 0.4, 0.12
                id: namee
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4

            Label:
                size_hint: 0.5,0.12

                text: "Email: "
                font_size: (root.width**2 + root.height**2) / 14**4

            TextInput:

                size_hint: 0.4, 0.12
                id: email
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4

            Label:
                size_hint: 0.5,0.12

                text: "Password: "
                font_size: (root.width**2 + root.height**2) / 14**4

            TextInput:

                size_hint: 0.4, 0.12
                id: passw
                multiline: False
                password: True
                font_size: (root.width**2 + root.height**2) / 14**4
            Label:
                size_hint: 0.5,0.12

                text: "Matric: "
                font_size: (root.width**2 + root.height**2) / 14**4

            TextInput:

                size_hint: 0.4, 0.12
                id: matnum
                multiline: False
                font_size: (root.width**2 + root.height**2) / 14**4
                
        Button:
            size_hint: 0.4, 0.1
            font_size: (root.width**2 + root.height**2) / 17**4
            text: "Already have an Account? Log In"
            on_release:
                root.manager.transition.direction = "left"
                root.login()

        Button:

            size_hint: 0.6, 0.15
            text: "Submit"
            font_size: (root.width**2 + root.height**2) / 14**4
            on_release:
                root.manager.transition.direction = "left"
                root.submit()


<Login>:
    name: "Login"

    email: email
    password: password

    GridLayout:
        cols:1
        Label:
            text:"Login UI "
            font_size: (root.width**2 + root.height**2) / 13**4
            
            size_hint: 0.35, 0.15
            
        Label:
            text:"Email: "
            font_size: (root.width**2 + root.height**2) / 13**4
            
            size_hint: 0.35, 0.15

        TextInput:
            id: email
            font_size: (root.width**2 + root.height**2) / 13**4
            multiline: False
            
            size_hint: 0.4, 0.15

        Label:
            text:"Password: "
            font_size: (root.width**2 + root.height**2) / 13**4
            
            size_hint: 0.35, 0.15

        TextInput:
            id: password
            font_size: (root.width**2 + root.height**2) / 13**4
            multiline: False
            password: True
            
            size_hint: 0.4, 0.15
        
        Button:
            size_hint: 0.4, 0.1
            font_size: (root.width**2 + root.height**2) / 17**4
            text: "Don't have an Account? Create One"
            on_release:
                root.manager.transition.direction = "right"
                root.createBtn()
        
        Button:
            
            size_hint: 0.6, 0.2
            font_size: (root.width**2 + root.height**2) / 13**4
            text: "Login"
            on_release:
                root.manager.transition.direction = "up"
                root.loginBtn()

        


<Main>:
    account_name: Acc_name
    email: email
    matric_number:matnum
    created:created

    GridLayout:
        cols: 1
        Label:
            id: Acc_name
            
            size_hint:0.8, 0.2
            text: "Account Name: "

        Label:
            id: email
            
            size_hint:0.8, 0.2
            text: "Email: "

        Label:
            id: matnum
            
            size_hint:0.8, 0.2
            text: "Matric Number: "
    
        Label:
            id: created
            
            size_hint:0.8, 0.2
            text: "Created: "

        Button:
            size_hint:0.6,0.15
            font_size: (root.width**2 + root.height**2) / 14**4
            text: "Log Out"
            on_release:
                app.root.current = "Login"
                root.manager.transition.direction = "down"
''')

sm = WindowManager()


screens = [Login(name="Login"), Register(name="Register"), Main(name="Main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "Login"


class DB:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, matric_number, created = line.strip().split(";")
            self.users[email] = (password, name, matric_number, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name, matric_number):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), matric_number.strip(), DB.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + ";" + self.users[user][3] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


db = DB("db.txt")


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
