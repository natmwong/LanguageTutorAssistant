import openai
from dotenv import find_dotenv, load_dotenv
import time
import json
import os

def show_json(obj):
    print(json.loads(obj.model_dump_json()))

# Retrieve API key
load_dotenv

client = openai.OpenAI()

class TutorAssistant:
    def __init__(self):  
        # Hardcoded ids created previously
        self.assistant_id = "asst_gunNdPVu1FxCBxklTFA8EVq5"
        self.thread_id = "thread_7EcmmSbdRJCxtTb3z5TOWWJ8"


        '''
        # Create assistant with instructions, model, and file retrieval
        tutor_assistant = client.beta.assistants.create(
            instructions="You are a personalized language learning assistant tasked with guiding learners through their language acquisition journey. Prompt the user to describe the language they want to learn, their experience in the language, points for improvement, and their intended goals such as learning more vocabulary or improving reading. Your role after involves suggesting tailored curriculum and exercises based on the learner's proficiency level and language learning goals. Different topics will produce different types of exercises. For conversation practice, you will speak to the user in the language they are learning to simulate daily conversation.  This includes using sayings and vocabulary that may be used in a day-to-day conversation. For pronunciation practice, provide words in phonetic alphabet, pinyin, romanization, etc. For cultural lessons, provide local slang/sayings and their context, and introduce cultural content by recommending popular songs, films, or stories. For reading comprehension, provide text and ask comprehension questions based on the text. For grammar practice, provide fill-in-the-blank questions for different tenses/conjugations. For vocabulary practice, also provide fill-in-the-blank questions. After the learner completes the exercises, provide constructive feedback on their performance, indicating whether their answers are correct or incorrect. If the learner struggles with an exercise or expresses difficulty, offer a lesson covering the relevant vocabulary and grammar concepts necessary to complete the task. Additionally, encourage the learner to provide feedback on the ease or difficulty of the exercises. Utilize this feedback to assess the effectiveness of the exercises and refine future exercises to better suit the learner's skill level and learning preferences.",
            name="Language Learning Tutor",
            tools=[{"type": "retrieval"}],
            model="gpt-3.5-turbo-1106",
        )
        # assistant ID: asst_gunNdPVu1FxCBxklTFA8EVq5
        self.assistant_id= tutor_assistant.id
        print(tutor_assistant.id)

        # Create thread
        # thread ID: thread_7EcmmSbdRJCxtTb3z5TOWWJ8
        thread= client.beta.threads.create()
        self.thread_id = thread.id
        print(thread.id)
        '''

    # Retrieve prompt/content from user and generate a response
    def generate_response(self, content):

        # Tells if the Assistant has completed processing the request
        def wait_on_run(run):
            while run.status == "queued" or run.status == "in_progress":
                run = client.beta.threads.runs.retrieve(
                    thread_id=self.thread.id,
                    run_id=run.id,
                )
                time.sleep(0.5)
            return run

        # Create a message to append to the thread
        message = client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content
        )

        # Execute the run
        run = client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id,
        )

        # Wait for completion
        wait_on_run(run)

    # Returns the list of Messages in a Thread
    def get_response(self):
        return client.beta.threads.messages.list(thread_id=self.thread.id, order="asc")
