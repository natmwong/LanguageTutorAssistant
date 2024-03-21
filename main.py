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
        # Get user prompt
        prompt = new_message.value

        # Generate response back from the prompt
        thread, run = languageTutor.create_thread_and_run(prompt)
        run = languageTutor.wait_on_run(run, thread)


        # Return tutor's response
        chat.controls.append(ft.Text(languageTutor.get_response(thread)))

        # Reset text field and update page
        new_message.value = ""
        page.update()
        

    page.add(
        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )

ft.app(target=main)