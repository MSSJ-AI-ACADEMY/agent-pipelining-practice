import json
import subprocess
import sys
from pathlib import Path

data = json.loads(sys.stdin.buffer.read().decode("utf-8").lstrip("\ufeff"))
file_path = data.get("tool_input", {}).get("file_path", "")
project = Path(data.get("cwd", ".")).resolve()
if not file_path:
    sys.exit(0)
target = Path(file_path)
if not target.is_absolute():
    target = project / target
try:
    rel = target.resolve().relative_to(project)
except ValueError:
    sys.exit(0)
if not (rel.parts and rel.parts[0] == "orders"):
    sys.exit(0)
out = subprocess.run([sys.executable, str(project / ".claude/skills/video-order/scripts/order_check.py")],
                     cwd=project, capture_output=True, text=True, encoding="utf-8").stdout.strip()
if "문제 없음" not in out:
    print("프롬프트 파일 검사에 걸렸습니다: " + out, file=sys.stderr)
    sys.exit(2)
sys.exit(0)
