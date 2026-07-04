from enum import Enum
from uuid import UUID as UUIDType, uuid4

from sqlalchemy import DateTime, String, func
from sqlalchemy import Enum as SQLenum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class UserRole(str, Enum):
    HR = ("hr",)
    FINANCE = ("finance",)
    LEGAL = ("legal",)
    CEO = ("ceo",)
    EMPLOYEE = "employee"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUIDType] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name: Mapped[str] = mapped_column(String, nullable=False)

    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    role: Mapped[UserRole] = mapped_column(
        SQLenum(UserRole, name="user_role"), nullable=False, default=UserRole.EMPLOYEE
    )

    created_At: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    last_login_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
