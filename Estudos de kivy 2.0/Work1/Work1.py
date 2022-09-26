import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class Game(BoxLayout):
    button_list = []
    i = 0
    Alpha = ['A', 'B', 'C', 'D', 'E']

    def Create_Btn(self, stc):
        ALPHA = random.choice(self.Alpha)
        red = random.randrange(1, 10)
        green = random.randrange(1, 10)
        blue = random.randrange(1, 10)
        RED = red/10
        GREEN = green/10
        BLUE = blue/10
        btn = Button(text=ALPHA, size_hint=(None, None), size=(100, 100), background_color=(RED, GREEN, BLUE), background_normal= '')
        self.button_list.append(btn)
        stc.add_widget(self.button_list[self.i])
        self.i = self.i+1
        print('Button Create')

    def Delete_Btn(self, stc):
        stc.remove_widget(self.button_list[self.i-1])
        self.button_list.pop(self.i-1)
        self.i = self.i-1


class Buttons(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TestApp(App):
    pass


TestApp().run()