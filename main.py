import flet as ft
import json
from assistant import TutorAssistant

class Message():
    def __init__(self, role: str, text: str):
        self.role = role
        self.text = text


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

        #create a new user Message from entered prompt
        userRole, userMsg = languageTutor.get_userMsg(languageTutor.get_messages(thread))
        userMessage = Message(userRole, userMsg)
        #create a new assistant Message
        assistRole, assistMsg = languageTutor.get_assistMsg(languageTutor.get_messages(thread))
        assistMessage = Message(assistRole, assistMsg)
        #add user Message to chat
        chat.controls.append(ft.Text(f"{userMessage.role}: {userMessage.text}"))
        #add assistant Message to chat
        chat.controls.append(ft.Text(f"{assistMessage.role}: {assistMessage.text}"))


        # Reset text field and update page
        new_message.value = ""
        page.update()
        

    page.add(
        chat, ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])
    )

ft.app(target=main)