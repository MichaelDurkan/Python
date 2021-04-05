from question import question
# This imports the "question" class from the "question.py" file

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Green\n(b) Orange\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Blue\n(b) Red\n(c) Green\n\n"
]
# These are our question prompts

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
]
# These are our answers stored in a data type called questions. We can add as many questions as we want

def run_test(questions):
# This is the function to run the test with the list of question objects that we want to ask the user
    score = 0
    # Keeps the users score. This starts at 0
    for question in questions:
        answer = input(question.prompt)
        # This stores the user input
        if answer == question.answer:
            score +=1
            # If the users gets the question correct, 1 is added to the users score

    print("You scored " + str(score) + "/" +str(len(questions)) + " correct")

run_test(questions)
# This passes the "questions" data type into "run_test"

