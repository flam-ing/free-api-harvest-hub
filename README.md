# ⚡ Free API & Scraping Harvest Hub (Developer & AI Free Tier Auto-Provisioning Skill)

[![Organization](https://img.shields.io/badge/ORG-flam--ing-e61862?style=for-the-badge&logo=github&logoColor=white)](https://github.com/flam-ing)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Verified Services](https://img.shields.io/badge/Verified%20Services-36%EA%B0%9C%20%2B%20AI%20%ED%8B%B0%EC%96%B4-blue?style=for-the-badge)](https://github.com/flam-ing/free-api-harvest-hub)

> **36개 글로벌 개발자, 엣지 AI, 서버리스 GPU, 무인 스크래핑 & 오픈소스 데이터 허브의 무료 플랜(Free Tier) 자격 증명을 전자동·반자동으로 수집, 검증, 로테이션하는 실전 에이전트 스킬입니다.**
>
> 2026-11-23 기준, 아래 표의 일부 AI 항목은 상태가 바뀌었습니다. **삭제하지 않고** `⚠️`로 표시했습니다. 카드·전화 없이 **일/월 쿼터가 반복 충전**되는 AI 티어는 [§2-1](#21-반복-충전--카드-없음--전화-인증-없음-2026-11-23-검증)에 따로 정리했습니다. 가입 노하우는 `SKILL.md`를 보세요.

---

## 📚 0. 오픈소스 3대 성지 (Reference Repositories)

본 프로젝트는 오픈소스 커뮤니티의 검증된 3대 성지 리포지토리의 핵심 자원과 프레임워크를 기반으로 실전 자동화 파이프라인을 구축했습니다:

1. **[ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev)** (⭐ 143k+): 개발자를 위한 글로벌 클라우드/인프라/SaaS 무료 티어 총망라 디렉토리.
2. **[public-apis/public-apis](https://github.com/public-apis/public-apis)** (⭐ 499k+): 전 세계 무료 공공/개발자 API (금융, 날씨, 번역, 소셜, 암호화폐 등) 집대성 카탈로그.
3. **[d4vinci/Scrapling](https://github.com/d4vinci/Scrapling)** (⭐ 103k+): 셀렉터 자동 복구(Self-healing), 봇 방어 우회 Stealth Fetcher, MCP Server를 내장한 차세대 파이썬 스크래핑 엔진.

---

## 📱 1. 【모든 것의 시작】 스마트폰 '구글 앱'으로 전화번호 없이 무한 부계정 생성법

PC 브라우저에서 계정을 만들면 100% 확률로 전화번호 인증(SMS)을 요구하여 다계정 생성이 막힙니다.  
**반드시 스마트폰(iOS / Android)의 공식 "Google 앱"**을 통해 생성해야 전화번호 인증을 할 수 있습니다.



---

## 📊 2. 검증 완료된 36개 전체 서비스 무료 API & 인프라 풀

`⚠️` = 2026-11-23 재확인에서 상태가 바뀌었거나, “반복 충전 + 카드 없음 + 전화 인증 없음” 기준을 충족하지 못함. 행은 유지합니다.

| 번호 | 분류 | 대상 서비스 | 실증 성공 키 규격 | 실제 활용 역량 |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **코드 & 인프라** | **GitHub** 🏆 | (Classic PAT) | Actions CI/CD 트리거, 패키지 배포, 레포/PR/스타/팔로우 자동화 |
| **2** | **초고속 LLM** | **Google Gemini** ⚠️ | (Gemini API) | **Gemini 4 Hydrogen** 등 무료 티어 지원(한도는 [AI Studio](https://aistudio.google.com/)에서 확인, 모델·프로젝트마다 다름). 카드 불필요. 무료 티어 데이터는 학습에 쓰일 수 있음. ⚠️ 추가 프로젝트·이상 활동 계정은 [실물 휴대폰 QR 기기 인증](https://aistudio.google.com/docs/verification)이 필요할 수 있음(전화번호는 수집하지 않음). |
| **3** | **초고속 LLM** | **Groq Cloud** 🏆 | (API Key) | 카드·전화 없이 키 발급. 한도는 조직 단위로 **매일 리필**(콘솔 Limits가 최신). 예: `openai/gpt-oss-120b` 30 RPM / 하루 1,000 요청. 초고속 추론 및 Whisper STT. |
| **4** | **초고속 LLM** | **Cerebras Cloud** ⚠️ | (Llama 3.3) | 웨이퍼 엔진 초고속 추론. ⚠️ **결제 수단을 추가해야** API·플레이그라운드가 활성화됨(2026-11 공식 빌링 문서·실측). |
| **5** | **LLM 추론** | **Mistral AI** ⚠️ | | ⚠️ 무료 플랜은 API 키 활성화가 안 됨. 키를 쓰려면 빌링(카드 등) 연결이 필요(2026-11 실측·문서). |
| **6** | **서버리스 GPU** | **Modal Labs** ⚠️ | (API Token) | 스타터 플랜에 월 크레딧 리필이 있으나, ⚠️ **결제 수단이 있어야 사용 가능**하고 초과분은 카드로 청구됨. |
| **7** | **클라우드 VM** | **InstaBox** 🏆 | (Bearer Token) | **계정당 1대 평생 무료 VM (4 vCPU / 8GB RAM / 20GB NVMe)**. REST 셸 원격 실행 |
| **8** | **클라우드 GPU** | **Lightning AI** ⚠️ | API Key / 30 Credits | ⚠️ **신규 가입 중단** (`signups_disabled`, 2026-11-19 실측). |
| **9** | **무료 주피터** | **Google Colab / Kaggle** 🏆 | OAuth / Token | **주 30시간 무료 GPU (T4 x 2, P100)**. 모델 파인튜닝 및 대규모 연산 |
| **10** | **지능형 스크래퍼** | **Scrapling Engine** 🏆 | Open Source Framework | **자가 치유(Self-healing) 셀렉터 + Stealth 브라우저 + MCP Server 내장** |
| **11** | **임베딩/검색** | **Cohere** 🏆 | (Trial API Key) | **Trial 키 매달 1,000 호출 리필**, 카드 불필요. Chat 모델은 분당 20. Rerank·Embed 포함. |
| **12** | **멀티 라우팅** | **OpenRouter** 🏆 | (`sk-or-v1-…`) | **`:free` 모델은 카드 없이** 사용 가능. 기본 **하루 50요청·20RPM**(누적 $10 이상 충전 시 하루 1,000). 예: [`inclusionai/ling-3.2-flash:free`](https://openrouter.ai/inclusionai/ling-3.2-flash:free) (1M 컨텍스트). Claude·GPT 등 유료 플래그십은 크레딧 필요. |
| **13** | **오픈소스 AI** | **Hugging Face** ⚠️ | (Access Token) | Spaces 등 허브 기능은 유지. ⚠️ **Inference Providers는 무료 계정 월 크레딧이 0** — 추론을 쓰려면 크레딧 구매 또는 PRO. |
| **14** | **인공지능 성우** | **ElevenLabs** 🏆 | | **Free 플랜 매달 10,000 크레딧 리필**(무료는 이월 없음). 카드·전화 없이 이메일 또는 Google로 가입. |
| **15** | **이메일 인프라** | **Resend** 🏆 | | 매월 3,000건 이메일 무료 발송 (React Email 템플릿 연동) |
| **16** | **AI 검색 엔진** | **Tavily AI Search** 🏆 | | **매달 1,000 API 크레딧**, 매월 1일 리셋, 공식 카드 불필요. 기본 검색 1크레딧·고급 2크레딧. |
| **17** | **웹 스크래핑** | **Firecrawl** 🏆 | | 동적 JS SPA 페이지를 LLM 친화적 마크다운으로 무인 크롤링 |
| **18** | **웹 스크래핑** | **Outcrawl** ⚠️ | | ⚠️ **서비스 중단**(2026-11-19 실측: `outcrawl.com`이 개인 블로그로 리다이렉트, 앱 DNS 실패). |
| **19** | **브라우저 클라우드** | **Browserbase** 🏆 | (API Key) | **매월 1시간 무료 Headless 브라우저**. 캡차/Cloudflare 우회 내장 Playwright 원격 구동 |
| **20** | **안티차단 프록시** | **Scrapfly** 🏆 | | **매월 1,000 API 크레딧 무료**. 스마트 프록시 풀 + 안티봇 바이패스. (다중 계정 감지 시 수동 심사 가능) |
| **21** | **엔터프라이즈 프록시** | **Bright Data** ⚠️ | Customer ID / API Key | Web Scraper IDE 및 Residential 프록시 테스트. ⚠️ 2026-11 실측에서 **gmail.com 가입이 거부**됨. |
| **22** | **오픈 데이터셋** | **Public APIs Hub** 🏆 | No-Auth / Free Key | 1,400+ 글로벌 공공 API (환율, 날씨, 가상화폐, 주식, 뉴스 등) 무인 연동 |
| **23** | **서버리스 DB** | **Neon Postgres** 🏆 | | Git 스타일 브랜칭 지원 PostgreSQL (0.5GB 무료 + Auto-suspend 0원 유지) |
| **24** | **엣지 DB** | **Turso (LibSQL)** 🏆 | (JWT Token) | 전 세계 엣지 1ms 응답 분산 SQLite (로컬-클라우드 실시간 양방향 동기화) |
| **25** | **BaaS 백엔드** | **Supabase** 🏆 | + Anon/Service | Postgres DB, Auth 인증, Storage, 실시간 웹소켓 통합 백엔드 |
| **26** | **엣지 AI & CDN** | **Cloudflare (Workers AI + R2)** 🏆 | | **매일 10,000 뉴런 무료 AI 추론**(00:00 UTC 리셋). 이메일 가입, 카드·전화 불필요. 일부 신형 모델은 결제 수단이 필요. R2 Egress 전송료 0원. |
| **27** | **미디어 CDN** | **Cloudinary** 🏆 | API Key & Secret | URL 파라미터만으로 9:16 쇼츠 세로 크롭, 자막 오버레이, WebP 최적화 |
| **28** | **프로덕트 분석** | **PostHog** 🏆 | | 매월 1M 이벤트 무료 + 유저 마우스/화면 세션 녹화(Session Replay) |
| **29** | **비디오 스트리밍** | **Mux Video** 🏆 | Token ID / Secret | HLS 고화질 적응형 비트레이트 비디오 스트리밍 & 자동 자막 추출 |
| **30** | **사용자 인증** | **Clerk Auth** 🏆 | Publishable / Secret Key | 50,000 MAU 무료 소셜 로그인 및 사용자 세션 관리 |
| **31** | **서버리스 Redis & 큐** | **Upstash (Redis + QStash)** 🏆 | REST URL / Token | 일 10,000 요청 Redis + **일 500 메시지 지연 큐/크론 스케줄링(QStash)** |
| **32** | **시맨틱 검색** | **Jina AI** ⚠️ | | 키 없이 Reader(`r.jina.ai`)는 IP당 20 RPM. ⚠️ 무료 API 키의 **토큰은 일회 지급**이며, 소진 후 충전이 필요. |
| **33** | **NoSQL 클라우드** | **MongoDB Atlas** 🏆 | Public/Private Key | 512MB 무료 M0 NoSQL 클러스터 및 도큐먼트 데이터베이스 |
| **34** | **무인 데스크톱** | **Simular Box** 🏆 | (MCP Token) | **매일 1,000 크레딧 무료 리셋**. MCP 원격 클라우드 데스크톱 & OS GUI 무인 제어 |
| **35** | **컨테이너 호스팅** | **Koyeb / Fly.io** ⚠️ | API Token | Fly.io org 토큰은 카드 없이 발급 가능(앱 생성은 카드 필요). ⚠️ **Koyeb**은 2026-11-19 실측에서 콘솔이 Mistral 합류 안내만 보이고 API 토큰 UI가 없음. |
| **36** | **오픈소스 프리티어** | **Free-For-Dev Curated** 🏆 | Directory Resource | ripienaar/free-for-dev 기반 1,000+ 클라우드/모니터링/로그 분석 자원 연계 |

---

## 2-1. 반복 충전 · 카드 없음 · 전화 인증 없음 (2026-11-23 검증)

일 또는 월 쿼터가 **반복해서 리필**되고, 가입·키 발급·사용에 **신용카드와 전화번호 인증이 필요 없는** AI 티어만 모았습니다. 일회성 가입 크레딧·기간 한정 프로모는 넣지 않았습니다. (계정은 새로 만들지 않았고, 공식 문서/가격 페이지와 최근 사용기로 확인했습니다.)

이미 위 36개 표에 있는 항목:

| 서비스 | 리필 | 메모 | 링크 |
| :--- | :--- | :--- | :--- |
| **Groq Cloud** | 일일 한도 (예: gpt-oss-120b 하루 1,000요청) | 콘솔 Limits가 최신 | [Keys](https://console.groq.com/keys) · [Limits](https://console.groq.com/docs/rate-limits) |
| **Cloudflare Workers AI** | 매일 10,000 뉴런 (00:00 UTC) | 일부 신형 모델은 결제 수단 필요 | [Pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| **OpenRouter `:free`** | 하루 50요청 · 20RPM | $10 이상 충전 시 하루 1,000 | [Limits](https://openrouter.ai/docs/api_reference/limits) · [Ling 3.2 Flash :free](https://openrouter.ai/inclusionai/ling-3.2-flash:free) |
| **ElevenLabs Free** | 매달 10,000 크레딧 | 무료 플랜은 이월 없음 | [Pricing](https://elevenlabs.io/pricing) |
| **Tavily Researcher** | 매달 1,000 크레딧 (매월 1일 리셋) | 기본 검색 1크레딧 | [Pricing](https://www.tavily.com/pricing) |
| **Cohere Trial** | 매달 1,000 호출 | “Trial” 정책 변경 여지 있음 | [Rate limits](https://docs.cohere.com/docs/rate-limits) |

저장소에 없었거나 빠져 있던 항목:

| 서비스 | 분류 | 리필 | 메모 | 링크 |
| :--- | :--- | :--- | :--- | :--- |
| **Keenable** | 웹 검색 API | 매달 100,000 요청 (조직 생성일 기준 리셋) | 공식 카드 불필요. 무료분 소진 시 402(자동충전을 켠 경우에만 과금) | [Pricing](https://keenable.ai/pricing) |
| **You.com MCP Free** | 검색 MCP | 하루 100회 | 계정·키·카드·전화 없음. `you-search` / `you-extract` / `you-discover` | [Docs](https://you.com/docs/agents/mcp-server) · 엔드포인트 `https://api.you.com/mcp/free` |
| **Context.dev Free** | 스크래핑·검색 | 매달 1,000 크레딧 | 공식 카드 불필요. 무료는 오버에이지 없이 중단 | [Pricing](https://www.context.dev/pricing) |
| **Rime Free** | TTS / STT | 매달 $50 사용량 (이월 없음) | 공식 “No card required”. 메일 인증 또는 Google/GitHub | [Pricing](https://www.rime.ai/pricing) |
| **Coarena Model API** | LLM API | 매일 무료 할당 (안내·사용기 기준 하루 $5, 00:00 UTC 리셋) | 공식 “Free, no card”. Google 로그인. **모든 요청이 저장·라이선스됨** | [Docs](https://coarena.ai/docs) |
| **LG K-EXAONE 2.5** | LLM API | 일일 한도 리필 (학습 미동의 사용기 기준 하루 100회) | 이메일 가입+메일 인증만. 키는 30일 만료. 비상업 약관 | [Rate limits](https://docs.exaone.ai/en/docs/rate-limits) · [Docs](https://docs.exaone.ai) |

**조건부 (이 목록에는 넣지 않음):** Google Gemini API·Gemini Decisions API(`gemini-decision-1`)는 카드 없이 일일 한도가 리필되지만, 일부 프로젝트·계정은 실물 휴대폰 QR 기기 인증이 필요합니다. 자세한 내용은 [Verification](https://aistudio.google.com/docs/verification), [Decisions API](https://aistudio.google.com/docs/decisions-api).

---

## 2-2. 조건 미충족·상태 변경 (삭제하지 않고 표시)

36개 표에서 `⚠️`를 붙인 AI/관련 항목의 이유입니다.

| 서비스 | 이유 (2026-11-23 확인) |
| :--- | :--- |
| **Cerebras Cloud** | API 사용에 결제 수단 필요 |
| **Mistral AI** | 무료 플랜에서 API 키 활성화 불가, 빌링 필요 |
| **Modal Labs** | 월 크레딧이 있어도 결제 수단 필수, 초과분 청구 |
| **Lightning AI** | 신규 가입 중단 (`signups_disabled`) |
| **Outcrawl** | 서비스 중단 |
| **Hugging Face Inference Providers** | 무료 계정 월 크레딧 0 |
| **Jina AI** | 무료 키 토큰은 일회 지급 |
| **Google Gemini** | 무료 티어는 있으나 일부 경우 휴대폰 기기 인증 |
| **Bright Data** | gmail.com 가입 거부 실측 |
| **Koyeb** | API 토큰 UI 없음 (Fly.io는 별도) |

표 밖 후보 중 같은 기준으로 뺀 것: NVIDIA NIM(전화/SMS 인증), Together AI Bonsai(키 생성에 최소 $15 충전), SambaNova(공식 플랜이 결제 수단·크레딧 구매 요구), さくら AI Engine(전화+카드), Parallel 월 $5(카드 필수), Vercel AI Gateway Parallel 검색(2027-01-31까지 기간 한정), Arena $50·Inception 1억 토큰·packet.ai Token Factory(일회성 또는 곧 종료·전화 인증) 등.

---

## 🧭 3. 주요 직통 가입 및 키 생성 링크 (Direct Links)

1. **GitHub PAT**: [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)
2. **Google AI Studio (Gemini)**: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
3. **Groq Cloud**: [https://console.groq.com/keys](https://console.groq.com/keys)
4. **Cerebras Cloud**: [https://cloud.cerebras.ai/](https://cloud.cerebras.ai/) — ⚠️ 결제 수단 필요
5. **Mistral AI**: [https://console.mistral.ai/api-keys](https://console.mistral.ai/api-keys) — ⚠️ 빌링 필요
6. **Modal Labs**: [https://modal.com/](https://modal.com/) — ⚠️ 결제 수단 필요
7. **InstaBox**: [https://instabox.sh/](https://instabox.sh/)
8. **Lightning AI**: [https://lightning.ai/](https://lightning.ai/) — ⚠️ 신규 가입 중단
9. **Google Colab**: [https://colab.research.google.com/](https://colab.research.google.com/)
10. **Scrapling Framework**: [https://github.com/d4vinci/Scrapling](https://github.com/d4vinci/Scrapling)
11. **Cohere**: [https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)
12. **OpenRouter**: [https://openrouter.ai/keys](https://openrouter.ai/keys) · [:free 모델](https://openrouter.ai/models?fmt=cards&max_price=0)
13. **Hugging Face**: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
14. **ElevenLabs**: [https://elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys)
15. **Resend**: [https://resend.com/api-keys](https://resend.com/api-keys)
16. **Tavily AI**: [https://app.tavily.com/home](https://app.tavily.com/home)
17. **Firecrawl**: [https://www.firecrawl.dev/app/api-keys](https://www.firecrawl.dev/app/api-keys)
18. **Outcrawl**: [https://outcrawl.com/](https://outcrawl.com/) — ⚠️ 서비스 중단
19. **Browserbase**: [https://www.browserbase.com/](https://www.browserbase.com/)
20. **Scrapfly**: [https://scrapfly.io/dashboard](https://scrapfly.io/dashboard)
21. **Bright Data**: [https://brightdata.com/cp](https://brightdata.com/cp)
22. **Public APIs Index**: [https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)
23. **Neon Tech**: [https://console.neon.tech/app/settings/api-keys](https://console.neon.tech/app/settings/api-keys)
24. **Turso**: [https://app.turso.tech/settings/tokens](https://app.turso.tech/settings/tokens)
25. **Supabase**: [https://supabase.com/dashboard/account/tokens](https://supabase.com/dashboard/account/tokens)
26. **Cloudflare**: [https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)
27. **Cloudinary**: [https://console.cloudinary.com/settings/api-keys](https://console.cloudinary.com/settings/api-keys)
28. **PostHog**: [https://us.posthog.com/project/settings](https://us.posthog.com/project/settings)
29. **Mux Video**: [https://dashboard.mux.com/settings/access-tokens](https://dashboard.mux.com/settings/access-tokens)
30. **Clerk Auth**: [https://dashboard.clerk.com/](https://dashboard.clerk.com/)
31. **Upstash**: [https://console.upstash.com/](https://console.upstash.com/)
32. **Jina AI**: [https://jina.ai/](https://jina.ai/)
33. **MongoDB Atlas**: [https://cloud.mongodb.com/v2#/account/apiKeys](https://cloud.mongodb.com/v2#/account/apiKeys)
34. **Simular Box**: [https://box.simular.ai/](https://box.simular.ai/)
35. **Koyeb / Fly.io**: [https://app.koyeb.com/](https://app.koyeb.com/) / [https://fly.io/](https://fly.io/)
36. **Free-For-Dev Repository**: [https://github.com/ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev)

신규 AI 티어:

37. **Keenable**: [https://keenable.ai/pricing](https://keenable.ai/pricing)
38. **You.com MCP Free**: [https://you.com/docs/agents/mcp-server](https://you.com/docs/agents/mcp-server) · `https://api.you.com/mcp/free`
39. **Context.dev**: [https://www.context.dev/pricing](https://www.context.dev/pricing)
40. **Rime**: [https://www.rime.ai/pricing](https://www.rime.ai/pricing)
41. **Coarena**: [https://coarena.ai/docs](https://coarena.ai/docs)
42. **LG K-EXAONE 2.5**: [https://docs.exaone.ai](https://docs.exaone.ai)

---

## 📄 License
MIT License. Created by [flam-ing](https://github.com/flam-ing).
