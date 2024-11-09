from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registration
import telebot
import os
from dotenv import load_dotenv

# .env fayldan TOKEN va CHAT_ID larni yuklash
load_dotenv()
BOT_TOKEN = '7830967987:AAEKpjGJeahHuXbEvB3jvbkDBJDjcYC-G9E'
CHAT_IDS = [5021533207, 2012841132, 6812505344]

bot = telebot.TeleBot(BOT_TOKEN)

def send_telegram_message(chat_ids, message):
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id, message)
        except Exception as e:
            print(f"Xabar yuborishda xato: {e}")

@receiver(post_save, sender=Registration)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        if instance.course:
            message = (
                f"⚡️Assalomu alaykum bizda yangi o'quvch bor:\n"
                f"👉 Ismi: {instance.name}\n"
                f"Telefon raqami: {instance.phone}\n"
                f"🌐 Kursi: {instance.course.course.name}\n"
                f"📃 Kurs yo'nalishi: {instance.course.name}"
            )
        else:
            message = (
                f"⚡️Assalomu alaykum bizda yangi o'quvch bor:\n"
                f"👉 Ismi: {instance.name}\n"
                f"📲 Telefon raqami: {instance.phone}"
            )
        send_telegram_message(CHAT_IDS, message)


