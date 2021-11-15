from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
import random
import easygui
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import pyautogui
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import os
import requests

from tkinter import messagebox
from tkinter import Tk
root = Tk()
root.withdraw()
user_screen_width, user_screen_height= pyautogui.size()
program_width = user_screen_width/3
program_height = user_screen_height/2
Window.size = (program_width, program_height)

def __init__():    
    if "assets" in os.listdir():
        for file in os.listdir("assets"):
            print (file)
            os.remove("assets/" + file)
        os.rmdir("assets")
    if not "assets" in os.listdir():
        os.mkdir("assets")
    if not "config.json" in os.listdir("assets"):
        config = open("assets\\config.json", "w")
        config.write
        config.close


def error_prompt(message):
    prompt = messagebox.showinfo(title = "Error",message = message)
    return prompt
    
Builder.load_string("""
<folder_selectScreen>:
    BoxLayout:
        orientation: 'vertical'
        size: root.size
        Label:
            text : 'Choose Where You Would Like To Download Images To'
        Button:
            id: button1
            text: 'Select Folder'
            on_release: root.update_selected()
        Label:
            id: label1
            text: 'You Have Selected: ' + root.selected
        Button:
            id: continue1
            text: 'Continue'
            on_release: root.continue_or_not()

<image_amountScreen>:
    BoxLayout:
        spacing: 1
        orientation: 'vertical'
        size: root.size
        Label:
            text : 'How many Images Would You Like to Download'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '-1000'
                on_press:
                    root.update_image_amount_m('1000')
            Button:
                text: '-100'
                on_press:
                    root.update_image_amount_m('100')
            Button:
                text: '-10'
                on_press:
                    root.update_image_amount_m('10')
            Button:
                text: '-1'
                on_press:
                    root.update_image_amount_m('1')
            Label:
                id: input
                text: str(root.input)
            Button:
                text: '+1'
                on_press:
                    root.update_image_amount_p('1')
            Button:
                text: '+10'
                on_press:
                    root.update_image_amount_p('10')
            Button:
                text: '+100'
                on_press:
                    root.update_image_amount_p('100')
            Button:
                text: '+1000'
                on_press:
                    root.update_image_amount_p('1000')
        Button:
            text: 'reset'
            on_press: root.reset()
        BoxLayout:

            orientation: 'horizontal'
            Button:
                id : previous1
                text : 'Previous'
                on_release:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "folder_select"
            Button:
                id: continue2
                text: 'Continue'
                on_release:
                    root.continue_or_not()

<Search_termsScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text : 'Select Search Terms:'
        GridLayout:
            cols : 3
            rows: 3
            ToggleButton:
                id : Lake
                text: 'Lake'
            ToggleButton:
                id : River
                text: 'River'
            ToggleButton:
                id : Sunset
                text: 'Sunset'
            ToggleButton:
                id : Sky
                text: 'Sky'
            ToggleButton:
                id : Ocean
                text: 'Ocean'
            ToggleButton:
                id : Moon
                text: 'Moon'
            ToggleButton:
                id : Urban
                text: 'Urban'
            ToggleButton:
                id : Cityscape
                text: 'Cityscape'
            ToggleButton:
                id : Cloudscape
                text: 'Cloudscape'
                on_press: 
                    root.press('Cloudscape',root.selected_terms)
                    root.update_selected_string(root.selected_terms)
                on_release: 
                    root.release('Cloudscape',root.selected_terms)
                    root.update_selected_string(root.selected_terms)
        Label:
            text : 'You Have Selected: ' + root.selected_string
""")

class folder_selectScreen(Screen):
    
    selected= StringProperty()
    
    def __init__(self, **kwargs):
        super(folder_selectScreen, self).__init__(**kwargs)
        self.selected = "Nothing"
    def update_selected(self):
        global continue_allowed
        selected = easygui.diropenbox()
        selected_after_check = None
        if selected == None:
            selected_after_check = self.selected
            continue_allowed = False
        if not selected == None:
            selected_after_check = selected
            continue_allowed = True
        self.selected = selected_after_check
    def continue_or_not(self):
        try:
            if not continue_allowed == None:
                if continue_allowed == True:
                    self.manager.transition.direction = 'left'
                    self.manager.current = "image_amount"
        except NameError:
            error_prompt("No Folder Selected")


class image_amountScreen(Screen):
    input = NumericProperty()
    def __init__(self, **kwargs):
        super(image_amountScreen, self).__init__(**kwargs)
        self.input = 1
    def update_image_amount_p(self,amount):
        self.input = int(self.input) + int(amount)
    def update_image_amount_m(self,amount):
        if not self.input == 0:
            if not int(self.input) - int(amount) < 0:
                self.input = int(self.input) - int(amount)
    def reset(self):
        self.input = 1
    def continue_or_not(self):
        continue_allowed = False
        if 1 <= self.input <=1000000:
            continue_allowed = True
        else:
            error_prompt("Selected Amount out of range 1-100000")
        
        if not continue_allowed == None:
            if continue_allowed == True:
                self.manager.transition.direction = 'left'
                self.manager.current = "search_terms"


class search_termsScreen(Screen):
    selected_terms = []

    def press(self,pressed,selected_terms):
        selected_terms.append(pressed)
    def release(self,released,selected_terms):
        selected_terms.remove(released)
    def update_selected_string(self,selected_terms):
        global selected_string
        selected_string = ", ".join(str(x) for x in selected_terms)
        print(selected_string)
    selected_string = selected_string



class Download_Background_ImagesApp(App):
    def build(self):
        global screens,sm
        sm = ScreenManager()
        sm.add_widget(folder_selectScreen(name="folder_select"))
        sm.add_widget(image_amountScreen(name="image_amount"))
        sm.add_widget(search_termsScreen(name="search_terms"))
        
        return sm

if __name__ == '__main__':
    __init__()
    Download_Background_ImagesApp().run()