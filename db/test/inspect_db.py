"""
이 파일은 MySQL에 생성된 DB가 실제로 잘 구성되었는지 확인하는 코드임
- 테이블이 정상적으로 생성되었는지
- 각 테이블에 어떤 컬럼(속성)이 있는지를 확인할 수 있음
"""

from sqlalchemy import create_engine, inspect
import sys
import os

# 현재 파일의 상위 디렉토리 (project 루트)를 import 경로에 추가함
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from db.config import DB_URL  # DB 접속 정보를 불러옴

# DB와 연결하기 위한 엔진 객체 생성
engine = create_engine(DB_URL)

# 연결을 기반으로 데이터베이스 구조를 분석할 수 있는 객체(inspector)를 만듦
inspector = inspect(engine)

# 전체 테이블 이름 목록 불러오기
tables = inspector.get_table_names()

# 출력 시작
print("현재 MySQL에 생성된 테이블 목록 및 각 테이블의 컬럼 구조:\n")

# 테이블이 하나도 없을 경우 안내
if not tables:
    print("! 현재 데이터베이스에 생성된 테이블이 없음 !")
else:
    # 테이블별로 반복
    for table in tables:
        print(f"• 테이블 이름: {table}")
        columns = inspector.get_columns(table)

        # 컬럼별로 이름, 타입, nullable 여부 출력
        for col in columns:
            name = col['name']
            col_type = col['type']
            nullable = col['nullable']
            default = col.get('default')
            print(f"   └─ 컬럼: {name} | 타입: {col_type} | Null 허용: {nullable} | 기본값: {default}")
        print("-" * 50)

# 연결 닫기
engine.dispose()