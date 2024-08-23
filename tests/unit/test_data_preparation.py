import uuid
from datetime import datetime

import pytest

from sqlalchemy import insert
from src.db.database import session_factory
from src.dto.schema import LevelDwhDTO, LevelAddDwhDTO, UserAddDwhDTO

from src.model.action_dwh_enum import ActionDWHEnum
from src.model.group_dwh import GroupDWH
from src.model.level_dwh import LevelDWH
from src.model.user_dwh import UserDWH
from src.model.word_dwh import WordDWH


# --------------------TEST CONSTANT--------------------
class DataPreparation:

    TEST_USER_ID = uuid.uuid4()
    TEST_USER_NAME = 'TEST_USER_NAME'
    TEST_USER_EMAIL = 'TEST_USER_EMAIL@gmail.com'
    TEST_PASS = 'TEST_PASS'
    TEST_TELEGRAM_USER_ID = "12341234"

    # Group
    TEST_GROUP_NAME = 'TEST_GROUP_NAME'
    TEST_GROUP_ID = uuid.uuid4()

    TEST_COMMON_GROUP_NAME = 'CUSTOM_GROUP'
    TEST_COMMON_GROUP_ID = uuid.uuid4()

    # Level
    TEST_LEVEL_NAME = "A1"
    TEST_LEVEL_ID = uuid.uuid4()

    # Word type
    TEST_WORD_TYPE = "TEST_TYPE"
    TEST_CUSTOM_WORD_TYPE = "CUSTOM_TYPE"
    TEST_WORD_TYPE_ID = uuid.uuid4()
    TEST_CUSTOM_WORD_TYPE_ID = uuid.uuid4()

    TEST_DESCRIPTION = "This is a test description"

    # Word
    TEST_WORD_ID = uuid.uuid4()
    TEST_WORD_DICT = [
        {'german_word' : "Hallo",
         'english_word': "Hello",
         'russian_word': "Привет"},
        {'german_word': "beantragen",
         'english_word': "apply for",
         'russian_word': "предлагать"},
        {'german_word': "der Antrag",
         'english_word': "request",
         'russian_word': "Предложение"},
        {'german_word': "einzahlen",
         'english_word': "pay",
         'russian_word': "платить"},
        {'german_word': "die Einzahlung",
         'english_word': "Deposit",
         'russian_word': "взнос,оплата"},
        {'german_word': "verdienen",
         'english_word': "earn",
         'russian_word': "зарабатывать"},
        {'german_word': "überweisen",
         'english_word': "transfer",
         'russian_word': "переводить деньги"},
        {'german_word': "wechseln",
         'english_word': "change",
         'russian_word': "менять, обменивать"},
        {'german_word': "sperren",
         'english_word': "block, lock out",
         'russian_word': "закрывать,блокировать"},
        {'german_word': "der Wechsel",
         'english_word': "the change",
         'russian_word': "изменение"},
        {'german_word': "die überweisung",
         'english_word': "the transfer",
         'russian_word': "перевод денег"},
        {'german_word': "der Verdienst",
         'english_word': "income",
         'russian_word': "заработок, заслуга"}
    ]

    TEST_WORD_DICT_MINI = [
        {'german_word': "Hallo",
         'english_word': "Hello",
         'russian_word': "Привет"},
        {'german_word': "beantragen",
         'english_word': "apply for",
         'russian_word': "предлагать"},
        {'german_word': "der Antrag",
         'english_word': "request",
         'russian_word': "Предложение"}
    ]

    TEST_WORD = {'german_word': "Hallo",
         'english_word': "Hello",
         'russian_word': "Привет"}


# --------------------FIXTURE--------------------

@pytest.fixture()
def create_test_user():
    """Create Test User Dwh Line in the beginning of test
    """
    with session_factory() as session:
        new_dwh_user = UserAddDwhDTO(
            id=DataPreparation.TEST_USER_ID,
            user_id=uuid.uuid4(),
            action=ActionDWHEnum.CREATED,
            user_name=DataPreparation.TEST_USER_NAME,
            training_length=10,
            email=DataPreparation.TEST_USER_EMAIL,
            hashed_password=DataPreparation.TEST_PASS,
            is_active=True,
            is_superuser=False,
            is_verified=True,
            telegram_user_id=DataPreparation.TEST_TELEGRAM_USER_ID,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            description=DataPreparation.TEST_DESCRIPTION
        )
        stmt = insert(UserDWH).values(**new_dwh_user.dict())
        session.execute(stmt)
        session.commit()


@pytest.fixture()
def create_test_level():
    """Create test level by TEST_LEVEL_NAME with id=TEST_LEVEL_ID """
    with session_factory() as session:
        new_level = LevelAddDwhDTO(
            lang_level=DataPreparation.TEST_LEVEL_NAME,
            id=DataPreparation.TEST_LEVEL_ID,
            level_id=uuid.uuid4(),
            action=ActionDWHEnum.CREATED,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            description=DataPreparation.TEST_DESCRIPTION
        )
        stmt = insert(LevelDWH).values(**new_level.dict())
        session.execute(stmt)
        session.commit()


@pytest.fixture()
def create_test_group():
    """Create test group for tests """
    with session_factory() as session:
        stmt = insert(GroupDWH).values(**{
            'id': DataPreparation.TEST_GROUP_ID,
            'group_id': uuid.uuid4(),
            'group_name': DataPreparation.TEST_GROUP_NAME,
            'user_id': DataPreparation.TEST_USER_ID,
            'action': ActionDWHEnum.CREATED,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'description': DataPreparation.TEST_DESCRIPTION
        })
        session.execute(stmt)
        session.commit()

@pytest.fixture()
def create_list_test_words():
    """Create tests word typy """
    with session_factory() as session:
        for word in DataPreparation.TEST_WORD_DICT:
            stmt = insert(WordDWH).values(**{
                'id': uuid.uuid4(),
                'word_id': uuid.uuid4(),
                'german_word': word.get('german_word'),
                'english_word': word.get('english_word'),
                'russian_word': word.get('russian_word'),
                'lang_level_id': DataPreparation.TEST_LEVEL_ID,
                'word_type_id': DataPreparation.TEST_WORD_TYPE_ID,
                'group_id': DataPreparation.TEST_GROUP_ID,
                'user_id': DataPreparation.TEST_USER_ID,
                'amount_already_know': 0,
                'amount_back_to_learning': 0,
                'action': ActionDWHEnum.CREATED,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            })
            session.execute(stmt)
        session.commit()


@pytest.fixture()
def create_test_word():
    """Create one test word  """
    test_word_id = DataPreparation.TEST_WORD_ID
    word = DataPreparation.TEST_WORD
    with session_factory() as session:
        stmt = insert(WordDWH).values(**{
            'id': test_word_id,
            'word_id': uuid.uuid4(),
            'german_word': word.get('german_word'),
            'english_word': word.get('english_word'),
            'russian_word': word.get('russian_word'),
            'lang_level_id': DataPreparation.TEST_LEVEL_ID,
            'word_type_id': DataPreparation.TEST_WORD_TYPE_ID,
            'group_id': DataPreparation.TEST_GROUP_ID,
            'user_id': DataPreparation.TEST_USER_ID,
            'amount_already_know': 0,
            'amount_back_to_learning': 0,
            'action': ActionDWHEnum.CREATED,
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'description':DataPreparation.TEST_DESCRIPTION
        })
        session.execute(stmt)
        session.commit()
