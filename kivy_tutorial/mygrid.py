import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


class GLayout(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print("Name: ", self.name.text, "Email: ", self.email.text)
        self.name.text = ""
        self.email.text = ""


kv = Builder.load_string('''
<GLayout>:
    name : name
    email: email

    GridLayout:
        cols:1
        size: root.width - 200, root.height - 200
        pos: 100,100

        GridLayout:
            cols:2

            Label:
                text: "Name: "

            TextInput:
                id:name
                multinline:False

            Label:
                text: "Email: "

            TextInput:
                id:email
                multinline:False

        Button:
            text:"Submit"
            on_press: root.btn()
''')


class MyApp(App):
    def build(self):
        return GLayout()


if __name__ == "__main__":
    MyApp().run()