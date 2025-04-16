'''
이 파일은 루트 디렉토리에서 MySQL DB에 모든 테이블을 생성하기 위한 실행 파일임
이 파일만 실행하면 DB 테이블이 전부 만들어짐
내부적으로는 db/schema.py에 정의된 create_all_tables() 함수를 호출함
'''

from db.schema import create_all_tables  # 테이블 생성 함수 불러옴

if __name__ == "__main__":
    print("루니펫 데이터베이스 테이블 생성 시작함...\n")
    create_all_tables()
    print("\n모든 테이블이 성공적으로 생성되었음.")