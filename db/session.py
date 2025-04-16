'''
이 파일은 데이터베이스와 실제 데이터를 주고받을 때 사용할 '세션(session)'을 만들어주는 도구임
세션은 '로그인된 접속 상태'처럼 생각하면 됨. DB와 안전하게 상호작용 할 수 있게 해줌
'''

from sqlalchemy.orm import sessionmaker
from db.engine import engine  # DB 엔진 객체 불러옴

# 세션을 생성하는 클래스 정의 (SessionLocal이라고 부름)
SessionLocal = sessionmaker(
    bind=engine,      # 어떤 DB에 연결할지 지정
    autocommit=False, # 자동 커밋 안 함 (직접 commit() 호출해야 저장됨)
    autoflush=False   # flush도 자동으로 하지 않음
)

# SessionLocal()을 호출하면 새로운 세션(접속 상태)을 하나 만들 수 있음
# 예: session = SessionLocal()