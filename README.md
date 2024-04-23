# Language Tutor Assistant App

This project is an OpenAI-powered chatbot designed to assist users in learning new languages. The chatbot suggests a tailored curriculum and exercises based on the language the user wants to learn. It also keeps a record of the user's language proficiency as they interact with the assistant.

## Features

- **Tailored Curriculum**: The chatbot suggests a personalized curriculum based on the language the user wants to learn. This curriculum is designed to help the user learn the language in the most efficient way possible.

- **Interactive Exercises**: The chatbot provides interactive exercises to help the user practice the language. These exercises are designed to be engaging and fun, making the learning process more enjoyable.

- **Language Proficiency Tracking**: The chatbot tracks the user's language proficiency through conversation history. This allows the user to visualize their progress and helps the chatbot adjust the curriculum and exercises to the user's level.

## How to Use

To use the Language Tutor Assistant, simply start a conversation with the chatbot and specify the language you want to learn, your experience in the language, possible points for improvement, and your intended goals such as learning more vocabulary or improving reading. The chatbot will then generate exercises, provide feedback, and suggest tailored curriculum based on your proficiency level and learning goals.

## Video Walkthrough

Here is a walkthrough of implemented stories:

<img src='https://github.com/natmwong/LanguageTutorAssistant/blob/main/LanguageTutorAssistantDemo.gif' title='Video Walkthrough' width='600' alt='Video Walkthrough' />

GIF created with [ScreenToGif](https://www.screentogif.com/) for Windows

## Future Improvements

We are constantly working to improve the Language Tutor Assistant. Future improvements include file retrieval study material, improving the accuracy of language proficiency tracking, and adding more user preferences.

## Notes

There was a fair bit of difficulty for me to figure out how to access the user and assistant messages separately so they could be displayed on the chat page. I figured I would have to create two functions: 1) get_userMsg() and 2) get_assistMsg(). These functions would allow me to retrieve the role and text held in those Messages and display them on the UI.

Another challenge in developing this project was prompt engineering. Generating the proper responses that the user would need for language learning requires delicate formulation of the instructions given to the Assistant to carry out.

## License

    Copyright [2024] [Natasha Wong]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0
