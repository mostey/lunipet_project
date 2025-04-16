'''
이 파일은 items 테이블을 정의함
루니펫 게임 안에서 사용 가능한 모든 아이템(먹이, 코스튬, 회복약 등)을 저장하는 테이블임
각각의 아이템은 이름, 종류(type), 효과(effect), 가격, 이미지 등을 가짐
'''

from sqlalchemy import Column, Integer, String, Enum, Text, JSON
from models.base import Base
import enum

# 아이템의 종류를 구분하는 Enum 정의
class ItemType(enum.Enum):
    costume = "costume"   # 코스튬 (옷, 모자 등 꾸미기 용도)
    food = "food"         # 먹이 (배고픔 수치 회복)
    medicine = "medicine" # 의약품 (병 치료)
    buff = "buff"         # 일시적 효과 (예: 경험치 2배 등)

# 아이템 테이블 정의
class Item(Base):
    __tablename__ = "items"  # 실제 DB에 생성될 테이블 이름

    # 아이템 고유 ID
    item_id = Column(
        Integer,              # 정수형 숫자
        primary_key=True,     # 고유한 기본키
        autoincrement=True    # 자동으로 1씩 증가함
    )

    # 아이템 이름 (예: '강아지 모자', '회복 물약')
    name = Column(
        String(100),      # 최대 100자까지 저장 가능한 문자열
        nullable=False    # 반드시 있어야 함 (이름 없는 아이템은 없음)
    )

    # 아이템 종류 (먹이, 코스튬, 약, 버프 중 하나)
    type = Column(
        Enum(ItemType),   # Enum 형식으로 값 제한함
        nullable=False    # 반드시 입력해야 함
    )

    # 아이템 설명
    description = Column(
        Text              # 제한 없는 긴 문자열 저장 가능
        # NULL 허용됨 (설명 없이도 생성 가능)
    )

    # 아이템 효과 (JSON 형태로 저장)
    effect = Column(
        JSON              # 예: {"exp": 50}, {"hunger": -30}
        # NULL 허용됨 (효과가 없는 경우도 있음)
    )

    # 아이템 상점 가격 (코인 단위)
    price = Column(
        Integer           # 정수형
        # NULL 허용됨 → NULL이면 상점에서 판매하지 않음
        # 예: {"price": NULL} → 이벤트 전용 아이템
    )

    # 아이템 이미지 URL
    image_url = Column(
        String(512)       # 최대 512자까지 저장 가능
        # NULL 허용됨. 나중에 이미지가 준비되면 채울 수 있음
        # 저장 방식은 외부 링크 또는 내부 저장 방식 중 선택 가능
    )