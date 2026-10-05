import hashlib
import json
import sys
from pathlib import Path

data = json.loads(sys.stdin.buffer.read().decode("utf-8").lstrip("\ufeff"))
project = Path(data.get("cwd", ".")).resolve()
orders = sorted((project / "orders").glob("order_v*.md"))

def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
        "permissionDecision": "deny", "permissionDecisionReason": reason}}, ensure_ascii=False))
    sys.exit(0)

if not orders:
    deny("프롬프트 파일이 없습니다. 영상을 생성하기 전에 프롬프트 파일부터 만드세요.")
order = orders[-1]
digest = hashlib.sha256(order.read_bytes()).hexdigest().lower()
ok = project / "approvals" / (order.name + ".approved")
if not ok.exists():
    deny(f"{order.name} 의 승인 기록이 없습니다. 사람이 프롬프트 파일을 읽고 approvals 폴더에 승인 기록을 남겨야 생성할 수 있습니다.")
if digest not in ok.read_text(encoding="utf-8-sig", errors="ignore").lower():
    deny(f"{order.name} 이 승인한 뒤에 바뀌었습니다. 바뀐 프롬프트 파일을 다시 읽고 다시 승인하세요.")
sys.exit(0)
