class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0

        for quiz in self.quizzes:
            quiz.display()

            while True:
                text = input("정답 번호(1~4): ").strip()

                try:
                    answer = int(text)
                except ValueError:
                    print("1~4 사이의 숫자를 입력해 주세요.")
                    continue

                if 1 <= answer <= 4:
                    break

                print("1~4 사이의 숫자를 입력해 주세요.")

            if quiz.check_answer(answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print("아쉽습니다. 정답 번호:", quiz.answer)

            print()

        print(f"결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답!")