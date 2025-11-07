import random

# response modes
MODE = ["normal", "motivational", "savage"]

# predefined responses for each mode
RESPONSES = {
    "questions_feedback": {
        "correct answer": {
            "normal": ["Correct! 👍"],
            "motivational": [
                "Great job! You got it right! ✨",
                "Ayy there we go! You're on fire today 🔥",
                "Correct! Keep stacking those Ws, champ 💪",
                "Boom. That's the grind paying off. ✨",
                "That's what I call brain gains 🧠🏋️",
                "Knew you'd nail it — consistency always wins.",
            ],
            "savage": [
                "If it was wrong you would have owed me money! 😎",
                "Oh wow, a correct answer? Miracles *do* happen! 😏",
                "You got it right? Who hacked your brain, genius? 🧠💀",
                "Correct. I was ready to roast you, but you escaped… this time. 😎",
            ],
        },
        "incorrect answer": {
            "normal": ["Incorrect. Try again. ❌"],
            "motivational": [
                "Don't give up! You can do it! 💪",
                "Nah, not this time. But legends miss too before they master. ⚔️",
                "Close one! Don't overthink — trust your gut next time. 🔮",
                "You fell? Cool. Now rise — that's what separates quitters from kings. 👑",
                "Hey, fail fast, learn faster — that's the whole game. 🧩",
                "Okay, you missed — now prove to me it was a fluke. 😎",
            ],         
            "savage": [
                "Wrong, I guess you need to rethink your life choices. 😂",
                "Bro… even auto-correct would've done better. 😂",
                "Wrong. Were you blindfolded while answering? 😭",
                "Incorrect. But hey, at least you are consistent. Unlike Shreyash who wrote this code!😌",
                "That was so wrong I think my code cried. 💀",
            ],
        },
        "incorrect option": {
            "normal": [
                "Nice work! You cleared this quiz. ✅",
                "Clean sweep — quiz passed.",
                "Correct answers all the way. You’re on track.",
                "Good job, keep it consistent.",
                "You're learning fast. Onward to the next one.",
            ],
            "motivational": [
                "That’s what I’m talking about! You just owned that quiz! 🔥",
                "Quiz? More like warm-up for a legend. 💪",
                "You didn’t just pass — you proved you’re built for this.",
                "Momentum’s yours now. Keep crushing it.",
                "You turned effort into results. Proud of you. ✨",
            ],
            "savage": [
                "Ayy, you passed. Miracles do happen, huh? 😏",
                "You actually made it? Damn, I might start believing in you. 💀",
                "Well, look who decided to use their brain today.",
                "That quiz didn’t stand a chance against your chaotic genius.",
                "You passed. Don’t get cocky — I saw you guessing. 👀",
            ],
        },
    },

    "quiz_feedback": {
        "passed": {
            "normal": [
                "Nice work! You cleared this quiz. ✅",
                "Clean sweep — quiz passed.",
                "Correct answers all the way. You’re on track.",
                "Good job, keep it consistent.",
                "You're learning fast. Onward to the next one.",
            ],
            "motivational": [
               "That's what I'm talking about! You just owned that quiz! 🔥",
               "Quiz? More like warm-up for a legend. 💪",
               "You didn't just pass — you proved you're built for this.",
               "Momentum's yours now. Keep crushing it.",
               "You turned effort into results. Proud of you. ✨",
            ],
            "savage": [
                "Ayy, you passed. Miracles do happen, huh? 😏",
                "You actually made it? Damn, I might start believing in you. 💀",
                "Well, look who decided to use their brain today.",
                "That quiz didn't stand a chance against your chaotic genius.",
                "You passed. Don't get cocky — I saw you guessing. 👀",
            ],
        }, 
        "failed": { 
            "normal": [
                "That didn't go as planned. Try again.",
                "Quiz failed. Review your notes and retry.",
                "Close call — but not quite there yet.",
                "You missed a few, let's fix that next round.",
                "No worries, just means more practice time.",
            ],
            "motivational": [
                "Hey, no one nails it the first time. Reset and rise. 💪",
                "Failure's just data. Adjust, reload, and dominate. 🔥",
                "Falling's fine — staying down isn't. You've got this.",
                "Even the greats miss sometimes. Try again, legend.",
                "You're not losing, you're learning. Keep grinding. ⚡",
            ],
            "savage": [
                "Bruh… did you even read the question? 💀",
                "That quiz just folded you like cheap origami.",
                "Wrong answers everywhere. You speedran failure. 🏃‍♂️💨",
                "If ignorance was a sport, you'd be national champ. 😂",
                "I'd roast you harder, but clearly life's already doing it. 🔥",
            ],
        },
    },

    "lesson_feedback": {
        "passed": {
            "normal": [
                "Lesson completed. Progress saved.",
                "Good work — you've mastered this lesson.",
                "Solid grasp on this topic. Keep it up.",
                "You finished strong. On to the next challenge.",
                "Lesson passed. You're getting better with each one.",
            ],
            "motivational": [
                "Lesson complete! You're literally evolving out here. 🚀",
                "Another milestone down. You're unstoppable, champ.",
                "You’re not learning anymore — you're transforming. 💫",
                "Discipline beats talent, and you've got both.",
                "That’s how legends grow — one lesson at a time.",
            ],
            "savage": [
                "Lesson passed? Oh so you do have a brain cell or two left. 😜",
                "Well, you didn't embarrass yourself this time. Impressive.",
                "You passed the lesson — I'm as shocked as your neurons.",
                "Not bad, Einstein. Maybe you can read after all.",
                "You aced it? Damn, I'll call NASA — a new species is emerging. 👽",
            ],
        },
        "failed": {
            "normal": [
                "Lesson incomplete. Try again when ready.",
                "Not enough correct answers to pass this lesson.",
                "Progress saved, but you'll need another round.",
                "Lesson failed. Review and retry.",
                "You're close — a few more right answers will do it.",
            ],
            "motivational": [
                "Alright, this one beat you. So what? You'll beat it back. 🔥",
                "Every failure's a setup for a stronger comeback.",
                "You're building resilience right now — that's growth. 💪",
                "Legends aren't born — they retry.",
                "You didn't fail, you just discovered how not to pass it yet.",
            ],
            "savage": [
                "Lesson failed. Guess Netflix is proud of you. 📺",
                "That was so bad even autocorrect couldn't save you.",
                "Bro… even my error handler gave up. 💀",
                "You flunked the whole lesson. I'm adding that to your legacy.",
                "That wasn't learning, that was performance art. 😭",
            ],
        },
    },
}
