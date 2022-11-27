import kivy

from SQLiteDB import searchTitle
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

#Kivy tutorial: https://www.youtube.com/watch?v=QUHnJrFouv8&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=3&ab_channel=TechWithTim


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.rows = 2

        self.input = TextInput(multiline = False)
        self.input.bind(on_text_validate = self.on_enter)
        self.add_widget(self.input)
        
        
    def on_enter(instance, userInput):
        print(searchTitle(userInput.text))

        

        


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()