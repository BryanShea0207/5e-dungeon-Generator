import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
class mainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(mainScreen, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Button(text='←'))
        self.add_widget(AsyncImage(source='dungon/Floor 1/Floor 1.jpg'))
        self.add_widget(Button(text='→'))

class App(App):

    def build(self):
        return mainScreen()
    
App().run()
