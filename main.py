from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
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

user_screen_width, user_screen_height= pyautogui.size()
program_width = user_screen_width/3
program_height = user_screen_height/2
Window.size = (program_width, program_height)
if "assets" in os.listdir():
    for file in os.listdir("assets"):
        os.remove("assets/" + file)
    os.rmdir("assets")
if not "assets" in os.listdir():
    os.mkdir("assets")
if not "config.json" in os.listdir("assets"):
    config = open("assets\\config.json", "w")
    config.write
    config.close
    error_image = "assets/"

def error_prompt(message):
    image = "assets/error.png"
    return easygui.msgbox(message, image=image, title="Error")
    
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

<image_amount_and_image_dimensionsScreen>:
    BoxLayout:
        orientation: 'vertical'
        size: root.size
        Label:
            text : 'Image'
        Slider:
            id: slider
            min: 1
            max: 10000
            step: 1
            orientation: 'horizontal'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                id : previous1
                text : 'Previous'
                on_release: root.manager.current = "folder_select"
            Button:
                id: continue2
                text: 'Continue'
                on_release: root.manager.current = ""

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
                    self.manager.current = "image_amount_and_image_dimensions"
        except NameError:
            error_prompt("No Folder Selected")






class image_amount_and_image_dimensionsScreen(Screen):
    pass


class Download_Background_ImagesApp(App):
    def build(self):
        global screens,sm
        sm = ScreenManager()
        sm.add_widget(folder_selectScreen(name="folder_select"))
        sm.add_widget(image_amount_and_image_dimensionsScreen(name="image_amount_and_image_dimensions"))
        
        return sm

if __name__ == '__main__':
    Download_Background_ImagesApp().run()