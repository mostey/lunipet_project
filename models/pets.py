'''
이 파일은 pets 테이블을 정의함
루니펫 앱에서 사용자가 키우는 가상의 동물 정보를 저장함
동물의 종류는 pet_types 테이블을 참조함
사용자 ID도 연결되어 있어, 누가 어떤 동물을 소유하는지 명확하게 알 수 있음
또한 동물의 상태(레벨, 경험치, 기분, 배고픔, 병 여부 등)를 저장함
'''

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import Base

# 가상 동물 테이블 정의
class Pet(Base):
    __tablename__ = "pets"  # 실제 DB에 생성될 테이블 이름

    # 가상 동물 고유 ID
    pet_id = Column(
        Integer,              # 정수형 숫자
        primary_key=True,     # 기본키로 사용됨
        autoincrement=True    # 자동 증가 값
    )

    # 이 동물이 어떤 사용자에게 속하는지 식별하는 값
    user_id = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블의 user_id를 참조함 (외래키)
        nullable=False                # 반드시 있어야 함 (NULL 불가)
    )

    # 이 동물이 어떤 종류인지 식별하는 값
    pet_type_id = Column(
        Integer,                         # 정수형
        ForeignKey("pet_types.type_id"),# pet_types 테이블의 type_id 참조 (외래키)
        nullable=False                   # 반드시 있어야 함
    )

    # 사용자가 직접 설정한 동물의 이름
    name = Column(
        String(50),      # 최대 50자까지 허용
        nullable=False   # 필수 입력값
    )

    # 동물의 현재 레벨
    level = Column(
        Integer,         # 정수형
        nullable=False,  # 값이 반드시 있어야 함
        default=1        # 기본값은 1레벨
    )

    # 현재 누적된 경험치
    experience = Column(
        Integer,         # 정수형
        nullable=False,  # 필수
        default=0        # 기본값은 0
    )

    # 동물의 현재 기분 상태 (예: happy, sad 등)
    mood = Column(
        String(50)       # 기분 상태를 문자열로 저장함
        # NULL 허용됨 (기분을 저장하지 않아도 됨)
    )

    # 동물의 배고픔 정도 (0~100 사이 값)
    hunger_level = Column(
        Integer,         # 정수형
        nullable=False,  # 반드시 값이 있어야 함
        default=100      # 기본은 배부른 상태(100)
    )

    # 병에 걸려 있는지 여부 (True: 아픔, False: 건강함)
    is_sick = Column(
        Boolean,         # 논리형
        nullable=False,  # 반드시 있어야 함
        default=False    # 기본은 아프지 않은 상태
    )

    # 마지막으로 밥을 준 시각
    last_fed_at = Column(
        DateTime         # 날짜 및 시간 정보
        # NULL 허용됨. 아직 밥을 한 번도 안 준 경우 비어있을 수 있음
    )

    # 마지막으로 놀아준 시각
    last_played_at = Column(
        DateTime         # 날짜 및 시간 정보
        # NULL 허용됨
    )

    # 이 동물이 생성된 시각 (처음 만들어진 시간)
    created_at = Column(
        DateTime,                  # 날짜 및 시간
        nullable=False,            # 반드시 있어야 함
        server_default=func.now()  # 생성 시 자동으로 현재 시간 입력됨
    )