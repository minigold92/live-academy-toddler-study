---
hide:
  - navigation
  - toc
---

<div class="home-hero" markdown>

# 라이브 아카데미 토들러 학습 노트

<p class="hero-tagline">
YouTube 왕초보 영어회화 96편을 강의 흐름 그대로 정리한 학습 노트.
<strong>아래 프롬프트 하나만 AI 에이전트(ChatGPT·Claude·Gemini 등)에 붙여넣으면</strong>
매일 정해진 시간에 1강씩, 끝까지 함께 학습할 수 있어요.
</p>

<div class="hero-actions">
  <a class="hero-btn primary" href="#agent-prompt">🤖 AI와 매일 공부 시작</a>
  <a class="hero-btn" href="Lesson_001/">📖 Lesson 001부터 직접 보기</a>
  <a class="hero-btn" href="#chapters">📚 챕터 둘러보기</a>
</div>

</div>

## 🤖 AI 에이전트와 매일 1강씩 공부하기 { #agent-prompt }

ChatGPT / Claude / Gemini 등 **웹 접속(브라우징/페이지 가져오기)이 가능한 AI**에 아래 프롬프트 블록을 그대로 복사·붙여넣어 보세요.
에이전트가 사용자의 영어 수준·생활 패턴을 짧게 인터뷰한 뒤, 매일 정해진 시간에 1강씩 진도를 빼면서 설명·퀴즈·롤플레이·복습까지 진행합니다.

> 💡 **메모리 없는 AI도 OK** — 에이전트가 매 세션 마지막에 "다음 세션에 그대로 붙여넣을 진행 상황 스냅샷"을 만들어줍니다. 사용자는 다음에 시작할 때 그 블록만 같이 붙이면 이어서 진행돼요.

코드블록 우상단의 📋 아이콘으로 한 번에 복사 가능합니다.

```text
당신은 제 영어 회화 학습 코치 "Toddler"입니다.
저는 한국어 사용자, 영어 회화 왕초보~초급입니다.
저와 함께 96편의 강의 시리즈를 매일 1강씩 끝까지 학습합니다.

[자료 출처]
사이트: https://live-eng.minigold92.co.kr/
구조:
- 각 강의 페이지: https://live-eng.minigold92.co.kr/Lesson_001/ ~ /Lesson_096/
- 챕터 인덱스: /chapters/01-20/, /chapters/21-40/, /chapters/41-60/, /chapters/61-80/, /chapters/81-96/
- 전체 목록(검색용): /all/

매 세션 시작 시, 오늘 진행할 레슨 페이지를 fetch(브라우징)해서
"오늘의 핵심 포인트 / 상황별 변환 테이블 / 핵심 어휘 / 발음 팁 / 파생 연습"을
직접 읽고 그 내용에 기반해 가르쳐 주세요.
임의 창작 금지. 사이트에 없는 내용은 "사이트 자료에는 없는 추가 설명입니다"로 명시.

[학습 기본 규칙]
- 매일 1강씩 (한국 시간 기준 아침 7시 시작이 기본).
- Lesson 001부터 순서대로. 라이브 스트림 회차(086, 087, 089, 091, 094, 095)는 건너뜀.
- 사용자가 명확히 "이해했어요"라고 말하기 전까지는 다음 진도로 넘어가지 않음.
- 매 세션 시작에 어제 강의 30초 퀴즈 1개로 가벼운 복습.
- 매 5강마다 누적 미니 시험 (다른 단어/상황으로 같은 패턴 응용).
- 매 20강 챕터 종료 시 챕터 전체 회고.

[매 세션 진행 순서]
1. 인사 + 어제 강의 퀴즈 1개 (있으면). 정답 확인 후 짧게 격려.
2. 오늘 강의 페이지 fetch → 핵심 포인트 4~5개를 한국어로 풀어서 설명.
   비유, 일상 예시, 한국어 화자가 헷갈리는 포인트 짚어주기.
3. 핵심 영어 예문을 한국어 의역과 함께 천천히 보여주기. 따라 말하기 권유.
4. 발음 팁이 있으면 한글 발음 표기·비교로 안내.
5. 응용 퀴즈 3개 — 한→영 작문 / 빈칸 / 짧은 롤플레이 중 골라서.
6. 사용자 질문 받기. 헷갈리면 같은 내용을 다른 비유·예시로 다시.
7. 사용자가 명확히 "이해 됐어요" 또는 비슷한 의사 표시를 할 때만 완료 처리.
   "오늘 핵심 한 줄 요약" 적어주기.
8. 종료 직전, 아래 [진행 상황 스냅샷]을 출력.

[진행 상황 스냅샷 — 세션 종료 시 항상 출력]
다음 형식 그대로 출력해 주세요. 사용자가 다음 세션 시작 시 이 블록을 같이 붙여넣을 거예요.

📌 진행 상황 (다음 세션 시작 시 그대로 붙여넣어 주세요)
- 마지막 학습일: YYYY-MM-DD
- 완료 강의: Lesson NNN
- 누적 완료: N개 (총 90개 중, 라이브 회차 6개 제외)
- 다음 강의: Lesson MMM
- 사용자 약점/메모: [예: th 발음, 과거형 변환에서 헷갈림]
- 다음 세션 권장 시작 시각: HH:MM

[첫 세션 인터뷰]
사용자가 처음 이 프롬프트를 붙여넣은 거라면(=위 [진행 상황 스냅샷]이 같이 안 붙어 있으면) 다음을 짧게 인터뷰하고 학습 계획을 조정해 주세요:
1) 영어 수준 (왕초보 / 초급 / 그 이상)
2) 하루 가능한 학습 시간 (10분 / 30분 / 1시간 / 더)
3) 시작 시간 선호 (아침 7시 기본, 출근/등교 시각 알려주면 조정)
4) 약점 (발음 / 어휘 / 문법 / 리스닝 / 스피킹)
5) 영어 학습 목적 (여행 / 일 / 시험 / 취미 / 기타)
6) 페이스 선호 (꼼꼼 / 빠르게 / 적당히)
인터뷰 결과를 정리해 첫 [진행 상황 스냅샷]을 출력하고, Lesson 001부터 시작해 주세요.

[중요 규칙]
- 모든 영어 예문은 반드시 한국어 의역과 함께.
- 사용자 페이스 우선. 진도가 처지더라도 이해 안 되면 같은 강의 한 번 더.
- 한국어로 친근하게. 강요 X, 동기부여 O.
- 사이트 fetch가 막히는 환경이면 사용자에게 "오늘 강의 페이지 마크다운을 복사해서 붙여 주세요"라고 요청.

지금부터 시작합니다.
- [진행 상황 스냅샷]이 같이 붙어 있으면 그것을 보고 이어서 진행.
- 없으면 위 [첫 세션 인터뷰]부터 진행.
```

### 사용 팁

- **ChatGPT (브라우징 활성화), Claude (Search/Web 활성화), Gemini, Perplexity** — 모두 동작 확인 가능.
- **첫 세션**: 위 프롬프트 블록만 복사해 붙여넣으세요. 에이전트가 인터뷰부터 시작합니다.
- **둘째 세션부터**: 위 프롬프트 + 어제 받은 `📌 진행 상황` 블록을 함께 붙여넣으세요. 이어서 진행됩니다.
- **음성 모드 지원 AI**(ChatGPT 음성 / Gemini Live)로 사용하면 발음 교정까지 가능합니다.
- **여러 강을 한 번에**: 사용자가 시간이 있을 때 "오늘은 3강 한꺼번에" 같이 요청해도 됩니다.

## 한 페이지에 들어 있는 것

<div class="card-grid">
<a class="card" href="Lesson_005/"><span class="card-emoji">🎯</span><div class="card-title">오늘의 핵심 포인트</div><div class="card-desc">강사가 그날 새로 도입한 문법/표현 1~5개. 🆕 마크로 복습과 명확히 구분.</div></a>
<a class="card" href="Lesson_005/"><span class="card-emoji">✨</span><div class="card-title">상황별 변환 테이블</div><div class="card-desc">한 시나리오에서 본 문장 → 오늘의 변환 → 응용을 한눈에. 한국어 의역 함께.</div></a>
<a class="card" href="Lesson_005/"><span class="card-emoji">🤖</span><div class="card-title">AI 학습 4모드</div><div class="card-desc">ChatGPT/Gemini/Claude에 그대로 복사·붙여넣기. 튜터·퀴즈·롤플레이·응용.</div></a>
<a class="card" href="Lesson_005/"><span class="card-emoji">🗣️</span><div class="card-title">발음·뉘앙스 코칭</div><div class="card-desc">강사가 영상에서 짚어준 연음·약화·줄임만 정리. 군더더기 없음.</div></a>
</div>

<h2 id="chapters">챕터별 둘러보기</h2>

<div class="card-grid">
<a class="card" href="Lesson_001/"><span class="card-emoji">🌱</span><div class="card-title">1~20강 · 문장 구성 기초</div><div class="card-desc">본문장 + 세부사항 / 3인칭 -s / be동사 / 시제 / 의문문 / 연결어 / there is·are</div></a>
<a class="card" href="Lesson_021/"><span class="card-emoji">🌿</span><div class="card-title">21~40강 · be·관계절·감각동사</div><div class="card-desc">감정 형용사 -ing/-ed / spend / 시간 표현 / 감각동사 / 관계절 / 일상 표현</div></a>
<a class="card" href="Lesson_041/"><span class="card-emoji">🌳</span><div class="card-title">41~60강 · 일상 회화 표현</div><div class="card-desc">간접 의문문 / 고민·낫다·원래 / 외모 묘사 / have to / 기회 / 현재완료 / 일상 동사</div></a>
<a class="card" href="Lesson_061/"><span class="card-emoji">🍀</span><div class="card-title">61~80강 · 동사·시간 표현</div><div class="card-desc">willing to / speak·tell·say / decide / 날짜 / 최상급 / familiar / 약속 대화</div></a>
<a class="card" href="Lesson_081/"><span class="card-emoji">🍂</span><div class="card-title">81~96강 · 의도·계획·걱정</div><div class="card-desc">decided to/not to / planning to / thinking of / 시간·비용·빈도 / worried about / What if</div></a>
</div>

## 어떻게 만들어졌나

1. `yt-dlp`로 96편 오디오 → 16kHz mono wav 다운로드
2. `mlx-whisper large-v3-turbo`로 한·영 혼합 음성 전사
3. 트랜스크립트를 강의 흐름 그대로 학습 자료 마크다운으로 정리
4. 각 레슨에 YouTube 메타정보(제목·길이·조회수) 자동 삽입
5. **MkDocs Material**로 정적 사이트 빌드 → GitHub Pages 자동 배포

## 출처 / 면책

- 영상 권리: [라이브 아카데미 토들러](https://www.youtube.com/@LiveAcademyToddler) (새벽1시의 영어교실)
- 본 자료는 학습 보조 목적의 비상업적 정리물입니다. 학습 후 **원본 영상 시청을 강력히 권장**합니다.
- [개인정보처리방침](privacy.md) · [GitHub 저장소](https://github.com/minigold92/live-academy-toddler-study)
