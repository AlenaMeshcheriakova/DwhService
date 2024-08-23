import uuid
from datetime import datetime

from sqlalchemy import select

from src.data.word_dwh_orm import WordDwhOrm
from src.db.database import session_factory
from src.dto.schema import WordAddDwhDTO
from src.model.action_dwh_enum import ActionDWHEnum
from src.model.word_dwh import WordDWH
from tests.unit.test_data_preparation import DataPreparation, create_test_word


class TestWordDwhOrm():

    def test_create_dwh_word(self):
        test_word_id = uuid.uuid4()
        test_data_word = DataPreparation.TEST_WORD
        # Prepare Data
        test_word_dto=WordAddDwhDTO(
            id=DataPreparation.TEST_WORD_ID,
            word_id=test_word_id,
            german_word=test_data_word.get('german_word'),
            english_word=test_data_word.get('english_word'),
            russian_word=test_data_word.get('russian_word'),
            lang_level_id=DataPreparation.TEST_LEVEL_ID,
            word_type_id=DataPreparation.TEST_WORD_TYPE_ID,
            group_id=DataPreparation.TEST_GROUP_ID,
            user_id=DataPreparation.TEST_USER_ID,
            amount_already_know= 0,
            amount_back_to_learning= 0,
            action=ActionDWHEnum.CREATED,
            created_at= datetime.now(),
            updated_at=datetime.now(),
            description=DataPreparation.TEST_DESCRIPTION
        )
        # Do test
        WordDwhOrm.create_dwh_word(test_word_dto)

        # Check results
        with session_factory() as session:
            word = session.execute(
                select(WordDWH)
            ).scalar_one_or_none()
            assert word.word_id == test_word_id
            assert word.german_word == test_data_word.get('german_word')
            assert word.english_word == test_data_word.get('english_word')
            assert word.russian_word == test_data_word.get('russian_word')
            assert word.lang_level_id == DataPreparation.TEST_LEVEL_ID
            assert word.word_type_id == DataPreparation.TEST_WORD_TYPE_ID
            assert word.group_id == DataPreparation.TEST_GROUP_ID
            assert word.user_id == DataPreparation.TEST_USER_ID
            assert word.amount_already_know == 0
            assert word.amount_back_to_learning == 0
            assert word.action == ActionDWHEnum.CREATED
            assert word.description == DataPreparation.TEST_DESCRIPTION

    def test_get_word_by_id(self, create_test_word):
        test_data_word = DataPreparation.TEST_WORD
        # Do test
        word = WordDwhOrm.get_word_by_id(DataPreparation.TEST_WORD_ID)

        # Check results
        assert word.german_word == test_data_word.get('german_word')
        assert word.english_word == test_data_word.get('english_word')
        assert word.russian_word == test_data_word.get('russian_word')
        assert word.lang_level_id == DataPreparation.TEST_LEVEL_ID
        assert word.word_type_id == DataPreparation.TEST_WORD_TYPE_ID
        assert word.group_id == DataPreparation.TEST_GROUP_ID
        assert word.user_id == DataPreparation.TEST_USER_ID
        assert word.amount_already_know == 0
        assert word.amount_back_to_learning == 0
        assert word.action == ActionDWHEnum.CREATED
        assert word.description == DataPreparation.TEST_DESCRIPTION


    def test_delete_user(self, create_test_word):
        # Do test
        res = WordDwhOrm.delete_word(DataPreparation.TEST_WORD_ID)

        # Check results
        assert res is True
        with session_factory() as session:
            word = session.execute(
                select(WordDWH)
            ).scalar_one_or_none()
            assert word is None