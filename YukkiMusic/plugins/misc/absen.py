from YukkiMusic import userbot
from pyrogram import filters, types, Client


@userbot.on_message(filters.command("absen", prefixes=list(".,-;=")))
async def absen_(c: Client, m: types.Message):
    me = await c.get_me()
    await m.reply(f"{me.first_name} Hadir!")
