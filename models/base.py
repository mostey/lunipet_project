'''
이 파일은 모든 테이블들이 공통적으로 사용하는 '기본 클래스'를 정의함
실제로는 다른 테이블들이 이 파일의 Base를 상속받아 사용함
마치 문서 양식에서 '모든 서류는 이 양식을 따르세요' 같은 느낌임
'''

from sqlalchemy.orm import declarative_base

# SQLAlchemy에서 제공하는 베이스 클래스 생성
Base = declarative_base()