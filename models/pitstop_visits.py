'''
이 파일은 pitstop_visits 테이블을 정의함
사용자가 위치 기반 보상 장소(피트스탑)를 방문한 이력을 저장하는 테이블임
피트스탑은 보상 쿨타임이 있기 때문에, 사용자가 언제 방문했는지를 기록해줘야 반복 보상 제한이 가능함
'''

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import Base

# 피트스탑 방문 기록 테이블 정의
class PitstopVisit(Base):
    __tablename__ = "pitstop_visits"  # 실제 DB에 생성될 테이블 이름

    # 방문 기록 고유 ID
    visit_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키 역할
        autoincrement=True    # 자동 증가
    )

    # 방문한 사용자 ID
    user_id = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블의 user_id 참조 (외래키)
        nullable=False                # 반드시 있어야 함
    )

    # 방문한 피트스탑 ID
    pitstop_id = Column(
        Integer,                          # 정수형
        ForeignKey("pitstops.pitstop_id"),# pitstops 테이블의 ID 참조 (외래키)
        nullable=False                    # 반드시 있어야 함
    )

    # 방문한 시각
    visit_time = Column(
        DateTime,                  # 날짜 및 시간 정보
        nullable=False,            # 반드시 있어야 함
        server_default=func.now()  # 기본값은 현재 시간 자동 입력
    )