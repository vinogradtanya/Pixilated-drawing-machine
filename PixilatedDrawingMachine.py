from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from random import random

class MainApp(App):
    def build(self):
        self.button_color = [0, 0, 0, 0]
        main_layout = GridLayout(cols = 30, rows = 31)

        for i in range(30):
            r, g, b = random(), random(), random()
            print(r, g, b)
            button = Button(background_color = [r, g, b, 1])
            button.bind(on_press = self.on_color)
            main_layout.add_widget(button)

        for j in range(30):
            for k in range(30):
                button = Button()
                button.bind(on_press = self.on_solution)
                main_layout.add_widget(button)

        return main_layout

    def on_solution(self, instance):
        instance.background_color = self.button_color

    def on_color(self, instance):
        self.button_color = instance.background_color


if __name__ == '__main__':
    MainApp().run()
