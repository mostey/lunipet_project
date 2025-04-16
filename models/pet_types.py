'''
이 파일은 pet_types 테이블을 정의함
루니펫에서 사용되는 가상 동물들의 '종류' 정보를 저장하는 테이블임
예: 강아지, 고양이, 햄스터 등의 종류 이름, 기본 이미지, 설명 등을 담고 있음
실제 동물(pets 테이블)에 연결되는 부모 테이블 개념임
'''

from sqlalchemy import Column, Integer, String, Text
from models.base import Base

# 가상 동물 종류 테이블 정의
class PetType(Base):
    __tablename__ = "pet_types"  # 실제 DB에 생성될 테이블 이름

    # 동물 종류 고유 ID
    type_id = Column(
        Integer,              # 정수형 숫자
        primary_key=True,     # 기본키로 사용됨. 중복 불가
        autoincrement=True    # 새로 생성될 때마다 1씩 자동 증가함
    )

    # 동물 종류 이름 (예: 강아지, 고양이)
    name = Column(
        String(50),           # 최대 50자까지 저장 가능한 문자열
        nullable=False,       # 반드시 입력해야 함 (NULL 안 됨)
        unique=True           # 같은 이름의 동물 종류는 중복될 수 없음
    )

    # 해당 동물 종류의 기본 이미지 경로(URL)
    base_image_url = Column(
        String(512),          # 이미지 URL을 저장함. 최대 512자까지 허용
        nullable=False        # 반드시 값이 있어야 함
        # 예: https://example.com/images/dog.png
        # 실제 저장 방식(내부 저장 or 외부 링크)은 추후 결정 가능
    )

    # 동물 종류에 대한 설명 (성격, 특성 등)
    description = Column(
        Text                  # 긴 글 저장 가능 (제한 없는 문자열)
        # NULL 허용됨 (설명이 비어 있어도 됨)
        # 예: "강아지는 활발하고, 외출을 좋아하는 성격입니다."
    )