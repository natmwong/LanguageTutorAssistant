import openai
from dotenv import find_dotenv, load_dotenv
import time

# Retrieve API key
load_dotenv

client = openai.OpenAI(api_key="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")

class TutorAssistant:
    def __init__(self):  
        # Hardcoded ids created previously
        self.assistant_id = "asst_gunNdPVu1FxCBxklTFA8EVq5"


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
    def submit_prompt(self, thread, prompt):
        
        # Create a message to append to the thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=prompt
        )

        # Execute the run
        return client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant_id,
        )

    # Creates a new thread and run
    def create_thread_and_run(self, user_input):
        thread = client.beta.threads.create()
        run = self.submit_prompt(thread, user_input)
        return thread, run

    # Returns the list of Messages in a Thread
    def get_messages(self, thread):
        return client.beta.threads.messages.list(thread_id=thread.id, order="asc")
    
    # Pretty printing help
    def pretty_print(self, messages):
        result = ""
        for m in messages:
            result += f"{m.role}: {m.content[0].text.value}\n"
        return result

    # Tells if the Assistant has completed processing the request
    def wait_on_run(self, run, thread):
        while run.status == "queued" or run.status == "in_progress":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run

    # Return the chat messages of the user's prompt and the Assistant's response
    def get_response(self, thread):
        return self.pretty_print(self.get_messages(thread))
