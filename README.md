# 《에이전트 파이프라이닝》 실습편 꾸러미

책 실습편에서 **통째로 붙여 넣는 긴 파일**을 모아 둔 곳입니다. 책을 보며 한 글자씩 치지 않고, 이 파일을 내 작업 폴더로 복사해 쓰면 됩니다.

책 지면에도 같은 글이 그대로 실려 있습니다. 읽고 이해하는 것은 책으로, 붙여 넣는 수고는 이 꾸러미로 줄이는 셈입니다.

## 1. 들어 있는 것

| 폴더 | 실습 | 파일 | 하는 일 |
|---|---|---|---|
| `practice02` | 실습 2 첫 일 맡기기 | `brief/shop.md` | 가게 소개 파일 |
| `practice02` | 실습 2 | `.claude/settings.json` | 첫 설정 파일(허락 규칙) |
| `practice03` | 실습 3 광고 팀 규칙 | `CLAUDE.md` | 광고 팀 규칙 파일 |
| `practice05` | 실습 5 영상 프롬프트 스킬 | `.claude/skills/video-order/SKILL.md` | 스킬 설명서 |
| `practice05` | 실습 5 | `.claude/skills/video-order/scripts/order_check.py` | 프롬프트 파일 검사 프로그램 |
| `practice07` | 실습 7 담당 나누기 | `.claude/agents/planner.md` | 기획 담당 파일 |
| `practice07` | 실습 7 | `brief/criteria.md` | 안을 고르는 기준 파일 |
| `practice08` | 실습 8 훅으로 검사 | `.claude/hooks/check_order.py` | 저장하면 도는 검사 훅 |
| `practice08` | 실습 8 | `.claude/hooks/need_approval.py` | 승인 없으면 생성을 막는 훅 |
| `practice10` | 실습 10 광고 체인 | `chain/chain_test.py` | 합격 테스트(실습 10 부록 전문) |

- 폴더 안의 경로는 작업 폴더 안의 경로와 같습니다. `practice05/.claude/skills/...` 는 작업 폴더의 `.claude/skills/...` 자리로 갑니다.
- `.claude/settings.json` 에 몇 줄을 끼워 넣는 단계(실습 6, 8)는 꾸러미에 넣지 않았습니다. 책의 단계대로 직접 넣습니다.
- `MANIFEST.json` 에는 파일마다 책 원고의 어느 줄에서 왔는지와 지문(SHA-256)이 적혀 있습니다.

## 2. 받는 법

**① 압축 파일로 받기 (처음이라면 이쪽)**

1. 이 페이지 위쪽의 초록색 **Code** 버튼을 누릅니다.
2. 맨 아래 **Download ZIP** 을 누릅니다.
3. 받은 파일의 압축을 풉니다.

**② git 으로 받기**

```text
git clone https://github.com/MSSJ-AI-ACADEMY/agent-pipelining-practice.git
```

## 3. 쓰는 법

책의 작업 폴더는 실습 1에서 만든 `ad-team` 입니다. 꾸러미의 파일을 그 폴더의 같은 자리로 복사합니다.

**직접 복사하기**: 탐색기에서 꾸러미 폴더를 열고, 그 실습의 파일을 `ad-team` 의 같은 경로로 복사합니다.

**맡기기**: 꾸러미를 받은 폴더 위치를 알려 주고 클로드 코드에게 이렇게 보냅니다.

```text
꾸러미의 practice03/CLAUDE.md 를 지금 작업 폴더의 CLAUDE.md 로 복사해 줘. 이미 같은 이름의 파일이 있으면 덮어쓰지 말고 먼저 알려 줘.
```

복사한 뒤에는 책의 확인 단계를 그대로 따라 합니다. 파일을 받았다고 끝이 아니라, 열어서 책과 같은지 보는 것까지가 한 단계입니다.

## 4. 준비물

윈도우 PC, 클로드 유료 요금제(Pro 이상), 실습 1에서 설치한 클로드 코드. 파이썬 파일(검사 프로그램, 훅, 합격 테스트)을 돌리려면 파이썬도 필요합니다.

## 5. 라이선스

MIT. `LICENSE` 를 보세요.
