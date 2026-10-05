# 광고 체인 합격 테스트 — 실습 10 에서 독자가 클로드 코드로 만든 chain/run.py 가 지켜야 할 약속을 잰다.
# 임시 폴더에 가짜 광고 팀을 차려 놓고 run.py 를 불러 본다. 진짜 작업 폴더는 건드리지 않는다.
# 사용: python chain/chain_test.py   · 마지막 줄 "합격 6/6" 이어야 한다
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RUN = Path(__file__).resolve().parent / "run.py"
STEPS = ["card", "order", "check", "approve", "video", "review"]


def sh(cwd, *args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")   # 윈도에서 자식 프로그램이 옛 한글 방식(CP949)으로 찍는 일을 막는다
    r = subprocess.run([sys.executable, str(RUN), *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    return r.returncode, ((r.stdout or "") + (r.stderr or ""))


def receipt(cwd, step):
    p = Path(cwd) / "chain" / "receipts" / f"{step}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def main():
    tmp = Path(tempfile.mkdtemp(prefix="adteam_test_"))
    ok = 0
    try:
        for d in ("cards", "orders", "approvals", "videos", "review", "chain"):
            (tmp / d).mkdir(parents=True, exist_ok=True)
        (tmp / "cards" / "card_v1.md").write_text("# 콘티 v1\n", encoding="utf-8")

        # 1. 앞 단계 실행 기록이 없으면 다음 단계를 거부한다
        code, out = sh(tmp, "done", "order", "--file", "orders/order_v1.md")
        r1 = code != 0 and receipt(tmp, "order") is None
        print("1 앞 단계 없이 건너뛰기 거부:", "통과" if r1 else "실패", out.strip()[:80]); ok += r1

        # 2. 단계를 마치면 실행 기록에 파일 지문(sha256)이 남는다
        code, out = sh(tmp, "done", "card", "--file", "cards/card_v1.md")
        rc = receipt(tmp, "card") or {}
        want = hashlib.sha256((tmp / "cards" / "card_v1.md").read_bytes()).hexdigest()
        r2 = code == 0 and rc.get("sha256") == want
        print("2 실행 기록에 지문:", "통과" if r2 else "실패"); ok += r2

        # 3. 실행 기록에 적힌 파일이 나중에 바뀌면 다음 단계를 거부한다
        (tmp / "orders" / "order_v1.md").write_text("# 영상 프롬프트 v1\n## Negative\nno text\n", encoding="utf-8")
        (tmp / "cards" / "card_v1.md").write_text("# 콘티 v1 (몰래 고침)\n", encoding="utf-8")
        code, out = sh(tmp, "done", "order", "--file", "orders/order_v1.md")
        r3 = code != 0
        print("3 앞 판이 바뀌면 거부:", "통과" if r3 else "실패", out.strip()[:80]); ok += r3
        (tmp / "cards" / "card_v1.md").write_text("# 콘티 v1\n", encoding="utf-8")

        # 4. 승인 단계는 approvals 의 승인 기록에 프롬프트 파일 지문이 있어야 마친다
        sh(tmp, "done", "order", "--file", "orders/order_v1.md")
        sh(tmp, "done", "check", "--file", "orders/order_v1.md")
        code, out = sh(tmp, "done", "approve", "--file", "orders/order_v1.md")
        no_ok = code != 0
        h = hashlib.sha256((tmp / "orders" / "order_v1.md").read_bytes()).hexdigest()
        (tmp / "approvals" / "order_v1.md.approved").write_text(h.upper() + " 승인\n", encoding="utf-8")
        code, out = sh(tmp, "done", "approve", "--file", "orders/order_v1.md")
        r4 = no_ok and code == 0
        print("4 승인 기록 없으면 거부 · 있으면 통과:", "통과" if r4 else "실패"); ok += r4

        # 5. 같은 단계를 두 번 마치려 하면 거부한다(돈 드는 일을 두 번 하지 않게)
        (tmp / "videos" / "ad_v1.mp4").write_bytes(b"fake video")
        sh(tmp, "done", "video", "--file", "videos/ad_v1.mp4")
        code, out = sh(tmp, "done", "video", "--file", "videos/ad_v1.mp4")
        r5 = code != 0
        print("5 같은 단계 두 번 거부:", "통과" if r5 else "실패"); ok += r5

        # 6. status 는 여섯 단계를 순서대로, 끝난 것과 남은 것을 보여 준다
        code, out = sh(tmp, "status")
        pos = [out.find(s) for s in STEPS]
        r6 = code == 0 and all(p >= 0 for p in pos) and pos == sorted(pos)
        print("6 status 순서대로:", "통과" if r6 else "실패"); ok += r6
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"합격 {ok}/6")
    sys.exit(0 if ok == 6 else 1)


if __name__ == "__main__":
    main()
