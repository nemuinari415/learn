from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Text, Uuid, Date, ForeignKey, DateTime
import uuid
from datetime import date, datetime
from zoneinfo import ZoneInfo


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        unique=True,
    )
    birthday: Mapped[date] = mapped_column(
        Date,
        nullable=True,
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )
    title: Mapped[str] = mapped_column(Text, nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(ZoneInfo("Asia/Tokyo")),
        onupdate=lambda: datetime.now(ZoneInfo("Asia/Tokyo")),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )
