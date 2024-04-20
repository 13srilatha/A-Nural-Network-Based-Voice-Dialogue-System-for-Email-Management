# import streamlit as st
# import pyttsx3
# import speech_recognition as sr
#
# # Initialize the TTS engine
# engine = pyttsx3.init()
#
#
# # Function to convert text to speech
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# # Simulated authentication (replace with your actual logic)
# USER_CREDENTIALS = {
#     "blindmail13@gmail.com": "Blind@123",
# }
#
#
# def authenticate_user(email, password):
#     return email in USER_CREDENTIALS and USER_CREDENTIALS[email] == password
#
#
# def login_page():
#     st.title("Blind-mailAI Login")
#
#     st.write("Click anywhere on the screen to start.")
#     speak("Welcome to voice mail assistance.")
#     speak("Enter your email address:")
#     st.write("Please enter your email or speak it.")
#     email = listen_for_input()
#     st.text_input("Enter your email address:", value=email)
#     speak("Enter your password:.")
#     st.write("Please enter your password or speak it.")
#     password = listen_for_input()
#     st.text_input("Enter your password:", value=password, type="password")
#
#     login_button = st.button("Login")
#     if login_button:
#         if authenticate_user(email, password):
#             st.session_state["logged_in"] = True
#             st.success("Login successful!")
#             speak("Login successful!")
#         else:
#             st.error("Invalid email or password.")
#             speak("Invalid email or password.")
#
#
# def listen_for_input():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
#
#     try:
#         input_text = recognizer.recognize_google(audio)
#         st.write("Recognized:", input_text)
#         return input_text
#     except sr.UnknownValueError:
#         st.error("Sorry, could not understand audio.")
#         speak("Login successful!")
#         return ""
#
#
# def display_inbox():
#     # Simulated inbox emails (replace with actual data)
#     speak("Login successful!")
#     inbox_emails = ["Email 1", "Email 2", "Email 3"]
#     st.title("Inbox")
#     for email in inbox_emails:
#         st.write(f"- {email}")
#
#
# def read_email():
#     # Simulated email reading (replace with actual functionality)
#     speak("Login successful!")
#     st.title("Read Email")
#     selected_email = st.selectbox("Select an email:", inbox_emails)
#     st.write(f"Reading email: {selected_email}")
#
#
# def search_email():
#     # Simulated email search (replace with actual functionality)
#     st.title("Search Email")
#     search_query = st.text_input("Enter search query:")
#     search_button = st.button("Search")
#     if search_button:
#         st.write(f"Searching for: {search_query}")
#
#
# def main():
#     if "logged_in" not in st.session_state:
#         login_page()
#     else:
#         speak("now you have successfully entered the blind-mailAI Dashoard choose your operation from Navigation to chosse Inbox say Inbox, to choose Compose Email say Compose Email!")
#         st.title("Blind-mailAI Dashboard")
#         st.sidebar.title("Navigation")
#         inbox_button = st.sidebar.button("Inbox")
#         compose_button = st.sidebar.button("Compose Email")
#         reply_button = st.sidebar.button("Reply Email")
#         forward_button = st.sidebar.button("Forward Email")
#         delete_button = st.sidebar.button("Delete Email")
#         quit_button = st.sidebar.button("Quit")
#
#         if inbox_button:
#             read_email()
#             search_email()
#         elif compose_button:
#             compose_email()
#         elif reply_button:
#             pass
#         elif forward_button:
#             pass
#         elif delete_button:
#             pass
#         elif quit_button:
#             pass
#
#
# if __name__ == "__main__":
#     main()
########################################################################################################################333
############################################################################################################################
# import streamlit as st
#
# # Simulated authentication (replace with secure hashing!)
# USER_CREDENTIALS = {"blindmail13@gmail.com": "hashed_password"}  # Placeholder
#
# def authenticate_user(email, password):
#     return email in USER_CREDENTIALS and USER_CREDENTIALS[email] == hash_password(password)  # Replace with secure hashing
#
# def hash_password(password):
#     # Implement a secure hashing algorithm (e.g., bcrypt)
#     pass  # Placeholder for actual hashing
#
# def login_page():
#     st.title("Blind-mailAI Login")
#     username = st.text_input("Enter your email address:")
#     password = st.text_input("Enter your password:", type="password")
#     login_button = st.button("Login")
#     if login_button:
#         if authenticate_user(username, password):
#             st.session_state["logged_in"] = True
#             st.success("Login successful!")
#         else:
#             st.error("Invalid email or password.")
#
#
# def compose_email():
#     st.title("Compose Email")
#     recipient = st.text_input("Recipient:")
#     subject = st.text_input("Subject:")
#     body = st.text_area("Body:")
#     send_button = st.button("Send Email")
#
#     if send_button:
#         if recipient and subject and body:  # Basic validation
#             # Call your email sending API here (replace with actual logic)
#             # Ensure secure handling of credentials and API keys
#             st.success("Email sent successfully!")  # Placeholder for success message from backend
#         else:
#             st.error("Please fill in all fields.")
#
#
# def read_email(selected_email):
#     st.title(selected_email["subject"])
#     st.write(f"From: {selected_email['from']}")
#     st.write(f"Body: {selected_email['body']}")
#
#     st.subheader("Actions")
#     reply_button = st.button("Reply")
#     forward_button = st.button("Forward")
#     delete_button = st.button("Delete")
#     quit_button = st.button("Back")
#
#     if reply_button:
#         reply_email(selected_email)
#     elif forward_button:
#         forward_email(selected_email)
#     elif delete_button:
#         # Implement logic for deleting email (replace with actual delete functionality)
#         pass
#     elif quit_button:
#         pass  # Back to main dashboard (handled in main function)
#
#
# def reply_email(email):
#     st.title("Reply Email")
#     subject = f"Re: {email['subject']}"  # Pre-fill subject with "Re:" prefix
#     body = st.text_area("Body:")
#     back_button = st.button("Back")
#
#     if back_button:
#         pass  # Back to read email (handled in read_email function)
#     else:
#         # Call your email replying API here (replace with actual logic)
#         # Ensure secure handling of credentials and API keys
#         if body:  # Basic validation for reply body
#             st.success("Reply sent successfully!")  # Placeholder for success message from backend
#         else:
#             st.error("Please enter a reply message.")
#
#
# def forward_email(email):
#     st.title("Forward Email")
#     recipient = st.text_input("Forward To:")
#     subject = st.text_input("Subject:", value=email["subject"])  # Pre-fill subject with option to edit
#     back_button = st.button("Back")
#
#     if back_button:
#         pass  # Back to read email (handled in read_email function)
#     else:
#         # Call your email forwarding API here (replace with actual logic)
#         # Ensure secure handling of credentials and API keys
#         if recipient:  # Basic validation for recipient
#             st.success("Email forwarded successfully!")  # Placeholder for success message from backend
#         else:
#             st.error("Please enter a recipient.")
#
#
# def display_inbox(emails):
#     st.title("Inbox")
#     for email in emails:
#         if st.button(f"{email['subject']} - {email['from']}"):
#             read_email(email)
#     st.write("---")
#     st.button("Logout")  # Add logout functionality
#
#
# def main():
#     if "logged_in" not in st.session_state:
#         login_page
#########################################################################################################################
# import streamlit as st
# from main import App
#
# def main():
#     st.title('Voice Controlled Email System')
#
#     @st.cache(allow_output_mutation=True)
#     def initialize_app():
#         return App()
#
#     app = initialize_app()
#
#     st.sidebar.title('Options')
#     selected_option = st.sidebar.radio('Select an action:', ['Send Email', 'Read Email', 'Help', 'Exit'])
#
#     if selected_option == 'Send Email':
#         st.write('Please speak "Send an email" to start sending an email.')
#     elif selected_option == 'Read Email':
#         st.write('Please speak "Read my emails" to start reading your emails.')
#     elif selected_option == 'Help':
#         st.write('Please speak "Help" to get assistance with available commands.')
#     elif selected_option == 'Exit':
#         st.write('Please speak "Exit" to quit the application.')
#
#     # Run the main loop of the app
#     app.main_loop()
#
# if __name__ == '__main__':
#     main()
##########################################################################################################################
# import streamlit as st
# import os
# import speech_recognition as sr
# import sounddevice as sd
# from google.cloud import texttospeech
# from graph import GraphDST
# from asr import ASRModule
# from myemail import EmailModule
# from understanding import UnderstandingModule
# import librosa
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{os.getcwd()}/data/tts_auth_key.json"
# os.environ['TOKENIZERS_PARALLELISM'] = 'true'
#
# USER_CREDENTIALS = {
#     "blindmail13@gmail.com": "Blind@123"  # Replace with a secure hash
# }
#
# def authenticate_user(email, password):
#     # Replace with secure password verification against a database or service
#     return email in USER_CREDENTIALS and USER_CREDENTIALS[email] == password
#
# def login_page():
#     st.title("Blind-mailAI Login")
#     username = st.text_input("Enter your email address:")
#     password = st.text_input("Enter your password:", type="password")
#     login_button = st.button("Login")
#
#     if login_button:
#         if authenticate_user(username, password):
#             st.session_state["logged_in"] = True
#             st.success("Login successful!")
#         else:
#             st.error("Invalid email or password.")
#
# class Speaker:
#
#     def __init__(self):
#         self.voice = texttospeech.VoiceSelectionParams(
#             language_code="en", name='en-IN-standard-A'
#         )
#
#         self.client = texttospeech.TextToSpeechClient()
#         # Select the type of audio file you want returned
#         self.audio_config = texttospeech.AudioConfig(
#             audio_encoding=texttospeech.AudioEncoding.MP3
#         )
#
#         # Perform the text-to-speech request on the text input with the selected
#         # voice parameters and audio file type
#
#     def say(self, text):
#         response = self.client.synthesize_speech(
#             input=texttospeech.SynthesisInput(text=text), voice=self.voice, audio_config=self.audio_config
#         )
#         with open(f"temp.mp3", "wb") as out:
#             # Write the response to the output file.
#             out.write(response.audio_content)
#
#         audio, sr = librosa.load('temp.mp3')
#         sd.play(audio, sr)
#         sd.wait()
# class App:
#     def __init__(self):
#         self.speaker = Speaker()
#         #self.speaker.say('loading forms, please wait')
#         self.understanding_module = UnderstandingModule()
#         self.asr_module = ASRModule()
#         self.opened_mail = []
#         self.mail_module = EmailModule()
#         self.graph_module = GraphDST()
#         #self.speaker.say('loading complete')
#         # initialize graph
#
#     def send_email_logic(self):
#         # Your email sending logic goes here
#         self.graph_module.print_graph()
#         if len(self.opened_mail) == 0:
#             text = self.asr_module.transcribe_audio(6)
#             print("ldone")
#             if not text:
#                 self.main_loop()
#                 return
#             intent, slots = self.understanding_module.process(text)
#             print(intent, slots)
#
#             # add successor
#
#             if intent == 'send_email' and len(self.opened_mail) == 0:
#                 self.speaker.say('send an email')
#                 self.graph_module.exchange('System', 'send an email')
#                 mail = {'object': None, 'person': None, 'body': None}
#                 for slots in slots:
#                     if slot[0] == 'object':
#                         mail['object'] = slot[1]
#                     elif slot[0] == 'person':
#                         mail['person'] = slot[1]
#                 self.graph_module.exchange('User', text, intent, slots)
#                 if all(field in mail.keys() for field in
#                        ['person', 'object', 'body']):  # Check if all fields are filled
#                     return mail['person'], mail['object'], mail['body']
#                 for field in mail.keys():
#                     if mail[field] is None:
#                         if field == 'person':
#                             self.speaker.say('who should this be sent to?')
#                             self.graph_module.exchange('System', 'who should it be sent to?')
#                             mail['person'] = self.asr_module.transcribe_audio()
#                             self.graph_module.exchange('User', mail['person'], None, [('person', mail['person'])])
#
#                         elif field == 'object':
#                             self.speaker.say('what\' is the subject?')
#                             self.graph_module.exchange('System', 'what is the object?')
#                             mail['object'] = self.asr_module.transcribe_audio()
#                             self.graph_module.exchange('User', mail['object'], None, [('person', mail['object'])])
#                             # update graph
#
#                         elif field == 'body':
#                             self.speaker.say('what is the body of the email?')
#                             self.graph_module.exchange('System', 'what is the body of the email?')
#                             mail['body'] = self.asr_module.transcribe_audio(10)
#                             self.graph_module.exchange('User', mail['body'], None, [('person', mail['body'])])
#                             # update graph
#
#                 if self.ask_confirm('send'):
#                     self.mail_module.dispatch_intent({'intent': intent, 'mail': mail})
#                     self.speaker.say('mail sent')
#                 self.main_loop()
#                 return
#         pass
#
# # def compose_email():
# #     st.title("Compose Email")
# #     subject = st.text_input("Subject:")
# #     body = st.text_area("Body:")
# #     recipient = st.text_input("Recipient:")
# #     send_button = st.button("Send Email", key="send")
# #
# #     if send_button:
# #         send_email_logic(subject, body, recipient)
#     def compose_email(self):
#         st.title("Compose Email")
#         recipient, subject, body = self.send_email_logic() or ("", "", "")
#         recipient_input = st.text_input("Recipient:", value=recipient if recipient else "")
#         subject_input = st.text_input("Subject:", value=subject if subject else "")
#         body_input = st.text_area("Body:", value=body if body else "")
#
#         if recipient == "" or subject == "" or body == "":
#             self.speaker.say("Missing information. Please provide the following:")
#             if recipient is None:
#                 self.speaker.say("Recipient")
#             if subject is None:
#                 self.speaker.say("Subject")
#             if body is None:
#                 self.speaker.say("Body")
#         send_button = st.button("Send Email", key="send")
#         if send_button:
#             # Send the email using the gathered information (recipient_input, subject_input, body_input)
#             # ... (implementation using your mail_module)
#             st.success("Email sent!")
#
#     def read_email(self):
#         st.title("Read Email")
#         # Placeholder for displaying/managing emails (implement using a mail API)
#         st.info("Email reading functionality not yet implemented (placeholder).")
#
#         forward_button = st.button("Forward Email (Disabled)")
#         reply_button = st.button("Reply Email (Disabled)")
#         delete_button = st.button("Delete Email (Disabled)")
#         quit_button = st.button("Quit")
#
#         # Disable read email buttons until functionality is implemented
#         forward_button.disabled = True
#         reply_button.disabled = True
#         delete_button.disabled = True
#
# def main():
#     if "logged_in" not in st.session_state:
#         login_page()
#     else:
#         st.title("Blind-mailAI Dashboard")
#         st.sidebar.title("Navigation")
#         send_mail_button = st.sidebar.button("Send Email")
#         read_mail_button = st.sidebar.button("Read Email")
#
#         if send_mail_button:
#             app = App()
#             app.compose_email()
#         elif read_mail_button:
#             app = App()
#             app.read_email()
#
#
# if __name__ == "__main__":
#     main()
import streamlit as st

USER_CREDENTIALS = {
  "blindmail13@gmail.com": "Blind@123" # Replace with a secure hash
}

def authenticate_user(email, password):
  # Replace with secure password verification against a database or service
  return email in USER_CREDENTIALS and USER_CREDENTIALS[email] == password

def login_page():
  st.title("Blind-mailAI Login")
  username = st.text_input("Enter your email address:")
  password = st.text_input("Enter your password:", type="password")
  login_button = st.button("Login")

  if login_button:
    if authenticate_user(username, password):
      st.session_state["logged_in"] = True
      st.success("Login successful!")
    else:
      st.error("Invalid email or password.")

def send_email_logic(self):
  # Your email sending logic goes here
  self.graph_module.print_graph()
  if len(self.opened_mail) == 0:
    text = self.asr_module.transcribe_audio(6)
    print("ldone")
    if not text:
      self.main_loop()
      return
    intent, slots = self.understanding_module.process(text)
    print(intent, slots)

    # add successor

    if intent == 'send_email' and len(self.opened_mail) == 0:
      self.speaker.say('send an email')
      self.graph_module.exchange('System', 'send an email')
      mail = {'object': None, 'person': None, 'body': None}
      for slots in slots:
        if slot[0] == 'object':
          mail['object'] = slot[1]
        elif slot[0] == 'person':
          mail['person'] = slot[1]
      self.graph_module.exchange('User', text, intent, slots)
      for field in mail.keys():
        if mail[field] is None:
          if field == 'person':
            self.speaker.say('who should this be sent to?')
            self.graph_module.exchange('System', 'who should it be sent to?')
            mail['person'] = self.asr_module.transcribe_audio()
            self.graph_module.exchange('User', mail['person'], None, [('person', mail['person'])])

          elif field == 'object':
            self.speaker.say('what\' is the subject?')
            self.graph_module.exchange('System', 'what is the object?')
            mail['object'] = self.asr_module.transcribe_audio()
            self.graph_module.exchange('User', mail['object'], None, [('person', mail['object'])])
            # update graph

          elif field == 'body':
            self.speaker.say('what is the body of the email?')
            self.graph_module.exchange('System', 'what is the body of the email?')
            mail['body'] = self.asr_module.transcribe_audio(10)
            self.graph_module.exchange('User', mail['body'], None, [('person', mail['body'])])
            # update graph

      if self.ask_confirm('send'):
        self.mail_module.dispatch_intent({'intent': intent, 'mail': mail})
        self.speaker.say('mail sent')
      self.main_loop()
      return
  pass

def compose_email():
  st.title("Compose Email")
  subject = st.text_input("Subject:")
  body = st.text_area("Body:")
  recipient = st.text_input("Recipient:")
  send_button = st.button("Send Email", key="send")

  if send_button:
    send_email_logic()

def read_email():
  st.title("Read Email")
  # Placeholder for displaying/managing emails (implement using a mail API)
  #st.info("Email reading functionality not yet implemented (placeholder).")

  forward_button = st.button("Forward Email")
  reply_button = st.button("Reply Email")
  delete_button = st.button("Delete Email")
  quit_button = st.button("Quit")

  # Disable read email buttons until functionality is implemented
  forward_button.disabled = True
  reply_button.disabled = True
  delete_button.disabled = True

def main():
  if "logged_in" not in st.session_state:
    login_page()
  else:
    st.title("Blind-mailAI Dashboard")
    st.sidebar.title("Navigation")
    send_mail_button = st.sidebar.button("Send Email")
    read_mail_button = st.sidebar.button("Read Email")

    if send_mail_button:
      compose_email()
    elif read_mail_button:
      read_email()

if __name__ == "__main__":
  main()