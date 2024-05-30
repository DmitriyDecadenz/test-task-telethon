from fastapi import FastAPI, File, UploadFile, HTTPException, status
from src.tg_api.tele_api import client, get_data_from_tg

app = FastAPI()


@app.post("/login")
async def login() -> list:
    return await get_data_from_tg(client)


@app.get("/check/login/{phone_number}")
async def check_login(
        phone_number: str,
) -> dict:
    if client.is_connected() is True:
        return {"status": "ok"}
    return {"status": "bad"}


@app.get("/messages/{phone_number}/{username}")
async def get_messages(
        phone_number: str,
        username: str,
) -> list:
    msg_list = []
    count = 0
    try:
        async for message in client.iter_messages(username):
            count += 1
            if count == 50:
                break
            msg_list.append(message)
    except ConnectionError:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return msg_list

#     print(message.id, message.text)
#


@app.get("/messages/send")
async def send_messages(
        messages: str,
        from_phone: str = None,
        username: str = None,
):
    try:
        if from_phone is None:
            await client.send_message(username, messages)
        await client.send_message(from_phone, messages)
    except ConnectionError:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.get("/messages/send/file")
async def send_file(
        from_phone: str = None,
        username: str = None,
        file: UploadFile = File(...)
) -> dict:
    contents = await file.read()
    try:
        if from_phone is None:
            await client.send_file(username, contents)
            return {"status": "ok"}
        await client.send_file(from_phone, contents)
        return {"status": "ok"}
    except ConnectionError:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


if __name__ == '__main__':
    client.loop.run_until_complete(get_data_from_tg(client=client))
