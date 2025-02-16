from flask import render_template  # render_template 함수 임포트
from app import app

@app.route('/')
@app.route('/index')
def index():
    # 모의 사용자 데이터
    user = {'username': 'Miguel'}

    # 모의 게시물 데이터
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    # 템플릿 렌더링
    return render_template('index.html', title='Home', user=user, posts=posts)