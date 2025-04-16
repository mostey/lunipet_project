'''
이 파일은 user_inventory 테이블을 정의함
루니펫 게임에서 사용자가 보유한 모든 아이템을 관리하는 테이블임
예: 어떤 사용자가 어떤 아이템을 몇 개 가지고 있는지, 그중 착용한 건 무엇인지 저장함
'''

from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import Base

# 사용자 인벤토리 테이블 정의
class UserInventory(Base):
    __tablename__ = "user_inventory"  # 실제 DB에 생성될 테이블 이름

    # 인벤토리 고유 ID
    inventory_id = Column(
        Integer,              # 정수형 숫자
        primary_key=True,     # 기본키 역할
        autoincrement=True    # 자동으로 1씩 증가함
    )

    # 이 인벤토리가 어떤 사용자에게 속해 있는지
    user_id = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블의 user_id 참조 (외래키)
        nullable=False                # 반드시 값이 있어야 함
    )

    # 인벤토리에 담긴 아이템이 무엇인지
    item_id = Column(
        Integer,                     # 정수형
        ForeignKey("items.item_id"),# items 테이블의 item_id 참조 (외래키)
        nullable=False               # 반드시 있어야 함
    )

    # 이 아이템을 몇 개 보유 중인지
    quantity = Column(
        Integer,         # 정수형 (예: 1개, 3개 등)
        nullable=False,  # 값이 반드시 있어야 함
        default=1        # 기본값은 1개
    )

    # 이 아이템을 언제 획득했는지
    obtained_at = Column(
        DateTime,                  # 날짜 및 시간
        nullable=False,            # 반드시 있어야 함
        server_default=func.now()  # 현재 시간 자동 입력
    )

    # 착용 중인지 여부 (True면 착용 상태)
    is_equipped = Column(
        Boolean,         # 논리형 (True / False)
        nullable=False,  # 반드시 값 있어야 함
        default=False    # 기본은 착용하지 않은 상태
    )

    # 어떤 펫에게 장착되어 있는지 (코스튬 아이템의 경우에만 해당)
    equipped_pet_id = Column(
        Integer,                  # 정수형
        ForeignKey("pets.pet_id")# pets 테이블의 pet_id 참조 (외래키)
        # NULL 허용됨 → 착용하지 않았거나, 펫에게 연결되지 않았으면 비어있음
    )