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
        self.width="page.window_width"
        self.expand=True
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
                    spacing=1,
                    expand=True,
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
    page.horizontal_alignment = "stretch"
    chat = ft.ListView(
        spacing=10,
        auto_scroll=True,
        expand=True,
    )
    new_message = ft.TextField(
        hint_text="Message your Language Tutor Assistant here...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
    )

    # Joining the chat function
    def join_click(e):
        page.dialog.open = False
        welcomeMessage = Message("Assistant", "Hello! I am your personalized language learning assistant. Please start off by telling me the language you want to learn, your experience in the language, possible points for improvement, and your intended goals such as learning more vocabulary or improving reading. I can then generate exercises, provide feedback, and suggest tailored curriculum based on your proficiency level and learning goals. How can I help you today?")
        welcomeChat = ChatMessage(welcomeMessage)
        chat.controls.append(welcomeChat)
        page.update()

    # Wecome the user with a pop up dialog
    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome to the Language Tutor Assistant!"),
        actions=[ft.ElevatedButton(text="Get started", on_click=join_click)],
        actions_alignment="end",
    )


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
        userChat = ChatMessage(userMessage)
        chat.controls.append(userChat)
        #add assistant Message to chat
        assistChat = ChatMessage(assistMessage)
        chat.controls.append(assistChat)


        # Reset text field and update page
        new_message.value = ""
        page.update()
        

    # Add everything to the page
    page.add(
        ft.Container(
            content=chat,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    tooltip="Send Message",
                    on_click=send_click,
                ),
            ]
        ),
    )

ft.app(target=main)