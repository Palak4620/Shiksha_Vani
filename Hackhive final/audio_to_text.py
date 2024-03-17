# import speech_recognition as sr
# import csv

# def write_to_csv(text, filename="output.csv"):
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Transcription"])
#         writer.writerow([text])
#     print(f"Transcription saved to {filename}")
# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Capture audio from the microphone
# with sr.Microphone() as source:
#     print("Listening...")
#     audio = recognizer.listen(source)

# # Use Google Web Speech API to convert audio to text
# try:
#     print("Recognizing...")
#     text = recognizer.recognize_google(audio)
#     print(f"Text: {text}")
#     # texts = [text]
#     # output_file = "temp_voice_text.csv"
#     # with open(output_file, 'w', newline='') as csvfile:
#     #     csv_writer = csv.writer(csvfile)
#     # csv_writer.writerows(["Text"])
#     # for text in texts:
#     #     csv_writer.writerow(texts)
#     # Function to write text to a CSV file

#     # print(f"Texts saved to {output_file}")
#     text = audio_to_text(audio_data)

# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))
import speech_recognition as sr
import csv

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to record audio from the user
def record_audio():
    with sr.Microphone() as source:
        print("Please say something...")
        audio_data = recognizer.listen(source)
        print("Audio recorded.")
    return audio_data

# Function to convert audio to text
def audio_to_text(audio_data):
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Text : {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Error with the request: {0}".format(e))
        return ""

# Function to write text to a CSV file
def write_to_csv(text, filename="audio_output.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Transcription"])
        writer.writerow([text])
    print(f"Transcription saved to {filename}")

# Main function
def main():
    # Record audio
    audio_data = record_audio()

    # Convert audio to text
    text = audio_to_text(audio_data)

    # Write text to CSV file
    write_to_csv(text)

if __name__ == "__main__":
    main()
