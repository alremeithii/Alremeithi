print("Hi, how are you feeling today? (happy / tired / bored / stressed)")
mood = input("Your mood: ").lower()

if mood == "happy":
    print("That's great! Keep doing what you're doing!")
elif mood == "tired":
    print("You should take a short nap or drink some water.")
elif mood == "bored":
    print("Try learning something new or going for a walk.")
elif mood == "stressed":
    print("Take a deep breath and give yourself a short break.")
else:
    print("I hope your day gets better!")

print("Thank you for chatting. Goodbye!")
