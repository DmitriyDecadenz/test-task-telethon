from pydantic import BaseModel


class Item(BaseModel):
    brand: str
    name: str
    id: int


class Items(BaseModel):
    products: list[Item]
