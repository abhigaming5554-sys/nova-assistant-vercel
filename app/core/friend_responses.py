import random

RESPONSES = {
    "tired": [
        "Bhai lagta hai kaafi der se kaam kar rahe ho 😅 thoda paani pee lo.",
        "Aaj kaafi load liya hai kya? 5 minute ka break le lo boss ☕"
    ],

    "bored": [
        "Chal bore mat ho 😎 ek naya AI feature bana dete hain.",
        "Bhai boredom ka best ilaaj hai kuch creative banana 🚀"
    ],

    "frustrated": [
        "Arre yaar 😅 error aaya hai to milke dekhte hain, tension mat lo.",
        "Relax bhai, har bug ki ek kamzori hoti hai 😎"
    ],

    "coding": [
        "Oho 😏 lagta hai aaj koi powerful feature banne wala hai.",
        "Coding mood on 🔥 batao kis project pe kaam chal raha hai?"
    ],

    "normal": [
        "Haan bhai bolo 😄",
        "Main sun rahi hoon boss 👀",
        "Batao kya scene hai 😎"
    ]
}

def get_response(mood):
    return random.choice(RESPONSES[mood])