'''
이 파일은 coin_transactions 테이블을 정의함
루니펫 앱에서 사용자가 코인을 얻거나 사용하는 모든 기록을 저장하는 테이블임
예: 운동으로 10코인 획득, 아이템 구매로 20코인 소비 등의 이력을 남김
거래 원인, 코인 변화량, 거래 후 잔액, 관련 대상 ID, 설명 등이 함께 저장됨
'''

from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import Base
import enum

# 코인 거래 원인을 나타내는 Enum(잘못된 값이 들어오는 것을 방지하기 위해, 값의 종류가 정해져 있는 필드만 사용하는 구조.) 정의
class CoinTransactionType(enum.Enum):
    activity = "activity"             # 운동 보상
    pitstop = "pitstop"               # 피트스탑 보상
    mission = "mission"               # 미션 보상
    challenge = "challenge"           # 챌린지 보상
    item_purchase = "item_purchase"   # 아이템 구매
    ad_reward = "ad_reward"           # 광고 시청 보상
    event = "event"                   # 이벤트 보상
    admin = "admin"                   # 관리자 지급 또는 회수
    initial = "initial"               # 초기 지급 (회원가입 보상 등)

# 코인 거래 기록 테이블 정의
class CoinTransaction(Base):
    __tablename__ = "coin_transactions"  # 실제 DB 테이블 이름

    # 거래 고유 ID
    transaction_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키
        autoincrement=True    # 자동 증가
    )

    # 이 거래가 어떤 사용자에 해당하는지
    user_id = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블 참조
        nullable=False                # 반드시 있어야 함
    )

    # 어떤 사유로 인해 코인 변화가 발생했는지
    type = Column(
        Enum(CoinTransactionType),  # Enum 값만 허용됨
        nullable=False              # 반드시 있어야 함
    )

    # 코인의 변화량
    amount = Column(
        Integer,         # 정수형
        nullable=False   # 반드시 있어야 함
        # 양수(+)이면 획득, 음수(-)이면 소비를 의미함
    )

    # 이 거래 이후 남은 총 코인 잔액
    balance_after = Column(
        Integer,         # 정수형
        nullable=False   # 반드시 있어야 함
    )

    # 관련된 대상의 ID (예: activity_id, item_id 등)
    related_id = Column(
        Integer          # 정수형
        # NULL 허용됨 (상황에 따라 연결 여부 다름)
        # 예: 운동 보상일 경우 activity_id 저장
    )

    # 거래 상세 설명 (예: "아이템 3번 구매", "운동 보상 지급")
    description = Column(
        String(255)      # 최대 255자까지 허용
        # NULL 허용됨 (설명 없는 기록도 저장 가능)
    )

    # 거래 발생 시각
    transaction_time = Column(
        DateTime,                  # 날짜 및 시간
        nullable=False,            # 반드시 있어야 함
        server_default=func.now()  # 기본값은 현재 시간
    )