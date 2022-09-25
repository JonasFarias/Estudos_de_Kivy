from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button


class Page_Layout(PageLayout):
    pass


class Page1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='Uma grande História começa aqui')
        b2 = Button(text='Continua a grande HIstoria')
        self.add_widget(b1)
        self.add_widget(b2)


class Page2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='Grandes coisas aconteceram')
        b2 = Button(text='Nossa que inesperado')
        self.add_widget(b1)
        self.add_widget(b2)


class Page3(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='Realmente surpreendente')
        b2 = Button(text='final')
        self.add_widget(b1)
        self.add_widget(b2)





# App Creation


class TestApp(App):
    pass


TestApp().run()
