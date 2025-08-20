from pyrogram import Client, filters

api_id = 27748866
api_hash = "8118b3e80aa7e8fcc8cce522a15d0e3b"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

bot_username = "TenderResearchBot"
group_id = -1002419015671

@app.on_message(filters.private & filters.user(bot_username))
async def forward_message(client, message):
    await client.get_chat(group_id)
    await client.send_message(chat_id=group_id, text=message.text)

app.run()