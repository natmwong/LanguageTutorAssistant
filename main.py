import flet as ft
import json
from assistant import TutorAssistant

class Message():
    def __init__(self, role: str, text: str):
        self.role = role
        self.text = text

class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(message.role)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(message.role),
                ),
                ft.Column(
                    [
                        ft.Text(message.role, weight="bold"),
                        ft.Text(message.text, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ]

    def get_initials(self, user_name: str):
        return user_name[:1].capitalize()

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


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