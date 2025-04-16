'''
이 파일은 notifications 테이블을 정의함
사용자가 받는 알림 메시지를 저장하는 테이블임
예: 친구 요청 알림, 걸음 수 부족 알림, 미션 완료 알림 등
알림을 보낸 시간, 읽었는지 여부, 관련된 대상 ID 등을 함께 저장함
'''

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import Base

# 알림 테이블 정의
class Notification(Base):
    __tablename__ = "notifications"  # 실제 DB에 생성될 테이블 이름

    # 알림 고유 ID
    notification_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 기본키
        autoincrement=True    # 자동 증가
    )

    # 이 알림을 받을 사용자 ID
    user_id = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블 참조
        nullable=False                # 반드시 있어야 함
    )

    # 알림 종류 (예: "친구 요청", "미션 알림", "걸음 수 미달")
    type = Column(
        String(50),      # 최대 50자까지 허용
        nullable=False   # 반드시 있어야 함
    )

    # 알림 메시지 내용
    message = Column(
        Text,            # 긴 문자열 허용
        nullable=False   # 반드시 있어야 함
    )

    # 알림이 어떤 대상과 관련 있는 경우 그 대상 ID1
    related_id1 = Column(
        Integer          # 정수형
        # NULL 허용됨 (필수 관계 아님, 상황에 따라 사용)
        # 예: 친구 요청이면 요청한 사람의 ID
    )

    # 알림이 두 번째 대상과 관련 있는 경우 그 대상 ID2
    related_id2 = Column(
        Integer          # 정수형
        # NULL 허용됨 (선택적 관계)
        # 예: 챌린지 ID, 미션 ID 등
    )

    # 알림을 읽었는지 여부
    is_read = Column(
        Boolean,         # True/False
        nullable=False,  # 반드시 있어야 함
        default=False    # 기본은 안 읽은 상태(False)
    )

    # 알림이 생성된 시각
    created_at = Column(
        DateTime,                  # 날짜 및 시간
        nullable=False,            # 반드시 있어야 함
        server_default=func.now()  # 현재 시간 자동 입력
    )