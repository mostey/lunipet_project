'''
이 파일은 friendships 테이블을 정의함
사용자 간의 친구 관계를 저장하는 테이블임
예: 친구 요청을 보냈는지(pending), 수락했는지(accepted), 차단했는지(blocked) 등 관계 상태를 저장함
'''

from sqlalchemy import Column, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import Base
import enum

# 친구 관계 상태를 나타내는 Enum 정의
class FriendshipStatus(enum.Enum):
    pending = "pending"     # 친구 요청 중 (대기 상태)
    accepted = "accepted"   # 친구 수락됨
    blocked = "blocked"     # 차단 상태

# 친구 관계 테이블 정의
class Friendship(Base):
    __tablename__ = "friendships"  # 실제 DB에 생성될 테이블 이름

    # 친구 관계 고유 ID
    friendship_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키
        autoincrement=True    # 자동 증가
    )

    # 요청을 보낸 사용자 ID
    user_id1 = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블의 user_id 참조
        nullable=False                # 반드시 있어야 함
    )

    # 요청을 받은 사용자 ID
    user_id2 = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블 참조
        nullable=False                # 반드시 있어야 함
    )

    # 친구 관계의 상태 (대기 중 / 수락 / 차단 중)
    status = Column(
        Enum(FriendshipStatus),  # Enum으로 상태값 지정
        nullable=False,          # 반드시 있어야 함
        default=FriendshipStatus.pending  # 기본값은 친구 요청 중 상태
    )

    # 친구 요청이 처음 발생한 시간
    requested_at = Column(
        DateTime,                  # 날짜 및 시간
        nullable=False,            # 반드시 있어야 함
        server_default=func.now()  # 기본값은 현재 시간
    )

    # 친구 요청이 수락된 시간
    accepted_at = Column(
        DateTime                  # 날짜 및 시간
        # NULL 허용됨 (아직 수락되지 않은 경우 비어 있음)
    )