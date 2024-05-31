from pydantic import BaseModel, root_validator, model_validator


class Item(BaseModel):
    brand: str
    name: str
    id: int

    # @model_validator(mode='after')
    # def create_url(self, values):
    #     self.brand = f'https://www.wildberries.ru/catalog/{self.id}/detail.aspx'


class Items(BaseModel):
    products: list[Item]
