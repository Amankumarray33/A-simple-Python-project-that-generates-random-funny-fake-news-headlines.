# 1- import the random module
import random
 # 2- create subjects
subjects = [
        "Aman",
        "Sneha",
        "Rahul",
        "Muskan",
        "A Mumbai cat",
        "A Group of Monkeys",
        "prime ministrer",
        "Auto Rekshwa Dirver from delih"
 ]
action = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "order",
    "celeberates"

]

places_or_things=[
    "at red fort",
    "in Mumbai Local Train",
    "Plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"

]

# 3 start the headline gereration loop
while True:
    subject = random.choice(subjects)
    action = random.choice(action)
    places_or_things = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {places_or_things}"
    print("\n" + headline)

    user_input = input("\nDo you want to generate another headline? (yes/no)").strip()
    if user_input == "no":
        break
    print("\nThanks for using the Fake News Generator. Have a great day!")



  