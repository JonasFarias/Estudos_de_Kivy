from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


Builder.load_file("other.kv")


class ExternalKv(BoxLayout):
    pass


class Variables(BoxLayout):
    _text_ = StringProperty('Helo Word')

    def Pressing(self):
        self._text_ = ('Welcome')



class LogicalInterface(BoxLayout):
    def OnPressing(self, ID, input):
        print('Oi')
        ID.text = input.text

    def OnRelease(self, ID, input):
        print('ah')


class Binding(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='Texto')
        b1.bind(on_press=self.callback_funt)
        self.add_widget(b1)
    def callback_funt(self, event):
        print('Foi')

class TestApp(App):
    def build(self):
        return Binding()


TestApp().run()