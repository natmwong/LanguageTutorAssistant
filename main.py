import flet as ft
import json
from assistant import TutorAssistant

class Message():
    def __init__(self, prompt: str):
        self.prompt = prompt


def main(page: ft.Page):
    page.title = "Language Tutor Assistant Chat"
    chat = ft.Column()
    new_message = ft.TextField()

    # Creating Language Tutor Assistant
    languageTutor = TutorAssistant()

    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        page.update()

        #get user prompt
        #generate response from the prompt
        #broadcast the tutor's response back to the user
        

    page.add(
        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )

ft.app(target=main)