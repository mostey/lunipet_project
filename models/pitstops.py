'''
이 파일은 pitstops 테이블을 정의함
루니펫 앱에서 위치 기반으로 제공되는 보상 지점(피트스탑)의 정보를 저장함
예: 공원, 놀이터 같은 장소를 등록하고, 사용자가 여기에 방문하면 보상을 지급할 수 있도록 설정하는 테이블임
'''

from sqlalchemy import Column, Integer, String, Enum, Text, Float, Boolean, JSON
from models.base import Base
import enum

# 보상 종류를 지정하는 Enum 클래스 정의
class RewardType(enum.Enum):
    coin = "coin"     # 코인 지급
    exp = "exp"       # 경험치 지급
    item = "item"     # 아이템 지급
    buff = "buff"     # 일시적 능력치 상승 등

# 피트스탑 테이블 정의
class Pitstop(Base):
    __tablename__ = "pitstops"  # 실제 DB에 생성될 테이블 이름

    # 피트스탑 고유 ID
    pitstop_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키
        autoincrement=True    # 자동 증가
    )

    # 피트스탑 이름 (예: "서울숲 공원", "루니 스팟 A")
    name = Column(
        String(100),      # 최대 100자까지 허용
        nullable=False    # 반드시 있어야 함
    )

    # 위도 정보 (GPS 좌표)
    latitude = Column(
        Float(precision=8),  # 소수점 포함하여 정밀한 위치 저장
        nullable=False       # 반드시 있어야 함
    )

    # 경도 정보 (GPS 좌표)
    longitude = Column(
        Float(precision=8),  # 정밀한 위치 저장
        nullable=False       # 반드시 있어야 함
    )

    # 피트스탑 설명 (어떤 장소인지 설명)
    description = Column(
        Text                 # 길고 자유로운 설명 가능
        # NULL 허용됨
    )

    # 보상 종류 (코인, 경험치, 아이템 등)
    reward_type = Column(
        Enum(RewardType),   # RewardType ENUM 사용
        nullable=False      # 반드시 있어야 함
    )

    # 보상 상세 정보 (예: {"amount": 5}, {"item_id": 10})
    reward_details = Column(
        JSON,               # JSON 형식으로 구조화된 데이터 저장
        nullable=False      # 반드시 있어야 함
    )

    # 재방문 대기 시간 (초 단위) – 예: 24시간 = 86400초
    cooldown_seconds = Column(
        Integer,          # 정수형
        nullable=False,   # 반드시 있어야 함
        default=86400     # 기본값은 하루(24시간)
    )

    # 피트스탑이 현재 활성 상태인지 여부
    is_active = Column(
        Boolean,         # True: 방문 가능 / False: 비활성화됨
        nullable=False,  # 반드시 있어야 함
        default=True     # 기본은 활성화 상태
    )