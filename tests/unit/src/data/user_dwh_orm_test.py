import datetime
import uuid

from sqlalchemy import select

from src.data.user_dwh_orm import UserDwhOrm
from src.db.database import session_factory
from src.dto.schema import UserAddDwhDTO
from src.model.action_dwh_enum import ActionDWHEnum
from src.model.user_dwh import UserDWH
from tests.unit.test_data_preparation import DataPreparation, create_test_user


class TestUserDwhOrm():

    def test_create_dwh_user(self):
        user_id_data = uuid.uuid4()
        # Prepare Data
        test_user_dto=UserAddDwhDTO(
            id=DataPreparation.TEST_USER_ID,
            user_id=user_id_data,
            action=ActionDWHEnum.CREATED,
            user_name=DataPreparation.TEST_USER_NAME,
            training_length=10,
            email=DataPreparation.TEST_USER_EMAIL,
            hashed_password=DataPreparation.TEST_PASS,
            is_active=True,
            is_superuser=False,
            is_verified=True,
            telegram_user_id=DataPreparation.TEST_TELEGRAM_USER_ID,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            description=DataPreparation.TEST_DESCRIPTION
            )
        # Do test
        UserDwhOrm.create_dwh_user(test_user_dto)

        # Check results
        with session_factory() as session:
            user = session.execute(
                select(UserDWH)
            ).scalar_one_or_none()
            assert user.id == DataPreparation.TEST_USER_ID
            assert user.user_id == user_id_data
            assert user.user_name == DataPreparation.TEST_USER_NAME
            assert user.training_length == 10
            assert user.hashed_password == DataPreparation.TEST_PASS
            assert user.is_active is True
            assert user.is_superuser is False
            assert user.is_verified is True
            assert user.telegram_user_id == DataPreparation.TEST_TELEGRAM_USER_ID
            assert user.action == ActionDWHEnum.CREATED
            assert user.description == DataPreparation.TEST_DESCRIPTION
            assert user.created_dwh_at is not None
            assert user.updated_dwh_at is not None

    def test_get_user_by_id(self, create_test_user):

        # Do test
        user = UserDwhOrm.get_user_by_id(DataPreparation.TEST_USER_ID)

        # Check results
        assert user.user_name == DataPreparation.TEST_USER_NAME
        assert user.training_length == 10
        assert user.hashed_password == DataPreparation.TEST_PASS
        assert user.is_active is True
        assert user.is_superuser is False
        assert user.is_verified is True
        assert user.telegram_user_id == DataPreparation.TEST_TELEGRAM_USER_ID
        assert user.action == ActionDWHEnum.CREATED
        assert user.description == DataPreparation.TEST_DESCRIPTION


    def test_delete_user(self, create_test_user):
        # Do test
        res = UserDwhOrm.delete_user(DataPreparation.TEST_USER_ID)

        # Check results
        assert res is True
        with session_factory() as session:
            user = session.execute(
                select(UserDWH)
            ).scalar_one_or_none()
            assert user is None