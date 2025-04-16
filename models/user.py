'''
이 파일은 users 테이블을 정의함
사용자 로그인 정보, 프로필 정보, 멤버십 정보 등을 저장함
루니펫 앱에서 가장 기본이 되는 사용자 계정 정보를 관리함
'''

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime
from sqlalchemy.sql import func
from models.base import Base
import enum

# 멤버십 타입을 구분하기 위한 Enum 클래스 정의함
# 사용자가 무료(free)인지 유료(paid)인지 구분하는 용도임
class MembershipType(enum.Enum):
    free = "free"   # 무료 멤버십
    paid = "paid"   # 유료 멤버십

# users 테이블 클래스 정의 시작
class User(Base):
    __tablename__ = "users"  # 실제 DB에 생성될 테이블 이름은 'users'임

    # 사용자 고유 ID
    user_id = Column(
        Integer,             # 정수형 숫자임 (예: 1, 2, 3, ...)
        primary_key=True,    # 이 컬럼이 테이블에서 '고유한 키(PK)'가 됨. 중복 안됨
        autoincrement=True   # 새로운 사용자가 추가될 때마다 번호가 자동으로 1씩 증가함
    )

    # 로그인에 사용할 사용자명 (아이디)
    username = Column(
        String(50),          # 최대 50자까지 입력 가능한 문자열임
        nullable=False,      # 반드시 입력해야 하는 값임 (NULL 허용 안 함)
        unique=True          # 같은 값을 가진 사용자가 두 명 이상 존재할 수 없음 (중복 금지)
    )

    # 사용자 이메일 주소
    email = Column(
        String(255),         # 최대 255자까지 입력 가능한 문자열임
        nullable=False,      # 반드시 입력해야 하는 값임
        unique=True          # 이메일도 중복 불가 (하나의 이메일은 한 명만 사용 가능)
    )

    # 비밀번호를 암호화한 결과 (평문 저장 안 함)
    password_hash = Column(
        String(255),         # 암호화된 문자열이기 때문에 긴 길이를 허용함
        nullable=False       # 무조건 입력해야 함 (비밀번호 없는 계정은 허용하지 않음)
    )

    # 앱 내에서 보여지는 닉네임
    nickname = Column(
        String(50),          # 최대 50자까지 허용함
        nullable=False,      # 닉네임은 반드시 있어야 함
        unique=True          # 닉네임도 중복 금지 (중복 허용하려면 False로 바꿔야 함)
    )

    # 보유 중인 루니펫 코인 수
    coins = Column(
        Integer,             # 정수형 숫자 (예: 100, 250 등)
        nullable=False,      # 항상 값이 있어야 함
        default=0            # 처음 가입하면 기본적으로 코인 0개부터 시작함
    )

    # 멤버십 종류 (무료 or 유료)
    membership_type = Column(
        Enum(MembershipType),     # 위에서 정의한 Enum 타입을 사용함
        nullable=False,           # 반드시 값이 있어야 함
        default=MembershipType.free  # 기본값은 'free' (무료)로 설정함
    )

    # 유료 멤버십 만료일
    membership_expiry_date = Column(
        DateTime                  # 날짜 및 시간 저장 (예: 2025-01-01 00:00:00)
        # nullable=True 이므로 값을 안 넣어도 됨
    )

    # 이메일 인증 여부 (True/False)
    is_email_verified = Column(
        Boolean,                  # 논리형 (True 또는 False 값만 가능)
        nullable=False,           # 반드시 값이 있어야 함
        default=False             # 기본값은 인증 안 된 상태(False)
    )

    # 프로필을 공개할지 여부
    profile_public = Column(
        Boolean,                  # True이면 다른 사용자도 이 사람의 프로필 볼 수 있음
        nullable=False,           # 값이 반드시 있어야 함
        default=True              # 기본값은 공개 상태(True)
    )

    # 사용자가 가입한 시각
    created_at = Column(
        DateTime,                 # 날짜 및 시간 정보 저장
        nullable=False,           # 반드시 값이 있어야 함
        server_default=func.now() # 값을 입력하지 않아도 자동으로 현재 시간이 저장됨
    )

    # 마지막으로 로그인한 시각
    last_login_at = Column(
        DateTime                  # 로그인할 때마다 시간 업데이트됨
        # nullable=True이므로 처음엔 비어있을 수 있음
    )