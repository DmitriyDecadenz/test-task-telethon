from telethon import TelegramClient
import asyncio


class AuthTG:

    def __init__(self, client: TelegramClient = None) -> None:
        self.api_id = 21921020
        self.api_hash = '31938aa34bf7bd88fea9fbfaaff6834d'
        self.client = client
        self.phone_number = None
        self.password = None
        self.code = None

    async def tg_user(self) -> None:
        self.client.start(phone=self.phone_number, password=self.password, code_callback=self.code)

    async def take_tg_code(self, code: str) -> str:
        self.code = code
        return code

    async def take_phone(self, phone_number: str) -> str:
        self.phone_number = phone_number
        return phone_number

    async def take_password(self, password: str) -> str:
        self.password = password
        return password

    async def send_code(self, phone_number):
        await self.client.connect()
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(phone_number)
    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # me = await client.get_me()
    # print(me.stringify())
    #
    # # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.text)

# asyncio.run(main())
