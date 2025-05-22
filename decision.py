print("Hello, how are you feeling today? (happy / tired / bored / stressed)")
mood = input("Your mood: ").lower()

if mood == "happy":
    print("That's great! Keep it up!")
elif mood == "tired":
    print("You should take some rest.")
elif mood == "bored":
    print("Try learning something new or go for a walk.")
elif mood == "stressed":
    print("Take a deep breath and give yourself a short break.")
else:
    print("I hope your day gets better!")

print("Thank you for chatting. Goodbye!")
