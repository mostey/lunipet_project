'''
이 파일은 missions 테이블을 정의함
사용자에게 제공되는 다양한 유형의 미션 정보를 저장함
예: 특정 거리 걷기, 특정 장소 방문 등의 조건과 보상 정보 포함
'''

from sqlalchemy import Column, Integer, String, Boolean, Text, JSON, ForeignKey
from models.base import Base

# 미션 정의 테이블 클래스
class Mission(Base):
    __tablename__ = "missions"  # 실제 DB 테이블 이름

    # 미션 고유 ID
    mission_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키
        autoincrement=True    # 자동 증가
    )

    # 미션 이름 (예: 하루 5,000보 달성)
    name = Column(
        String(100),          # 최대 100자 문자열
        nullable=False        # 반드시 있어야 함
    )

    # 미션 설명
    description = Column(
        Text                  # 긴 텍스트 설명 저장
        # NULL 허용됨
    )

    # 미션 타입 (걸음 수, 방문, 거리 달성 등)
    type = Column(
        String(50),           # 최대 50자 문자열
        nullable=False        # 반드시 있어야 함
        # 확인 필요 - 추후 기획에 따라 ENUM으로 변경 가능성 있음
    )

    # 목표 달성 조건 (예: {"distance_km": 5})
    goal_criteria = Column(
        JSON,                 # JSON 형식으로 저장
        nullable=False        # 반드시 있어야 함
    )

    # 미션 보상 코인 수
    reward_coins = Column(
        Integer,              # 정수형
        nullable=False,       # 반드시 있어야 함
        default=0             # 기본값은 0
    )

    # 미션 보상 펫 경험치
    reward_experience = Column(
        Integer,              # 정수형
        nullable=False,       # 반드시 있어야 함
        default=0             # 기본값은 0
    )

    # 미션 보상 아이템 ID
    reward_item_id = Column(
        Integer,                            # 정수형
        ForeignKey("items.item_id")         # 외래키: items 테이블 참조
        # NULL 허용됨
    )

    # 보상 아이템 개수
    reward_item_quantity = Column(
        Integer,              # 정수형
        nullable=False,       # 반드시 있어야 함
        default=1             # 기본값 1개
    )

    # 반복 가능 여부
    is_repeatable = Column(
        Boolean,              # 논리형 (True/False)
        nullable=False,       # 반드시 있어야 함
        default=False         # 기본값은 반복 불가
        # 확인 필요 - 기획에 따라 추가 정의 필요
    )

    # 반복 주기 (예: 7일마다)
    repeat_interval_days = Column(
        Integer               # 정수형
        # NULL 허용됨
    )

    # 미션 활성화 여부
    is_active = Column(
        Boolean,              # 논리형
        nullable=False,       # 반드시 있어야 함
        default=True          # 기본값은 활성화 상태
    )