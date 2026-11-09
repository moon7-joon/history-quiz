print("역사 탐험 퀴즈에 오신 것을 환영합니다!")
print()
print("1. 역사 퀴즈 풀기")
print("2. 새로운 문제 추가하기")
print("3. 문제 목록 보기")
print("4. 최고 점수 보기")
print("5. 게임 끝내기")
choice = input("번호를 선택하세요: ")
if choice == "1":
    print("역사 퀴즈를 시작합니다!")
elif choice == "2":
    print("새로운 문제를 추가합니다.")
elif choice == "3":
    print("문제 목록을 보여줍니다.")
elif choice == "4":
    print("최고 점수를 보여줍니다.")
elif choice == "5":
    print("게임을 끝냅니다.")
else:
    print("1~5 사이의 번호를 입력해 주세요.")