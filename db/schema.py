'''
이 파일은 데이터베이스에 모든 테이블을 실제로 생성하는 스크립트임
models 폴더에 정의된 모든 테이블 구조들을 불러와서 MySQL DB에 반영함 (CREATE TABLE 작업)
이 파일을 실행하면 MySQL에 테이블들이 전부 자동으로 생성됨
'''

from db.engine import engine         # DB 연결 객체 불러옴
from models import Base              # Base: 모든 테이블이 상속하는 SQLAlchemy 기본 클래스
import models                        # models 폴더 안의 모든 테이블 정의를 불러오기 위함

def create_all_tables():
    """
    전체 테이블을 MySQL DB에 생성하는 함수.
    실행하면 루니펫 앱에서 사용할 17개의 모든 테이블이 DB에 만들어짐.
    """
    print("MySQL 데이터베이스에 테이블 생성 시작함...")
    Base.metadata.create_all(bind=engine)
    print("모든 테이블 생성 완료됨.")

# 단독 실행 시, 위 함수 자동 실행되도록 설정
if __name__ == "__main__":
    create_all_tables()