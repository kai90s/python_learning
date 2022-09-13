from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_string('''
WindowManager:
    MainWindow:
    SecondWindow:

<MainWindow>:
    name: "Main"

    GridLayout:
        cols: 1

        GridLayout:
            cols: 2

            Label:
                text: "Password: "

            TextInput:
                id:passw
                multiline: False
        Button :
            text: "Submit"
            on_release:
                app.root.current = "Second" if passw.text == "kai" else "Main"
                root.manager.transition.direction = "left"

<SecondWindow>:
    name: "Second"

    Button:
        text: "Go back"

        on_release:
            app.root.current = "Main"
            root.manager.transition.direction = "right"
''')


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()