'''
이 파일은 SQLAlchemy에서 사용할 DB 연결 엔진을 생성하는 파일임
엔진은 Python 코드와 MySQL 사이를 연결해주는 '통신 케이블' 같은 역할을 함
'''

from sqlalchemy import create_engine
from db.config import DB_URL  # 접속 정보 불러옴

# SQLAlchemy 엔진 생성
engine = create_engine(
    DB_URL,        # 접속 URL 정보 (config.py에서 불러온 것)
    echo=True,     # True로 설정하면 SQL 실행 로그를 출력함
    future=True    # 최신 SQLAlchemy 문법을 사용하도록 설정함
)