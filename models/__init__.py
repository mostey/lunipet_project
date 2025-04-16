'''
이 파일은 models 디렉토리 내 모든 테이블 정의 파일을 외부에서 쉽게 불러올 수 있도록 연결하는 역할을 함
예: schema.py 또는 향후 추가 할 Flask 앱에서 from models import User, Pet 등으로 간단하게 불러올 수 있게 됨
'''

from models.base import Base

# 각 모델 테이블을 전부 불러와야 SQLAlchemy가 인식함
from models.user import User
from models.user_settings import UserSettings
from models.user_external_services import UserExternalService
from models.pet_types import PetType
from models.pets import Pet
from models.items import Item
from models.user_inventory import UserInventory
from models.activities import Activity
from models.pitstops import Pitstop
from models.pitstop_visits import PitstopVisit
from models.friendships import Friendship
from models.notifications import Notification
from models.coin_transactions import CoinTransaction
from models.challenges import Challenge
from models.challenge_participants import ChallengeParticipant
from models.missions import Mission
from models.user_mission_progress import UserMissionProgress

# 참고: 이 파일이 있어야 schema.py에서 Base.metadata.create_all(bind=engine) 명령이 전체 테이블을 인식하고 생성함