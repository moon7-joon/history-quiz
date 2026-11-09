from quiz import Quiz

my_quiz = Quiz(
    "구석기 사람들이 돌을 깨뜨려 만든 도구는?",
    ["빗살무늬토기", "주먹도끼", "청자", "금속활자"],
    2
)

print(my_quiz.question)
print(my_quiz.choices)
print("정답 번호:", my_quiz.answer)
print("2번을 고르면:", my_quiz.check_answer(2))
print("1번을 고르면:", my_quiz.check_answer(1))
my_quiz.display()