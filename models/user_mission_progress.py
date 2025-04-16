'''
이 파일은 user_mission_progress 테이블을 정의함
사용자가 수행 중인 미션에 대한 진행 상태, 반복 횟수, 시간 기록 등을 저장함
'''

from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, JSON
from sqlalchemy.sql import func, text
from models.base import Base
import enum

# 미션 상태 ENUM 정의
class MissionStatus(enum.Enum):
    ongoing = "ongoing"       # 진행 중
    completed = "completed"   # 완료됨

# 사용자 미션 진행 상황 테이블 클래스
class UserMissionProgress(Base):
    __tablename__ = "user_mission_progress"

    # 고유 ID
    progress_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키
        autoincrement=True    # 자동 증가
    )

    # 사용자 ID (누가 이 미션을 수행 중인지)
    user_id = Column(
        Integer,                          # 정수형
        ForeignKey("users.user_id"),     # users 테이블 참조
        nullable=False                   # 반드시 있어야 함
    )

    # 어떤 미션인지 식별
    mission_id = Column(
        Integer,                             # 정수형
        ForeignKey("missions.mission_id"),  # missions 테이블 참조
        nullable=False                      # 반드시 있어야 함
    )

    # 몇 번째 달성인지 (반복 미션일 경우)
    completion_instance = Column(
        Integer,              # 정수형
        nullable=False,       # 반드시 있어야 함
        server_default=text("1")  # 기본값 1
    )

    # 현재 진행 상황 저장 (예: {"distance_km": 2.3, "count": 1})
    current_progress = Column(
        JSON,                 # JSON 형식
        nullable=False        # 반드시 있어야 함
    )

    # 미션 상태 (진행 중인지 완료됐는지)
    status = Column(
        Enum(MissionStatus),   # ENUM 타입 ('ongoing', 'completed')
        nullable=False,        # 반드시 있어야 함
        server_default=text("'ongoing'")  # 기본값은 'ongoing'
    )

    # 미션 시작(또는 재시작) 시각
    started_at = Column(
        DateTime,                        # DATETIME 타입
        nullable=False,                  # 반드시 있어야 함
        server_default=func.now()        # 기본값은 현재 시각
    )

    # 미션 완료 시각
    completed_at = Column(
        DateTime                         # DATETIME 타입
        # NULL 허용됨
    )

    # 미션 진행 상황 변경 시 자동 갱신되는 시각
    last_updated_at = Column(
        DateTime,                                # DATETIME 타입
        nullable=False,                          # 반드시 있어야 함
        server_default=func.now(),               # 생성 시 현재 시각 저장
        onupdate=func.now()                      # 갱신 시 자동 업데이트
    )