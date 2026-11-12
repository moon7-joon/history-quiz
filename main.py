from quiz_game import QuizGame
from storage import load_state, save_state


quizzes, best_score = load_state()

game = QuizGame(quizzes)
game.best_score = best_score

print("역사 탐험 퀴즈에 오신 것을 환영합니다!")
print(f"불러온 퀴즈: {len(game.quizzes)}개")

try:
    while True:
        print()
        print("1. 역사 퀴즈 풀기")
        print("2. 새로운 문제 추가하기")
        print("3. 문제 목록 보기")
        print("4. 최고 점수 보기")
        print("5. 게임 끝내기")

        choice = input("번호를 선택하세요: ").strip()

        if choice == "1":
            game.play()
            save_state(game.quizzes, game.best_score)
        elif choice == "2":
            game.add_quiz()
            save_state(game.quizzes, game.best_score)
        elif choice == "3":
            game.show_list()
        elif choice == "4":
            game.show_score()
        elif choice == "5":
            print("게임을 끝냅니다.")
            break
        else:
            print("1~5 사이의 번호를 입력해 주세요.")

except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되어 게임을 종료합니다.")

finally:
    if save_state(game.quizzes, game.best_score):
        print("게임 데이터를 저장했습니다.")