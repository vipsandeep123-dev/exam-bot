import asyncio
import random
from datetime import datetime
import pytz
import os
from telegram import Bot
from telegram.constants import ParseMode

# ── CONFIG ─────────────────────────────────────────────────────────────────
BOT_TOKEN   = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
GROUP_ID    = os.environ.get("GROUP_ID",  "YOUR_GROUP_CHAT_ID_HERE")
APP_URL     = "https://the-exam.vercel.app"
TIMEZONE    = "Asia/Kolkata"  # IST

# ── AGRICULTURE FACTS ──────────────────────────────────────────────────────
AGRI_FACTS = [
    "🌾 The world's first known farmers lived in the Fertile Crescent around 10,000 BC.",
    "🌱 Rice is the staple food for more than half of the world's population.",
    "🐝 One-third of all food produced globally depends on pollination by bees.",
    "🌽 Corn (Maize) is the most widely produced grain crop in the world.",
    "🍅 Tomatoes are botanically a fruit but legally classified as a vegetable in the USA.",
    "🌿 Hybrid seeds can increase crop yield by 20-30% compared to traditional varieties.",
    "💧 Agriculture uses approximately 70% of the world's fresh water supply.",
    "🪱 One acre of healthy soil contains about 1 million earthworms.",
    "🌾 India is the world's largest producer of milk, pulses, and spices.",
    "🌱 Photosynthesis converts about 1% of solar energy into chemical energy in plants.",
    "🐄 A dairy cow produces about 90 glasses of milk per day.",
    "🌿 Nitrogen, Phosphorus, and Potassium (NPK) are the three primary plant nutrients.",
    "🌾 Wheat was one of the first crops to be cultivated, around 9600 BC.",
    "🦟 Integrated Pest Management (IPM) reduces pesticide use by up to 50%.",
    "🌱 Drip irrigation can save 30-50% water compared to flood irrigation.",
    "🧬 Gregor Mendel discovered the laws of inheritance through pea plant experiments.",
    "🌾 India produces about 22% of the world's total wheat production.",
    "🪴 Hydroponics can grow plants 50% faster than soil-based agriculture.",
    "🐓 Poultry is the fastest-growing livestock sector in India.",
    "🌿 Crop rotation helps maintain soil fertility and reduces pest pressure.",
    "🌾 The Green Revolution in India was led by Dr. M.S. Swaminathan.",
    "💧 Sprinkler irrigation is most suitable for sandy and undulating soils.",
    "🌱 Vermicompost contains 5 times more nitrogen than ordinary compost.",
    "🐝 India has about 5 species of honeybees commercially important for apiculture.",
    "🌾 Paddy requires standing water of 5-7 cm for optimal growth.",
    "🧪 pH of 6.5-7.5 is considered ideal for most agricultural crops.",
    "🌿 Allelopathy is the chemical inhibition of one plant by another.",
    "🌱 Seed dormancy can be broken by scarification, stratification, or chemicals.",
    "🐄 Murrah buffalo is the highest milk-producing buffalo breed in India.",
    "🌾 Rabi crops are sown in winter and harvested in spring — wheat, mustard, barley.",
    "🌱 Kharif crops are sown in monsoon and harvested in autumn — rice, maize, cotton.",
    "🦠 Rhizobium bacteria fix atmospheric nitrogen in legume root nodules.",
    "🌿 Hybrid vigor (Heterosis) is the superiority of F1 hybrids over parents.",
    "🌾 India has the largest area under wheat cultivation in the world.",
    "💧 Waterlogging causes anaerobic conditions harmful to most crops.",
    "🌱 Tissue culture is used to produce disease-free planting material.",
    "🐟 Pisciculture is the controlled breeding and farming of fish.",
    "🌾 Sugarcane has the highest water requirement among all field crops.",
    "🧬 Plant breeding aims to improve yield, quality, and disease resistance.",
    "🌿 Contour farming reduces soil erosion on sloping lands by up to 50%.",
    "🌾 India is the second largest producer of fruits and vegetables in the world.",
    "💧 One mm of rainfall provides 1000 litres of water per 1000 sq meters.",
    "🌱 Organic farming prohibits use of synthetic fertilizers and pesticides.",
    "🐄 Holstein Friesian is the highest milk-producing cattle breed in the world.",
    "🌾 Minimum Support Price (MSP) is announced by CCEA before each crop season.",
    "🧪 Soil organic matter improves water retention and nutrient availability.",
    "🌿 Aeroponics grows plants with roots suspended in air and misted with nutrients.",
    "🌾 India exports the most rice in the world — mainly Basmati and Non-Basmati.",
    "🦟 BT cotton contains a gene from Bacillus thuringiensis for pest resistance.",
    "🌱 Zero tillage farming conserves moisture and reduces soil disturbance.",
]

# ── MOTIVATIONAL QUOTES ────────────────────────────────────────────────────
QUOTES = [
    "Success is the sum of small efforts repeated day in and day out. 💪",
    "The harder you work for something, the greater you'll feel when you achieve it. 🎯",
    "Don't watch the clock; do what it does — keep going. ⏰",
    "Dream big, work hard, stay focused. 🌟",
    "Every expert was once a beginner. Keep learning! 📚",
    "Your only limit is your mind. Push beyond it! 🚀",
    "Consistency is the key to excellence. Show up every day! 📅",
    "One quiz at a time, one step closer to your dream. 🌾",
    "Believe in yourself — you are stronger than you think! 💫",
    "Today's preparation determines tomorrow's achievement. 📝",
]

# ── MESSAGE TEMPLATES ──────────────────────────────────────────────────────
def good_morning_msg():
    fact = random.choice(AGRI_FACTS)
    quote = random.choice(QUOTES)
    now = datetime.now(pytz.timezone(TIMEZONE))
    day = now.strftime("%A, %d %B %Y")
    return f"""🌅 *Good Morning, Champions\\!*
📅 _{day}_

{fact}

✨ *Thought of the Day:*
_{quote}_

📚 *Ready for today's quiz?*
👉 [Start Daily Quiz]({APP_URL})

Best of luck\\! 💪
— *Sandeep* 🌾"""

def quiz_reminder_msg():
    return f"""⚡ *DAILY QUIZ REMINDER\\!*

🕐 Have you taken today's quiz yet?

Don't miss your daily practice\\!
👉 [Take Quiz Now]({APP_URL})

🔥 Keep your streak alive\\!
💡 Every question makes you stronger\\!

— *THE EXAM by Sandeep* 🌾"""

def evening_msg():
    quote = random.choice(QUOTES)
    return f"""🌙 *Good Evening, Scholars\\!*

Hope you had a productive day\\! 🌟

*Evening Motivation:*
_{quote}_

📊 Check your stats and see how far you've come\\!
👉 [{APP_URL}]({APP_URL})

Rest well and come back stronger tomorrow\\! 💪
— *Sandeep* 🌾"""

def weekly_leaderboard_msg():
    return f"""🏆 *WEEKLY LEADERBOARD UPDATE\\!*

Check where you stand among your peers\\!

👉 [View Leaderboard]({APP_URL})

🥇 Keep practicing to reach the top\\!
📚 Daily quiz = Daily progress\\!

— *THE EXAM by Sandeep* 🌾"""

# ── SCHEDULER ─────────────────────────────────────────────────────────────
async def send_message(bot, text):
    try:
        await bot.send_message(
            chat_id=GROUP_ID,
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2,
            disable_web_page_preview=False
        )
        print(f"✅ Message sent at {datetime.now()}")
    except Exception as e:
        print(f"❌ Error: {e}")

async def scheduler():
    bot = Bot(token=BOT_TOKEN)
    tz  = pytz.timezone(TIMEZONE)

    print(f"🤖 Bot started! Timezone: {TIMEZONE}")
    print(f"📢 Group ID: {GROUP_ID}")

    last_run = {}  # track last run time for each job

    while True:
        now  = datetime.now(tz)
        hour = now.hour
        minute = now.minute
        weekday = now.weekday()  # 0=Monday, 6=Sunday
        day_key = now.strftime("%Y-%m-%d")

        # ── 7:00 AM — Good Morning + Agri Fact ──
        if hour == 7 and minute == 0:
            key = f"morning_{day_key}"
            if key not in last_run:
                await send_message(bot, good_morning_msg())
                last_run[key] = True

        # ── 9:00 AM — Quiz Reminder ──
        if hour == 9 and minute == 0:
            key = f"quiz_{day_key}"
            if key not in last_run:
                await send_message(bot, quiz_reminder_msg())
                last_run[key] = True

        # ── 8:00 PM — Evening Message ──
        if hour == 20 and minute == 0:
            key = f"evening_{day_key}"
            if key not in last_run:
                await send_message(bot, evening_msg())
                last_run[key] = True

        # ── Sunday 9:00 AM — Weekly Leaderboard ──
        if weekday == 6 and hour == 9 and minute == 0:
            key = f"leaderboard_{day_key}"
            if key not in last_run:
                await send_message(bot, weekly_leaderboard_msg())
                last_run[key] = True

        # Clean old keys (keep only last 2 days)
        if len(last_run) > 20:
            last_run = {}

        await asyncio.sleep(60)  # check every minute

if __name__ == "__main__":
    asyncio.run(scheduler())
