from quiz import Quiz
from storage import load_state, save_state


class QuizGame:
    def __init__(self, quizzes=None):
        if quizzes is None:
            self.quizzes, self.best_score = load_state()
        else:
            self.quizzes = quizzes
            self.best_score = None

    def save(self):
        return save_state(self.quizzes, self.best_score)

    def show_menu(self):
        print()
        print("1. 역사 퀴즈 풀기")
        print("2. 새로운 문제 추가하기")
        print("3. 문제 목록 보기")
        print("4. 최고 점수 보기")
        print("5. 게임 끝내기")

    def run(self):
        print("역사 탐험 퀴즈에 오신 것을 환영합니다!")
        print(f"불러온 퀴즈: {len(self.quizzes)}개")

        try:
            while True:
                self.show_menu()
                choice = self.read_number("번호를 선택하세요: ", 1, 5)

                if choice == 1:
                    self.play()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_list()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    print("게임을 끝냅니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 종료합니다.")

        finally:
            if self.save():
                print("게임 데이터를 저장했습니다.")

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

        self.save()

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

        if self.save():
            print("퀴즈가 추가되었습니다!")
        else:
            print("퀴즈는 추가됐지만 파일 저장에 실패했습니다.")