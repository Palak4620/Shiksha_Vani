# import speech_recognition as sr

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
#     print(text)
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e)) 
from googlesearch import search
from googlesearch import GoogleSearch
# response = googlesearch.search("")
# query = input()
  
my_results_list = []  
for i in GoogleSearch.search("this is google",        # The query you want to run  
                tld = 'com',  # The top level domain  
                lang = 'en',  # The language  
                num = 10,     # Number of results per page  
                start = 0,    # First result to retrieve  
                stop = None,  # Last result to retrieve  
                pause = 2.0,  # Lapse between HTTP requests  
               ):  
    my_results_list.append(i)  
    print(i) 
# from googlesearch.googlesearch import GoogleSearch

# query = "Python programming"
# response = GoogleSearch().search(query)

# for result in response.results:
#     print(result.title)
#     print(result.link)
#     print(result.description)
#     print()