from src.core.schemas import IDSchema


class RedditPublisher(IDSchema):
    photo_url: str | None
    name: str


class RedditPost(IDSchema):  # TODO: сделать базовый класс с этими параметрами (ибо у вк также)
    upvotes: int

    timestamp: int
    is_pinned: bool
    text: str

    photos_url: list[str] | None 

    publisher: RedditPublisher
