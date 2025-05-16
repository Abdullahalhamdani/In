
from telethon.sync import TelegramClient, events
from datetime import datetime
import asyncio
import os

# بيانات الدخول من المتغيرات البيئية
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
user_to_watch = int(os.getenv('USER_ID'))

# اسم جلسة Telethon
client = TelegramClient('session', api_id, api_hash)


async def main():
    me = await client.get_me()
    target = await client.get_entity(user_to_watch)
    print(f"بدأت مراقبة: {target.first_name} ({user_to_watch})")
    await client.send_message('me', f"تم بدء مراقبة {target.first_name} ({user_to_watch})")

    last_online = None
    while True:
        user = await client.get_entity(user_to_watch)
        status = user.status
        now = datetime.now()

        if hasattr(status, 'was_online'):
            # غير متصل حاليًا
            if last_online:
                duration = now - last_online
                message = f"انتهى اتصال {target.first_name}\nمن: {last_online.strftime('%H:%M:%S')}\nإلى: {now.strftime('%H:%M:%S')}\nالمدة: {str(duration)}"
                await client.send_message('me', message)
                last_online = None
        else:
            # متصل الآن
            if not last_online:
                last_online = now

        await asyncio.sleep(10)


with client:
    client.loop.run_until_complete(main())
