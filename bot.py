import discord
import asyncio
import random
import os

TOKEN = os.getenv("TOKEN")

GUILD_ID = 1453098427461402766
VOICE_ID = 1490673130824401016

icons = [
    "🌈","✨","💫","🔥","💖","⚡","🌟","🌀","🎧","👑",
    "💎","🌸","🌙","⭐","🖤","🤍","💜","💙","💚","💛"
]

NAME = "♡𝑲𝒂𝒏𝒈 𝑾 𝑩𝒐𝒏𝒈♡"

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True


class MyBot(discord.Client):

    async def on_ready(self):
        print(f"✅ Logged in: {self.user}")

        self.guild = self.get_guild(GUILD_ID)
        self.channel = self.guild.get_channel(VOICE_ID)

        # chạy loop
        self.loop.create_task(self.voice_loop())
        self.loop.create_task(self.rename_loop())


    # 🔥 GIỮ VOICE KHÔNG RỚT
    async def voice_loop(self):
        await self.wait_until_ready()

        while not self.is_closed():
            try:
                vc = discord.utils.get(self.voice_clients, guild=self.guild)

                # nếu lỗi hoặc chưa connect → reconnect
                if not vc or not vc.is_connected():
                    if vc:
                        try:
                            await vc.disconnect(force=True)
                        except:
                            pass

                    await self.channel.connect()
                    print("🎧 Reconnected voice")

                await asyncio.sleep(10)

            except Exception as e:
                print("⚠️ Voice lỗi:", e)
                await asyncio.sleep(5)


    # 🔥 ĐỔI TÊN LIÊN TỤC (ANTI 429)
    async def rename_loop(self):
        await self.wait_until_ready()

        while not self.is_closed():
            try:
                guild = self.guild
                me = guild.get_member(self.user.id)

                icon = random.choice(icons)
                new_name = f"{icon} {NAME} {icon}"

                await me.edit(nick=new_name)

                # ⚡ delay chống block
                await asyncio.sleep(random.uniform(6, 9))

            except Exception as e:
                print("⚠️ Rename lỗi:", e)
                await asyncio.sleep(10)


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
        asyncio.sleep(5)
