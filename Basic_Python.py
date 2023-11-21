from Questions import Question


question_prompts = [
    "Qual a cor do céu ?  \n(a) Azul \n(b) Verde \n(c) Rosa\nResposta:"
]

questions = [
    Question(question_prompts[0], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score = score + 1
        print("voce acertou "+str(score)+"/"+str(len(questions)))
run_test(questions)



