from telethon.errors.rpcerrorlist import SessionPasswordNeededError
from telethon import TelegramClient
from qrcode import QRCode

qr = QRCode()

# Remember to use your own values from my.telegram.org!


def gen_qr(token: str):
    qr.clear()
    qr.add_data(token)
    qr.print_ascii()
    var = qr.data_list
    return var
def display_url_as_qr(url):
    print(url)  # do whatever to show url as a qr to the user
    gen_qr(url)


async def get_data_from_tg(client: TelegramClient):
    if not client.is_connected():
        await client.connect()
    await client.connect()
    qr_login = await client.qr_login()
    print(client.is_connected())

    display_url_as_qr(qr_login.url)
    # Important! You need to wait for the login to complete!
    await qr_login.wait(50)

    me = await client.get_me()
    print('!!!!!', client.is_connected())
    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())
    return gen_qr()
    # # When you print something, you see a representation of it.
    # # You can access all attributes of Telegram objects with
    # # the dot operator. For example, to get the username:
    # username = me.username
    # print(username)
    # print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)
    #
    # # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # # ...to some chat ID
    # await client.send_message('+79649910610', 'I love, ny hot bitch')
    # ...to your contacts
    # await client.send_message('+34600123123', 'Hello, friend!')
    # # ...or even to any username
    # await client.send_message('username', 'Testing Telethon!')

    # # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )

    # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)
    #
    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/decadenz/Pictures/photo_2024-05-28_01-00-30.jpg')

    # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)
    #
    #     # You can download media from messages, too!
    #     # The method will return the path where the file was saved.
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

#
api_id = 21921020
api_hash = '31938aa34bf7bd88fea9fbfaaff6834d'
client = TelegramClient('anon', api_id, api_hash)
# client.loop.run_until_complete(get_data_from_tg(client=client))
