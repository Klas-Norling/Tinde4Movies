from SQLiteDB import searchTitle
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#Kivy tutorial: https://www.youtube.com/watch?v=QUHnJrFouv8&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=3&ab_channel=TechWithTim


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.inside = GridLayout()

        self.rows = 3
        self.inside.cols = 2
        self.inside.rows = 1
        
        self.input = TextInput(multiline = False)
        self.input.bind(on_text_validate = self.on_enter)

        self.searchButton = Button(text = "Search")
        self.searchButton.bind(on_press = self.on_pressed)
        
        self.inside.add_widget(self.input)
        self.inside.add_widget(self.searchButton)

        self.add_widget(Label(text = "Here is where the picture is displayed"))
        self.add_widget(self.inside)
        self.add_widget(Label(text='this is just a blank space'))
               

    def on_enter(instance, userInput):
        print(searchTitle(userInput.text))

    def on_pressed(self, instance):
        print(searchTitle(self.input.text))
        print("Pressed button")
        




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()