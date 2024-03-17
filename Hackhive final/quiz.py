import random
import os
import pyttsx3
from gtts import gTTS
import speech_recognition as sr

# Define the questions and answers
start_questions = {
    "Who wrote C++": "Bjarne Stroustrup",
    "Which is the fastest bird'?": "Ostrich",
    "What is the largest mammal?": "Blue whale",
    "What is the main programming language used for AI?": "Python"
}
def voice_output(dictate):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
        engine.say(dictate)
        engine.runAndWait()

def voice_input():
     recognizer = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        voice = recognizer.listen(source)
        try:
            print("Recognizing...")
            ans_text = recognizer.recognize_google(voice)
            print(f"Answer: {ans_text}")
            return ans_text
        except sr.UnknownValueError:
            print("Could not understand audio,please try again !!")
            # voice_input()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Function to generate a quiz
def generate_quiz(questions, num_questions=2):
    # Randomly select 2 questions for the quiz
    quiz_questions = random.sample(list(questions.items()), num_questions)
    return quiz_questions

# Function to present the quiz and calculate the score
def take_quiz(quiz_questions):
    score = 0
    for question, answer in quiz_questions:
        voice_output(question)
        print(question)
        user_answer = voice_input()
        print(user_answer)
        # user_answer = input(f"{question}")
        try :
            if user_answer.lower() == answer.lower():
                print("Correct!")
                voice_output("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {answer}")
                voice_output(f"Incorrect. The correct answer is {answer}")
        except:
            print("Please try again")
    return score

# Generate a quiz with 2 questions
quiz_questions = generate_quiz(start_questions, num_questions=3)
# print(quiz_questions)

# Take the quiz
score = take_quiz(quiz_questions)

print(f"Your score is: {score}/{len(quiz_questions)}")
voice_output(f"Your score is: {score}/{len(quiz_questions)}")
