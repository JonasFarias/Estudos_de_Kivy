from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout




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




class TestApp(App):
    pass

TestApp().run()