'''
이 파일은 user_external_services 테이블을 정의함
사용자가 Google Fit, Apple Health 같은 외부 건강 서비스와 앱을 연동할 때 정보를 저장하는 테이블임
어떤 사용자(user_id)가, 어떤 외부 서비스(service_type)에, 어떤 외부 ID로(external_service_id) 연결되었는지를 저장함
'''

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from models.base import Base
import enum

# 어떤 종류의 외부 서비스인지 구분하는 Enum 정의
class ServiceType(enum.Enum):
    google = "google"  # Google Fit
    apple = "apple"    # Apple Health

# 외부 서비스 연동 정보 테이블 정의
class UserExternalService(Base):
    __tablename__ = "user_external_services"  # 실제 DB 테이블 이름

    # 외부 서비스 연동 고유 ID
    service_id = Column(
        Integer,              # 정수형 숫자
        primary_key=True,     # 이 컬럼이 고유한 기본키 역할을 함
        autoincrement=True    # 자동으로 1씩 증가함
    )

    # 이 연동 정보가 어떤 사용자에 해당하는지 식별
    user_id = Column(
        Integer,                      # 정수형
        ForeignKey("users.user_id"), # users 테이블의 user_id를 참조함 (외래키)
        nullable=False                # 반드시 값이 있어야 함 (NULL 안 됨)
    )

    # 서비스 종류 (google 또는 apple)
    service_type = Column(
        Enum(ServiceType),  # Enum 타입. google 또는 apple만 가능
        nullable=False      # 반드시 있어야 함
    )

    # 외부 서비스에서 이 사용자를 식별하는 고유 ID
    external_service_id = Column(
        String(255),        # 문자열. 최대 255자까지 저장 가능
        nullable=False,     # 반드시 있어야 함
        unique=True         # 중복 불가. 동일한 외부 ID는 두 번 연결될 수 없음
    )