from flask import Flask, render_template, request, jsonify
from model import db, FAQ, UserQuestion
import os

# Flask 앱 생성
app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'  # SQLite 파일
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False            # 경고 메시지 끄기
app.config['SECRET_KEY'] = 'your-secret-key-here'               # 보안 키

# 데이터베이스 초기화
db.init_app(app)

# 데이터베이스 테이블 생성 및 샘플 데이터 추가
with app.app_context():
    # 테이블 생성
    db.create_all()
    
    # 샘플 FAQ 데이터 추가 (처음 실행시에만)
    if FAQ.query.count() == 0:
        print("샘플 FAQ 데이터를 추가합니다...")
        sample_faqs = [
            FAQ(question="체크인 시간은 언제인가요?", 
                answer="체크인 시간은 오후 3시부터 가능합니다. 늦은 체크인이 필요하시면 미리 연락주세요!", 
                category="체크인", is_popular=True),
            
            FAQ(question="주차 가능한가요?", 
                answer="네, 무료 주차장을 이용하실 수 있습니다. 주차 공간이 한정되어 있으니 미리 알려주세요!", 
                category="주차", is_popular=True),
            
            FAQ(question="조식이 포함되어 있나요?", 
                answer="조식은 별도 요금이며, 1인당 15,000원입니다. 전날 밤 10시까지 예약해주세요!", 
                category="식사", is_popular=True),
            
            FAQ(question="와이파이 사용 가능한가요?", 
                answer="네, 전 객실에서 고속 무료 와이파이를 이용하실 수 있습니다!", 
                category="편의시설", is_popular=True),
            
            FAQ(question="체크아웃 시간은 언제인가요?", 
                answer="체크아웃 시간은 오전 11시까지입니다. 연장이 필요하시면 미리 말씀해 주세요!", 
                category="체크아웃", is_popular=False),
        ]
        
        for faq in sample_faqs:
            db.session.add(faq)
        db.session.commit()
        print("샘플 데이터 추가 완료!")

# 홈페이지 라우트 (데이터베이스에서 FAQ 가져오기)
@app.route('/')
def home():
    # 인기 FAQ 모두 가져오기 (limit 제거)
    popular_faqs = FAQ.query.filter_by(is_popular=True).all()
    return render_template('home.html', popular_faqs=popular_faqs)
    #popular_faqs = FAQ.query.filter_by(is_popular=True).limit(3).all()  #
   

# 챗봇 페이지 라우트
@app.route('/chat')
def chat():
    return '''
    <h2>💬 챗봇 페이지</h2>
    <p>곧 멋진 챗봇 인터페이스가 여기에 나타날 예정입니다!</p>
    <a href="/">← 홈으로 돌아가기</a>
    '''

# 관리자 페이지 라우트
@app.route('/admin')
def admin():
    return '''
    <h2>⚙️ 관리자 페이지</h2>
    <p>FAQ 관리 기능이 곧 추가될 예정입니다!</p>
    <a href="/">← 홈으로 돌아가기</a>
    '''

# API: 모든 FAQ 가져오기
@app.route('/api/faqs')
def get_faqs():
    faqs = FAQ.query.all()
    return jsonify([{
        'id': faq.id,
        'question': faq.question,
        'answer': faq.answer,
        'category': faq.category,
        'is_popular': faq.is_popular
    } for faq in faqs])

# API 테스트 라우트
@app.route('/api/test')
def api_test():
    # 데이터베이스 연결 테스트
    faq_count = FAQ.query.count()
    return jsonify({
        "message": "API가 정상적으로 작동합니다!",
        "status": "success",
        "database": "connected",
        "faq_count": faq_count
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)