import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

class FloatLayout(FloatLayout):
    pass


kv = Builder.load_string('''
<FloatLayout>:
    Button:
        pos_hint: {"x":0.5,"top":1}
        text:"Test"

    Button:
        id:btn
        pos_hint:{"y":0.3}
        text:"Test2" if btn.state == "normal" else "Down"
        background_color: 0.3,0.4,0.5,1

<Button>:
    font_size:40
    color:0.3,0.6,0.7,1
    size_hint:0.3,0.6


''')


class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()