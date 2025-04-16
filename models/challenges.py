'''
이 파일은 challenges 테이블을 정의함
루니펫 앱 내에서 열리는 챌린지 정보를 저장함
예: 챌린지 제목, 설명, 종류, 시작/종료 시각, 보상 정보 등
'''

from sqlalchemy import Column, Integer, String, Enum, Text, DateTime, JSON
from models.base import Base
import enum

# 챌린지 종류를 나타내는 Enum 클래스 정의함
class ChallengeType(enum.Enum):
    one_on_one = "1v1_steps"   # 1:1 걸음 수 대결
    group_total = "group_dist" # 그룹 누적 거리 챌린지

# 챌린지 상태를 나타내는 Enum 클래스 정의함
class ChallengeStatus(enum.Enum):
    upcoming = "upcoming"       # 챌린지 시작 전
    ongoing = "ongoing"         # 챌린지 진행 중
    completed = "completed"     # 챌린지 완료됨
    cancelled = "cancelled"     # 챌린지 취소됨

# 챌린지 테이블 클래스 정의 시작
class Challenge(Base):
    __tablename__ = "challenges"  # 실제 DB 테이블 이름은 'challenges'임

    # 챌린지 고유 ID
    challenge_id = Column(
        Integer,               # 정수형
        primary_key=True,      # 기본키
        autoincrement=True     # 자동 증가
    )

    # 챌린지 이름
    name = Column(
        String(100),           # 최대 100자까지 저장 가능
        nullable=False         # 반드시 입력해야 함
    )

    # 챌린지 설명
    description = Column(
        Text                   # 긴 문자열 설명 허용
        # NULL 허용됨
    )

    # 챌린지 종류 (1:1 걸음 수 대결 or 그룹 거리 누적)
    type = Column(
        Enum(ChallengeType),   # ChallengeType ENUM 사용
        nullable=False         # 반드시 입력해야 함
    )

    # 챌린지 시작 시각
    start_time = Column(
        DateTime,              # 날짜 및 시간
        nullable=False         # 반드시 입력해야 함
    )

    # 챌린지 종료 시각
    end_time = Column(
        DateTime,              # 날짜 및 시간
        nullable=False         # 반드시 입력해야 함
    )

    # 챌린지 상태 (예: 예정, 진행 중, 완료, 취소)
    status = Column(
        Enum(ChallengeStatus),        # ChallengeStatus ENUM 사용
        nullable=False                # 반드시 입력해야 함
    )

    # 챌린지 완료 시 보상 정보 (예: {"coins": 100}, {"item_id": 3})
    reward_details = Column(
        JSON                   # JSON 형식으로 보상 내용 저장
        # NULL 허용됨
    )