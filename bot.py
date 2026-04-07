import discord
from discord.ext import commands
import os
import asyncio

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# ✨ chữ đẹp giữ nguyên
base_text = "𝑲𝒂𝒏𝒈 𝑾 𝑩𝒐𝒏𝒈 ♡"

# 🌈 icon siêu nhiều
icons = [
    "🌈","✨","💫","🔥","💖","⚡","🌟","🌀","🎧","👑",
    "💎","🌸","🌺","🍀","🌙","☀️","⭐","🌻","🎶","🖤",
    "🤍","💜","💙","💚","💛","🧡","❤️","💥","🎀","🧸",
    "🦋","🐉","🍓","🍒","🥀","🌼","🌊","☁️","🧿","🔮"
]

def generate_frames(text):
    frames = []
    for icon in icons:
        frames.append(f"{icon} {text} {icon}")
    return frames

@bot.event
async def on_ready():
    print(f"✅ Logged in: {bot.user}")

    await asyncio.sleep(5)

    channel_id = 1490673130824401016
    channel = bot.get_channel(channel_id)

    # 🎧 vào voice
    if channel:
        while True:
            try:
                vc = await channel.connect(timeout=60, reconnect=True)
                await vc.guild.change_voice_state(
                    channel=channel,
                    self_mute=True,
                    self_deaf=True
                )
                print("🎧 Joined voice")
                break
            except Exception as e:
                print("❌ Voice error:", e)
                await asyncio.sleep(5)

    guild = bot.guilds[0]
    me = guild.me

    frames = generate_frames(base_text)

    while True:
        try:
            for frame in frames:
                await me.edit(nick=frame)
                await asyncio.sleep(0.8)  # ⚡ nhanh hơn
        except Exception as e:
            print("❌ Rename error:", e)
            await asyncio.sleep(5)

# 🔥 chống crash
while True:
    try:
        if not TOKEN:
            print("❌ Missing TOKEN")
        else:
            print("🚀 Running bot...")
            bot.run(TOKEN)
    except Exception as e:
        print("💥 Crash, restarting:", e)
