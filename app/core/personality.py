import random
from datetime import datetime

GREETINGS = [
    "Boss, kya chal raha hai? 😄",
    "Abhay bhai, coding mode me ho kya? 🔥",
    "Oho boss aa gaye 😎 Main ready hoon!",
    "Kya haal hai boss? Aaj kya banane wale ho? 🚀",
    "Boss, aaj AI ki duniya hila dete hain 😁"
]

IDLE_RESPONSES = [
    "Boss, chup-chaap baithe ho... koi naya idea pak raha hai kya? 😏",
    "Coffee break chal raha hai ya deep thinking? ☕",
    "Main yahin hoon boss, bas ek command bolo 😄",
    "Aap soch rahe ho aur main ready hoon 🚀"
]

JOKES = [
    "Boss, programmers andhere me kyun kaam karte hain? Kyunki bugs light se darte nahi 😂",
    "Aaj ka motivation: semicolon bhoolna mana hai 😅",
    "Coding ka asli dard tab hota hai jab bug khud hi gayab ho jaye 😭😂"
]

def random_greeting():
    return random.choice(GREETINGS)

def idle_message():
    return random.choice(IDLE_RESPONSES)

def random_joke():
    return random.choice(JOKES)

def time_based_greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good morning boss 🌞 Aaj ka mission kya hai?"
    elif hour < 18:
        return "Good afternoon boss 😎 Kaam ka kya scene hai?"
    else:
        return "Good evening boss 🌙 Coding continue karein ya thoda relax karein?"