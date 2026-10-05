import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
orders = sorted(Path("orders").glob("order_v*.md"))
if not orders:
    print("프롬프트 파일이 아직 없습니다.")
    raise SystemExit(0)
text = orders[-1].read_text(encoding="utf-8-sig")
low = text.lower()
problems = []
if "## negative" not in low or not text.split("## Negative")[-1].split("##")[0].strip():
    problems.append("Negative 줄이 비었습니다")
for word in ("person", "people", "man", "woman", "face"):
    if f" {word}" in low and "## negative" in low and low.index(f" {word}") < low.index("## negative"):
        problems.append(f"장면 묘사에 사람 낱말 '{word}' 이 있습니다")
if "9:16" not in text:
    problems.append("화면 비율 9:16 이 없습니다")
print(orders[-1].name, "문제 없음" if not problems else " / ".join(problems))
