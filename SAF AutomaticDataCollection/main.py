from telethon import TelegramClient

api_id = 39533424
api_hash = "2ddb7ea287d91744c2ae2aab318c0bf6"

client = TelegramClient("test_session",api_id,api_hash)

async def main():
    await client.start()

    channel = "https://t.me/rangoonscoutnetwork"

    async for message in client.iter_messages(channel, limit=5):
        print("--------")
        print("ID:",message.id)
        print("DATE:",message.date)
        print("TEXT:",message.text)

with client:
    client.loop.run_until_complete(main())