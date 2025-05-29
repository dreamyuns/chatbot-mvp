from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 데이터베이스 객체 생성
db = SQLAlchemy()

class FAQ(db.Model):
    """자주 묻는 질문 모델"""
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)  # 질문
    answer = db.Column(db.Text, nullable=False)           # 답변
    category = db.Column(db.String(50), default='일반')    # 카테고리
    is_popular = db.Column(db.Boolean, default=False)     # 인기 질문 여부
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # 생성 시간
    
    def __repr__(self):
        return f'<FAQ {self.question[:30]}...>'

class UserQuestion(db.Model):
    """사용자가 물어본 질문 모델"""
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)         # 사용자 질문
    answer = db.Column(db.Text)                           # 관리자 답변
    status = db.Column(db.String(20), default='pending')  # 상태: pending, answered
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # 질문 시간
    answered_at = db.Column(db.DateTime)                  # 답변 시간
    
    def __repr__(self):
        return f'<UserQuestion {self.question[:30]}...>'