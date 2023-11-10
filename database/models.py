from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Float, text


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, nullable=False, index=True, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[float] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))


class Posts(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)
    zipcode: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[float] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    price: Mapped[float] = mapped_column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("Users")
    images = relationship("Images", back_populates="product")


class Votes(Base):
    __tablename__ = "Votes"
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True,
                                         nullable=False)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True,
                                         nullable=False)


class Images(Base):
    __tablename__ = "Images"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    url: Mapped[str] = mapped_column(String, nullable=False)

    posts_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)

    product = relationship("Posts", back_populates="images")
