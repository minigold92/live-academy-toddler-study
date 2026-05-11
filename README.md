# 라이브 아카데미 토들러 학습 노트

[새벽1시의 영어교실 / 라이브 아카데미 토들러](https://youtube.com/playlist?list=PLEzsBdrpZXC8tdzAqQHEQ66TocGI-Kagh) 왕초보 영어회화 96편의 영상 자막을 기반으로 만든 학습 노트입니다.

🌐 **웹에서 보기**: https://minigold92.github.io/live-academy-toddler-study/

## 자료 구성

각 레슨(`docs/Lesson_NNN.md`)은 다음을 포함합니다.

- 🎯 오늘의 핵심 포인트
- ✨ 상황별 변환 테이블 (복습 vs 오늘 추가 🆕)
- 🧩 문맥으로 이어 말하기
- 🔑 변환/응용 패턴
- 📖 핵심 어휘 / 🗣️ 발음 팁 / 📝 파생 연습
- 🤖 AI와 함께 공부하기 — 4모드 프롬프트 (튜터/퀴즈/회화/응용)

## 로컬에서 보기

```bash
pip install mkdocs-material
mkdocs serve
# http://127.0.0.1:8000
```

## 자료 만들기 흐름

1. `yt-dlp`로 96개 영상 오디오 다운로드 (16kHz mono wav)
2. `mlx-whisper` (large-v3-turbo)로 한·영 혼합 음성 전사
3. 트랜스크립트 → 학습 자료 추출 (이 작업은 Claude로 진행)
4. YouTube 메타정보 (제목·길이·조회수) 자동 삽입
5. MkDocs Material로 정적 사이트 빌드 → GitHub Pages 배포

## 디렉토리

```
.
├── docs/                    # 96개 학습 자료 마크다운 (사이트 소스)
├── scripts/                 # 전사·메타 삽입·nav 생성 스크립트
├── SPEC.md                  # 자료 포맷 스펙
├── mkdocs.yml               # MkDocs 설정 (Material 테마, 한국어, 다크모드)
└── .github/workflows/       # GitHub Pages 자동 배포
```

## 출처 / 면책

- 영상 권리는 [원작자](https://www.youtube.com/@LiveAcademyToddler)에게 있습니다.
- 본 자료는 학습 보조 목적의 비상업적 정리물이며, 학습 후 원본 영상 시청을 권장합니다.
