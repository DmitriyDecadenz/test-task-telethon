from fastapi import FastAPI, File, UploadFile, HTTPException, status
from src.parsers.text import URL
from src.parsers.wild_parser import ParseWB
from src.tg_api.tele_api import AuthTG
from telethon import TelegramClient
from src.env import API_ID, API_HASH

api_id = API_ID
api_hash = API_HASH
app = FastAPI()
tg_client = AuthTG(client=TelegramClient('aa', api_id, api_hash))


@app.post("/login")
async def login(
        phone_number: str,
        password: str,
) -> dict:
    await tg_client.take_phone(phone_number)
    await tg_client.take_password(password)
    await tg_client.send_code(phone_number=phone_number)
    return status.HTTP_200_OK


@app.post("/login/authorize")
async def authorize(
        code: str
) -> dict:
    await tg_client.take_tg_code(code)
    await tg_client.tg_user()

    return status.HTTP_200_OK


@app.get("/check/login")
async def check_login(
        phone_number: str,
):
    if await tg_client.client.is_user_authorized() is True:
        return status.HTTP_200_OK
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authorize')


@app.get("/messages/{phone_number}/{username}")
async def get_messages(
        username: str,
) -> list:
    msg_list = []
    count = 0
    try:
        async for message in tg_client.client.iter_messages(username):
            count += 1
            if count == 50:
                break
            msg_list.append(message)
        return msg_list
    except ConnectionError:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.get("/messages/send")
async def send_messages(
        messages: str,
        from_phone: str = None,
        username: str = None,
):
    try:
        if from_phone is None:
            await tg_client.client.send_message(username, messages)
        await tg_client.client.send_message(from_phone, messages)
    except ConnectionError:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authorize')


@app.post("/messages/send/file")
async def send_file(
        username: str = None,
        file: UploadFile = File(...)
):
    contents = await file.read()
    try:
        await tg_client.client.send_file(username, contents)
        return status.HTTP_200_OK

    except:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/wild/any-product")
async def get_wb_data() -> list:
    product_list = []
    for product in await ParseWB(URL).get_products():
        product = product.model_dump()
        product["url"] = f'https://www.wildberries.ru/catalog/{product["id"]}/detail.aspx'
        product_list.append(product)
    return product_list
