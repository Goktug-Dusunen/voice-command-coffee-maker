import random
import nltk
import pyttsx3
import speech_recognition as sr

def get_coffee_order():
    print("What type of coffee would you like? (espresso, latte, cappuccino, americano)")
    coffee_order = input().lower()
    return coffee_order

def make_coffee(coffee_order):
    if coffee_order == "espresso":
        print("Here is your espresso. Enjoy!")
    elif coffee_order == "latte":
        print("Here is your latte. Enjoy!")
    elif coffee_order == "cappuccino":
        print("Here is your cappuccino. Enjoy!")
    elif coffee_order == "americano":
        print("Here is your americano. Enjoy!")
    else:
        print("Sorry, we don't have that type of coffee. Would you like something else?")

def generate_response(text):
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)

    for word, tag in tagged:
        if word in ["espresso", "latte", "cappuccino", "americano"]:
            make_coffee(word)
            return "Your coffee is being made. Enjoy!"
        elif word in ["no", "nope", "not", "don't"]:
            return "Okay, let me know if you change your mind."
        else:
            return "I'm sorry, I didn't understand. Can you please specify which coffee you would like?"

def chat_with_customer():
    engine = pyttsx3.init()
    engine.say("Hello, welcome to the AI coffee machine. How can I help you today?")
    engine.runAndWait()

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        audio = recognizer.listen(source)

    customer_response = recognizer.recognize_google(audio).lower()
    response = generate_response(customer_response)

    engine.say(response)
    engine.runAndWait()
    print(response)

if __name__ == "__main__":
    chat_with_customer()
