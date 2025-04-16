'''
이 파일은 MySQL 데이터베이스에 연결할 때 사용할 접속 정보를 설정하는 파일임
사용자 이름, 비밀번호, 주소, 포트, 사용할 데이터베이스 이름 등을 포함함
이 정보는 외부에서 불러와서 엔진(engine) 생성 시 사용됨

아래 형식은 SQLAlchemy에서 사용하는 "접속 URL" 형식임:
mysql+pymysql://사용자이름:비밀번호@서버주소:포트/데이터베이스명
'''

DB_URL = "mysql+pymysql://root:0000@localhost:3306/lunipet_db"