'''
이 파일은 activities 테이블을 정의함
사용자가 운동(걷기 등)을 한 기록을 저장하는 테이블임
예: 언제 시작해서 언제 끝났는지, 몇 걸음 걸었는지, 펫이 얼마나 경험치를 얻었는지 등을 기록함
'''

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from models.base import Base

# 운동 기록 테이블 정의
class Activity(Base):
    __tablename__ = "activities"  # 실제 DB에 생성될 테이블 이름

    # 운동 기록 고유 ID
    activity_id = Column(
        Integer,            # 정수형
        primary_key=True,   # 기본키
        autoincrement=True  # 자동 증가
    )

    # 어떤 사용자가 운동했는지
    user_id = Column(
        Integer,                        # 정수형
        ForeignKey("users.user_id"),    # users 테이블 참조
        nullable=False                  # 반드시 있어야 함
    )

    # 어떤 펫이 함께 운동했는지
    pet_id = Column(
        Integer,                    # 정수형
        ForeignKey("pets.pet_id"),  # pets 테이블 참조
        nullable=False              # 반드시 있어야 함
    )

    # 운동 시작 시각
    start_time = Column(
        DateTime,         # 날짜 및 시간
        nullable=False    # 반드시 있어야 함
    )

    # 운동 종료 시각
    end_time = Column(
        DateTime,         # 날짜 및 시간
        nullable=False    # 반드시 있어야 함
    )

    # 운동한 총 시간 (초 단위)
    duration_seconds = Column(
        Integer,          # 정수형 (예: 1800 = 30분)
        nullable=False    # 반드시 있어야 함
    )

    # 이동 거리 (단위: 미터)
    distance_meters = Column(
        Float             # 실수형. 소수점 포함
        # NULL 허용됨
    )

    # 총 걸음 수
    steps = Column(
        Integer           # 정수형
        # NULL 허용됨
    )

    # 소모된 칼로리 (단위: kcal, 추정값)
    calories_burned = Column(
        Float             # 실수형
        # NULL 허용됨
    )

    # 사용자가 운동하면서 이동한 경로 데이터 (좌표 등)
    path_data = Column(
        JSON              # JSON 형식으로 저장 (예: 위치 좌표 목록)
        # NULL 허용됨
    )

    # 펫이 운동을 통해 얻은 경험치
    earned_experience = Column(
        Integer,          # 정수형
        nullable=False,   # 반드시 있어야 함
        default=0         # 기본은 0
    )

    # 운동으로 획득한 코인 수
    earned_coins = Column(
        Integer,          # 정수형
        nullable=False,   # 반드시 있어야 함
        default=0         # 기본은 0
    )

    # 운동 기록이 저장된 시각
    created_at = Column(
        DateTime,                  # 날짜 및 시간
        nullable=False,            # 반드시 있어야 함
        server_default=func.now()  # 기본은 현재 시간 자동 저장
    )