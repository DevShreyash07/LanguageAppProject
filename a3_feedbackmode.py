import random

# response modes
MODE = ["normal", "motivational", "savage"]

# predefined responses for each mode
RESPONSES = {
    "correct": {
        "normal": "Correct! 👍",
        "motivational": [
            "Great job! You got it right! ✨"
            "Ayy there we go! You're on fire today 🔥"
            "Correct! Keep stacking those Ws, champ 💪"
            "Boom. That's the grind paying off. ✨"
            "That's what I call brain gains 🧠🏋️"
            "Knew you'd nail it — consistency always wins.",
        ],
        "savage": [
            "If it was wrong you would have owed me money! 😎"
            "Oh wow, a correct answer? Miracles *do* happen! 😏",
            "You got it right? Who hacked your brain, genius? 🧠💀",
            "Correct. I was ready to roast you, but you escaped… this time. 😎"
        ],
    },
    "incorrect": {
        "normal": "Incorrect. Try again. ❌",
        "motivational": [
            "Don't give up! You can do it! 💪",
            "Nah, not this time. But legends miss too before they master. ⚔️",
            "Close one! Don't overthink — trust your gut next time. 🔮"
            "You fell? Cool. Now rise — that's what separates quitters from kings. 👑"
            "Hey, fail fast, learn faster — that's the whole game. 🧩"
            "Okay, you missed — now prove to me it was a fluke. 😎"
        ],         
        "savage": [
            "Wrong, I guess you need to rethink your life choices. 😂"
            "Bro… even auto-correct would've done better. 😂",
            "Wrong. Were you blindfolded while answering? 😭",
            "Incorrect. But hey, at least you’re consistent. 😌",
            "That was so wrong I think my code cried. 💀"
        ],
    },
}
