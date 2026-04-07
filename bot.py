import discord
import asyncio
import random
import os

TOKEN = os.getenv("TOKEN")

GUILD_ID = 1453098427461402766   # 👉 ID server
VOICE_ID = 1490673130824401016   # 👉 ID room voice

icons = [
    "🌈","✨","💫","🔥","💖","⚡","🌟","🌀","🎧","👑",
    "💎","🌸","🌙","⭐","🖤","🤍","💜","💙","💚","💛"
]

NAME = "𝑲𝒂𝒏𝒈 𝑾 𝑩𝒐𝒏𝒈 ♡"

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

class MyBot(discord.Client):
    async def on_ready(self):
        print(f"✅ Logged in: {self.user}")

        guild = self.get_guild(GUILD_ID)
        channel = guild.get_channel(VOICE_ID)

        # 🎧 vào voice
        try:
            await channel.connect()
            print("🎧 Joined voice")
        except:
            print("⚠️ đã ở trong voice hoặc lỗi connect")

        # chạy loop đổi tên
        self.loop.create_task(self.rename_loop(guild))

    async def rename_loop(self, guild):
        await self.wait_until_ready()
        me = guild.get_member(self.user.id)

        while True:
            try:
                icon = random.choice(icons)
                new_name = f"{icon} {NAME} {icon}"

                await me.edit(nick=new_name)

                # ⚡ delay chuẩn né block
                await asyncio.sleep(random.uniform(2.6, 3.3))

            except Exception as e:
                print("⚠️ Rename lỗi:", e)

                # nếu bị chặn thì nghỉ ngắn thôi
                await asyncio.sleep(5)

bot = MyBot(intents=intents)

while True:
    try:
        if not TOKEN:
            print("❌ thiếu TOKEN")
        else:
            print("🚀 Bot đang chạy...")
            bot.run(TOKEN)
    except Exception as e:
        print("💥 Crash, restart:", e)
