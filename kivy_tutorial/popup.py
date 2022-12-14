import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder


class P(FloatLayout):
    pass


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window",
                        content=show,
                        size_hint=(None, None),
                        size=(400, 400))
    popupWindow.open()


Builder.load_string('''
<Widgets>:
    Button:
        text:"Press me"
        on_release: root.btn()

<P>:
    Label:
        text: "You pressed the button"
        size_hint: 0.6, 0.2
        pos_hint: {"x":0.2, "top":1}

    Button:
        text: "You pressed the button"
        size_hint: 0.8, 0.2
        pos_hint: {"x":0.1, "y":0.1}
''')


class Widgets(Widget):
    def btn(self):
        show_popup()


class MyApp(App):
    def build(self):
        return Widgets()


if __name__ == "__main__":
    MyApp().run()
