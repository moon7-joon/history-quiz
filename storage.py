import json
from pathlib import Path

from quiz import Quiz
from quiz_data import create_default_quizzes


STATE_PATH = Path(__file__).resolve().parent / "state.json"


def save_state(quizzes, best_score):
    data = {
        "quizzes": [quiz.to_dict() for quiz in quizzes],
        "best_score": best_score
    }

    try:
        with STATE_PATH.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError:
        print("파일을 저장하지 못했습니다.")
        return False

    return True


def load_state():
    try:
        with STATE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError

        items = data["quizzes"]
        best_score = data["best_score"]

        if not isinstance(items, list):
            raise ValueError

        if best_score is not None:
            if type(best_score) is not int or not 0 <= best_score <= 100:
                raise ValueError

        quizzes = []

        for item in items:
            if not isinstance(item, dict):
                raise ValueError

            question = item["question"]
            choices = item["choices"]
            answer = item["answer"]

            if not isinstance(question, str) or not question.strip():
                raise ValueError

            if not isinstance(choices, list) or len(choices) != 4:
                raise ValueError

            if any(not isinstance(c, str) or not c.strip() for c in choices):
                raise ValueError

            if type(answer) is not int or not 1 <= answer <= 4:
                raise ValueError

            quizzes.append(Quiz(question, choices, answer))

        return quizzes, best_score

    except FileNotFoundError:
        print("저장 파일이 없어 기본 문제로 시작합니다.")
    except (ValueError, KeyError, TypeError, UnicodeError):
        print("저장 파일 내용에 문제가 있어 기본 문제로 시작합니다.")
    except OSError:
        print("저장 파일을 읽지 못해 기본 문제로 시작합니다.")

    return create_default_quizzes(), None