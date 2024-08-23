import datetime
import uuid

from sqlalchemy import select

from src.data.group_dwh_orm import GroupDwhOrm
from src.db.database import session_factory
from src.dto.schema import GroupAddDwhDTO
from src.model.action_dwh_enum import ActionDWHEnum
from src.model.group_dwh import GroupDWH
from tests.unit.test_data_preparation import (DataPreparation, create_test_group)

class TestGroupDwhOrm():

    def test_create_dwh_group(self):
        group_id = uuid.uuid4()
        # Prepare Data
        test_group_dto = GroupAddDwhDTO(
            id=DataPreparation.TEST_GROUP_ID,
            group_id=group_id,
            action=ActionDWHEnum.CREATED,
            group_name=DataPreparation.TEST_GROUP_NAME,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            description=DataPreparation.TEST_DESCRIPTION,
            user_id=DataPreparation.TEST_USER_ID
        )

        # Do test
        GroupDwhOrm.create_dwh_group(test_group_dto)

        # Check results
        with session_factory() as session:
            group = session.execute(
                select(GroupDWH)
            ).scalar_one_or_none()
            assert group.id == DataPreparation.TEST_GROUP_ID
            assert group.group_id == group_id
            assert group.group_name == DataPreparation.TEST_GROUP_NAME
            assert group.action == ActionDWHEnum.CREATED
            assert group.description == DataPreparation.TEST_DESCRIPTION
            assert group.created_dwh_at is not None
            assert group.updated_dwh_at is not None

    def test_get_group_by_id(self, create_test_group):

        # Do test
        group = GroupDwhOrm.get_group_by_id(DataPreparation.TEST_GROUP_ID)

        # Check results
        assert group.group_name == DataPreparation.TEST_GROUP_NAME
        assert group.action == ActionDWHEnum.CREATED
        assert group.description == DataPreparation.TEST_DESCRIPTION


    def test_delete_group(self, create_test_group):

        # Do test
        res = GroupDwhOrm.delete_group(DataPreparation.TEST_GROUP_ID)

        # Check results
        assert res is True
        with session_factory() as session:
            group = session.execute(
                select(GroupDWH)
            ).scalar_one_or_none()
            assert group is None

