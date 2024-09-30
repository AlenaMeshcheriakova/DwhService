import uuid
from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.exc import NoResultFound
from src.db.database import session_factory
from src.dto.schema import WordAddDwhDTO, WordDwhDTO
from src.log.logger import log_decorator, logger
from src.model.word_dwh import WordDWH


class WordDwhOrm:

    @staticmethod
    @log_decorator(my_logger=logger)
    def create_dwh_word(new_word: WordAddDwhDTO):
        with session_factory() as session:
            stmt = insert(WordDWH).values(**new_word.dict())
            session.execute(stmt)
            session.commit()

    @staticmethod
    @log_decorator(my_logger=logger)
    def get_word_by_id(word_id: uuid.UUID) -> Optional[WordDwhDTO]:
        try:
            with session_factory() as session:
                word = session.execute(
                    select(WordDWH).filter_by(id=word_id)
                ).scalar_one_or_none()
                if word:
                    word_dto = WordDwhDTO(
                        word_id=word.word_id,
                        action=word.action,
                        german_word=word.german_word,
                        english_word=word.english_word,
                        russian_word=word.russian_word,
                        lang_level_id=word.lang_level_id,
                        word_type_id=word.word_type_id,
                        group_id=word.group_id,
                        user_id=word.user_id,
                        amount_already_know=word.amount_already_know,
                        amount_back_to_learning=word.amount_back_to_learning,
                        created_at=word.created_at,
                        updated_at=word.updated_at,
                        description=word.description
                    )
                    return word_dto
                else:
                    raise NoResultFound(f"Word with id {word_id} was not found")
        except NoResultFound:
            return None

    @staticmethod
    @log_decorator(my_logger=logger)
    def delete_word(word_id: uuid.UUID) -> bool:
        """
        Delete object by table id, not by Word ID from original table
        :param word_id: Unique id in table WordDWH
        :return: Bool (True if object was successfully deleted)
        """
        with session_factory() as session:
            word = session.execute(
                select(WordDWH).filter_by(id=word_id)
            ).scalar_one_or_none()
            if word:
                session.delete(word)
                session.commit()
                return True
            return False
