from sqlalchemy.orm import DeclarativeBase

from farm_todo.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
