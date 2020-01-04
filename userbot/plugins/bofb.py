import asyncio
from userbot.utils import admin_cmd
@borg.on(admin_cmd("bofb"))
m = await event.client.send_message("@botfather","/token")
await asyncio.sleep(5)
hs = await event.client.get_messages(entity="@botfather", limit=1, reverse=False)
await m.reply("/cancel")
h = hs[0]
bot_lists = h.reply_markup.rows
# /952952/4723940
bot_names = [user_name.text for bot_list in bot_lists for user_name in bot_list.buttons]
print(bot_names)
