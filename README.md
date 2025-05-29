# 🏠 숙소 문의 챗봇 서비스

Flask로 제작한 숙소 예약 문의 챗봇 MVP 서비스입니다.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.0+-orange.svg)

## ✨ 주요 기능

- 💬 **실시간 챗봇 상담**: 숙소에 대한 궁금증을 즉시 해결
- 📚 **FAQ 시스템**: 자주 묻는 질문 자동 답변  
- 🗃️ **질문 관리**: 사용자 질문 저장 및 관리
- 📱 **반응형 디자인**: 모바일과 데스크톱 모두 지원
- ⚡ **빠른 응답**: 키워드 기반 즉시 답변

## 🛠️ 기술 스택

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Template Engine**: Jinja2
- **Version Control**: Git, GitHub

## 🚀 실행 방법

### 1. 저장소 복제
```bash
git clone https://github.com/dreamyuns/chatbot-mvp.git
cd chatbot-mvp

2. 가상환경 생성 및 활성화
bashpython -m venv venv

# Windows
venv\Scripts\activate


3. 패키지 설치
bashpip install -r requirements.txt


4. 애플리케이션 실행
bashpython app.py


5. 브라우저에서 확인
http://localhost:5000에 접속하여 서비스를 이용하세요!


📊 API 엔드포인트
MethodEndpointDescriptionGET/홈페이지GET/chat챗봇 페이지GET/admin관리자 페이지GET/api/faqs모든 FAQ 조회GET/api/testAPI 상태 확인


📸 스크린샷
홈페이지

깔끔한 메인 화면
인기 FAQ 표시
반응형 카드 레이아웃


데이터베이스 구조
sql-- FAQ 테이블
CREATE TABLE faq (
    id INTEGER PRIMARY KEY,
    question VARCHAR(500) NOT NULL,
    answer TEXT NOT NULL,
    category VARCHAR(50),
    is_popular BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 사용자 질문 테이블  
CREATE TABLE user_question (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT,
    status VARCHAR(20) DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
📝 개발 진행 상황

 Flask 웹 애플리케이션 구축
 데이터베이스 모델 설계 및 구현
 기본 FAQ 시스템 구현
 반응형 웹 디자인 적용
 Git 버전 관리 시스템 구축
 실시간 챗봇 기능 구현
 관리자 패널 개발
 배포 환경 구축

🔮 향후 계획

Week 6-7: 실제 챗봇 대화 기능 구현
Week 8-9: 관리자 패널 개발
Week 10-12: 배포 및 운영 환경 구축

💡 배운 점
이 프로젝트를 통해 학습한 내용들:

Python Flask 웹 프레임워크 활용
SQLAlchemy ORM을 통한 데이터베이스 관리
HTML/CSS/Bootstrap을 활용한 프론트엔드 개발
Git/GitHub을 통한 버전 관리
웹 애플리케이션 아키텍처 설계

👨‍💻 개발자
윤성균 - 기획 및 개발

GitHub: @dreamyuns
프로젝트 기간: 2025년 06월

📄 라이선스
이 프로젝트는 MIT License 하에 배포됩니다.

⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!
