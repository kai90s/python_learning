from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        # label widget
        self.greet = Label(
                        text="What's your name?",
                        font_size= 18,
                        color='#FFFFFF'
                        )
        self.window.add_widget(self.greet)

        # text input widget
        self.user = TextInput(
                    multiline=False,
                    padding_y=(40, 10),
                    size_hint=(1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "GREET",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#FFFFCE',
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):

        self.greet.text = "Hello " + self.user.text + "!"


if __name__ == "__main__":
    SayHello().run()