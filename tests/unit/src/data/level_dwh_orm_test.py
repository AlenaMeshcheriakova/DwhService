import datetime
import uuid

from sqlalchemy import select

from src.data.level_dwh_orm import LevelDwhOrm
from src.db.database import session_factory
from src.dto.schema import LevelAddDwhDTO
from src.model.action_dwh_enum import ActionDWHEnum
from src.model.level_dwh import LevelDWH
from tests.unit.test_data_preparation import DataPreparation, create_test_level


class TestLevelDwhOrm():

    def test_create_dwh_level(self):
        # Prepare Data
        level_id = uuid.uuid4()
        test_level_dto = LevelAddDwhDTO(
            id=DataPreparation.TEST_LEVEL_ID,
            level_id=level_id,
            action=ActionDWHEnum.CREATED,
            lang_level=DataPreparation.TEST_LEVEL_NAME,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            description=DataPreparation.TEST_DESCRIPTION,
        )

        # Do test
        LevelDwhOrm.create_dwh_level(test_level_dto)

        # Check results
        with session_factory() as session:
            level = session.execute(
                select(LevelDWH)
            ).scalar_one_or_none()
            assert level.id == DataPreparation.TEST_LEVEL_ID
            assert level.level_id == level_id
            assert level.lang_level == DataPreparation.TEST_LEVEL_NAME
            assert level.action == ActionDWHEnum.CREATED
            assert level.description == DataPreparation.TEST_DESCRIPTION
            assert level.created_dwh_at is not None
            assert level.updated_dwh_at is not None

    def test_get_level_by_id(self, create_test_level):

        # Do test
        level = LevelDwhOrm.get_level_by_id(DataPreparation.TEST_LEVEL_ID)

        # Check results
        assert level.lang_level == DataPreparation.TEST_LEVEL_NAME
        assert level.action == ActionDWHEnum.CREATED
        assert level.description == DataPreparation.TEST_DESCRIPTION


    def test_delete_level(self, create_test_level):
        # Do test
        res = LevelDwhOrm.delete_level(DataPreparation.TEST_LEVEL_ID)

        # Check results
        assert res is True
        with session_factory() as session:
            level = session.execute(
                select(LevelDWH)
            ).scalar_one_or_none()
            assert level is None