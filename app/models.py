import enum

from app.database import Base
from sqlalchemy import BigInteger, Column, Enum, Integer


class Status(enum.Enum):
    success = "success"
    pending = "pending"


class Fibonacci(Base):
    __tablename__ = "fibonacci"

    id = Column(Integer, primary_key=True, index=True)
    n = Column(Integer, unique=True)
    nth = Column(BigInteger, nullable=True)
    status = Column(Enum(Status), nullable=False, server_default=Status.pending.value)
