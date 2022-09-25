from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class LogicalInterface(BoxLayout):
    def OnPressing(self, ID):
        print('Oi')
        ID.text = 'Bem vindo'

    def OnRelease(self):
        print('ah')




class TestApp(App):
    pass

TestApp().run()