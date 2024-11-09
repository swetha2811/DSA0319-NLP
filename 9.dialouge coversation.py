conversation = [
    "Good morning! How's the weather today?",
    "I heard it's going to be sunny and warm.",
    "Could you please send me the report by 3 PM?",
    "Of course, I'll send it over before the deadline.",
    "Do you know where the nearest post office is?",
    "The post office is two blocks down the street."
]

for utterance in conversation:
    if utterance.endswith('?'):
        print(f"Question: {utterance}")
    elif utterance.endswith('.'):
        print(f"Statement: {utterance}")
    elif utterance.endswith('!'):
        print(f"Exclamation: {utterance}")
    else:
        print(f"Other: {utterance}")
