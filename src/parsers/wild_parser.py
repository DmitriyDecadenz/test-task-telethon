import httpx
from src.parsers.models import Items, Item
from src.parsers.text import PARAMS, HEADERS


class ParseWB:
    def __init__(self, url: str) -> None:
        self.url = url
        self._wb_json_data = self._get_wb_json_data()

    async def _get_wb_json_data(self) -> Items:
        response = httpx.get(self.url, params=PARAMS, headers=HEADERS)
        items_info = Items.parse_obj(response.json()["data"])
        return items_info

    async def get_products(self) -> list[Item]:
        count = 0
        product_list = []
        for products in await self._wb_json_data:
            for product in products:
                for item in product:
                    if count < 8:
                        pass
                    else:
                        if count == 18:
                            break
                        product_list.append(item)
                    count += 1
        return product_list








