from quiz import Quiz


class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = None

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0

        for quiz in self.quizzes:
            quiz.display()
            answer = self.read_number("정답 번호(1~4): ", 1, 4)

            if quiz.check_answer(answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print("아쉽습니다. 정답 번호:", quiz.answer)

            print()

        score = round(correct_count / len(self.quizzes) * 100)

        print(f"결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답!")
        print(f"이번 점수: {score}점")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")

    def show_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
            return

        print(f"최고 점수: {self.best_score}점")

    def show_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈: 총 {len(self.quizzes)}개")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def read_text(self, prompt):
        while True:
            text = input(prompt).strip()

            if text:
                return text

            print("내용을 입력해 주세요.")

    def read_number(self, prompt, minimum, maximum):
        while True:
            text = input(prompt).strip()

            try:
                number = int(text)
            except ValueError:
                print(f"{minimum}~{maximum} 사이의 숫자를 입력해 주세요.")
                continue

            if minimum <= number <= maximum:
                return number

            print(f"{minimum}~{maximum} 사이의 숫자를 입력해 주세요.")

    def add_quiz(self):
        print("새로운 퀴즈를 추가합니다.")

        question = self.read_text("문제를 입력하세요: ")
        choices = []

        for number in range(1, 5):
            choice = self.read_text(f"선택지 {number}: ")
            choices.append(choice)

        answer = self.read_number("정답 번호(1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다!")