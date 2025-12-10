from pydantic import BaseModel, ConfigDict
import datetime


class AuthorBase(BaseModel):
    name: str
    bio: str | None = None


class AuthorCreate(AuthorBase):
    pass


class BookInAuthor(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str


class Author(AuthorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    books: list[BookInAuthor] = []


class BookBase(BaseModel):
    title: str
    summary: str | None = None
    publication_date: datetime.date | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author_id: int



