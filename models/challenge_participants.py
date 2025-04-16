'''
이 파일은 challenge_participants 테이블을 정의함
사용자가 어떤 챌린지에 언제 참여했고, 어떤 진행 상태와 결과를 가지고 있는지 저장함
예: 사용자 A가 챌린지 2에 참여했고, 참여 시각은 2025-04-10, 현재 진행률은 80%, 2등이며 우승 여부는 False임
'''

from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, JSON
from models.base import Base

# 챌린지 참가자 정보를 저장하는 테이블 클래스 정의
class ChallengeParticipant(Base):
    __tablename__ = "challenge_participants"  # 실제 DB 테이블 이름

    # 챌린지 참가 기록의 고유 ID
    participant_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키
        autoincrement=True    # 자동 증가
    )

    # 사용자가 참여한 챌린지 ID
    challenge_id = Column(
        Integer,                                  # 정수형
        ForeignKey("challenges.challenge_id"),    # 외래키: challenges 테이블 참조
        nullable=False                            # 반드시 있어야 함
    )

    # 챌린지에 참여한 사용자 ID
    user_id = Column(
        Integer,                             # 정수형
        ForeignKey("users.user_id"),         # 외래키: users 테이블 참조
        nullable=False                       # 반드시 있어야 함
    )

    # 챌린지 진행 상황 (예: {"steps": 3000, "distance": 1.2})
    progress = Column(
        JSON              # JSON 형식 (예: {"걸음 수": 5000, "거리": 2.4})
        # NULL 허용됨
    )

    # 순위 (예: 1위, 2위 등)
    rank = Column(
        Integer           # 정수형 순위
        # NULL 허용됨
    )

    # 챌린지 우승 여부
    is_winner = Column(
        Boolean           # True = 우승, False = 우승 아님
        # NULL 허용됨
    )

    # 챌린지에 참여한 날짜 및 시간
    joined_at = Column(
        DateTime,         # DATETIME 형식
        nullable=False    # 반드시 있어야 함
    )