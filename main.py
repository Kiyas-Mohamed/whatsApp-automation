import pyautogui
import time
# import random

wordArrays = [
    "Welcome Back to our (ZINA) hub",
    "எங்கள் (ZINA) மையத்திற்கு மீண்டும் வரவேற்கிறோம்",
    "අපගේ (ZINA) මධ්‍යස්ථානය වෙත නැවත සාදරයෙන් පිළිගනිමු",
]

# emojiArrays = [":)", ":(", ";)", ":p", "8-)", ":(", ":-/", "<3"]

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# number = "0123456789"
# symbol = "!@#$%&"

count = 1
while count <= 99:

    # useForAll = lower + upper + number + symbol
    # length = 12
    # temp = random.sample(useForAll, length)
    # answer = "".join(temp)

    for word in wordArrays:

        pyautogui.typewrite(f"{count}. {word}")
        pyautogui.press("enter")
        time.sleep(0.3)
        count += 1
