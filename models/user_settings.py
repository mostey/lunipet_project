'''
이 파일은 user_settings 테이블을 정의함
각 사용자가 앱 내에서 직접 설정한 개인 설정값을 저장하는 테이블임
예: 하루 목표 걸음 수, 알림 받기 여부, 앱의 테마 설정 등
'''

from sqlalchemy import Column, Integer, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import Base
import enum

# 테마 종류를 미리 지정함 (라이트 모드 or 다크 모드)
class ThemeType(enum.Enum):
    light = "light"  # 밝은 테마
    dark = "dark"    # 어두운 테마

class UserSettings(Base):
    __tablename__ = "user_settings"  # 실제 DB에 생성될 테이블 이름

    # 설정 고유 ID
    setting_id = Column(
        Integer,              # 정수형
        primary_key=True,     # 고유 ID. 중복 불가. 테이블 내에서 유일해야 함
        autoincrement=True    # 자동으로 1씩 증가함
    )

    # 설정이 어떤 사용자에게 속하는지 식별하는 컬럼
    user_id = Column(
        Integer,                        # 정수형
        ForeignKey("users.user_id"),   # users 테이블의 user_id를 참조함 (외래키)
        nullable=False,                # 반드시 있어야 함 (NULL 안됨)
        unique=True                    # 사용자 1명당 설정은 하나만 있어야 하므로 중복 금지
    )

    # 하루 목표 걸음 수
    daily_step_goal = Column(
        Integer,         # 정수형
        nullable=False,  # 반드시 있어야 함
        default=10000    # 기본값은 만보
    )

    # 알림을 받을지 여부
    notification_enabled = Column(
        Boolean,         # 논리형 (True 또는 False)
        nullable=False,  # 반드시 있어야 함
        default=True     # 기본은 알림 받는 상태(True)
    )

    # 앱의 테마 설정 (라이트 or 다크)
    theme = Column(
        Enum(ThemeType),  # 미리 정의한 Enum 값(light 또는 dark)만 입력 가능
        nullable=False,   # 반드시 있어야 함
        default=ThemeType.light  # 기본은 라이트 테마
    )

    # 마지막 설정 변경 시각
    last_updated_at = Column(
        DateTime,                  # 날짜 및 시간 저장
        nullable=False,            # 반드시 있어야 함
        server_default=func.now(), # 기본값은 현재 시간
        onupdate=func.now()        # 값이 변경될 때마다 자동으로 갱신됨
    )