print("Welcome to THE ULTIMATE QUIZ")

name = input("Enter Your Name: ")

questions = [
  {"ques": "If a chicken crosses the road, what’s it doing?", "options": ["Going to KFC job interview", "Beating GTA mission", "Just crossing the road", "Escaping tax fraud"], "answer": "Just crossing the road"},
{"ques": "Why do people wear shoes?", "options": ["To flex on rocks", "To hide ugly socks", "Because carpets aren’t everywhere", "To run from responsibilities"], "answer": "To flex on rocks"},
{"ques": "What do you call a fish with no eyes?", "options": ["Fsh", "Blind Nemo", "Wi-Fi signal", "Shark with student loans"], "answer": "Fsh"},
{"ques": "Why do we eat food?", "options": ["To survive", "Because chewing is a hobby", "Free serotonin", "To annoy gym trainers"], "answer": "To survive"},
{"ques": "What happens if you sleep in class?", "options": ["Teacher wakes you up", "You unlock dream DLC", "Auto GPA reduction", "You time travel to lunch break"], "answer": "Teacher wakes you up"},
{"ques": "Why do humans blink?", "options": ["To clean eyes", "To refresh browser", "To skip boring moments", "To avoid staring contests with walls"], "answer": "To clean eyes"},
{"ques": "If Wi-Fi stops working, what do we call it?", "options": ["Depression", "Free therapy", "Real life", "Offline boss battle"], "answer": "Depression"},
{"ques": "Why do people brush their teeth?", "options": ["To avoid cavities", "To scare toothpaste ads", "So dentists don’t bully them", "To roleplay as Colgate model"], "answer": "To avoid cavities"},
{"ques": "What do you get if you boil water?", "options": ["Steam", "Tea upgrade", "Cloud in your kitchen", "Free sauna"], "answer": "Steam"},
{"ques": "If you put your phone on airplane mode, what does it do?", "options": ["Nothing", "Flies to Dubai", "Turns into pilot", "Starts speaking Arabic"], "answer": "Nothing"}
]

score = 0

for num, x in enumerate(questions, start=1):
  print(f"Question no {num}: {x["ques"]}")
  for i, option in enumerate(x["options"], start=1):
    print(f"{i}. {option}")
  ans = int(input("Answer: "))

  if x["answer"] == x["options"][ans - 1]:
    score = score + 1
    print(f"Answer is Correct.\nScore = {score}")
  else:
    print(f"Answer is not Correct. Correct Answer is: {x["answer"]}")
  