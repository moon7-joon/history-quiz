from pathlib import Path
from tempfile import TemporaryDirectory

import storage


original_path = storage.STATE_PATH

try:
    with TemporaryDirectory() as folder:
        storage.STATE_PATH = Path(folder) / "state.json"

        print("[1] 저장 파일이 없는 경우")
        quizzes, score = storage.load_state()
        assert len(quizzes) == 5 and score is None
        print("통과: 기본 문제 5개로 시작합니다.")

        print()
        print("[2] 저장 파일이 손상된 경우")
        storage.STATE_PATH.write_text(
            "잘못된 JSON 내용",
            encoding="utf-8"
        )

        quizzes, score = storage.load_state()
        assert len(quizzes) == 5 and score is None
        print("통과: 기본 문제 5개로 복구합니다.")

finally:
    storage.STATE_PATH = original_path