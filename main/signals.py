from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registration
import telebot

# Telegram bot tokenini kiriting
BOT_TOKEN = '7830967987:AAEKpjGJeahHuXbEvB3jvbkDBJDjcYC-G9E'
CHAT_ID = [5021533207,2012841132, 6812505344]
bot = telebot.TeleBot(BOT_TOKEN)

@receiver(post_save, sender=Registration)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:  # Faqat yangi yaratilgan model uchun ishlaydi
        # course_name = instance.course.name if instance.course else "No Course"
        # message = f"New Registration Created:\n\nCourse: {course_name}\nName: {instance.name}\nPhone: {instance.phone}"
        # for i in CHAT_ID:
        #     bot.send_message(i, message)

        if instance.course:
            message = f"Assalomu alaykum bizda yangi o'quvchi bor :\nIsmi : {instance.name}\nTelefon raqami : {instance.phone}\nKursi :{instance.course.course.name}\nKurs yo'nalishi : {instance.course.name}"
            for i in CHAT_ID:
                bot.send_message(i, message)
        else:
            message = f"Assalomu alaykum bizda yangi o'quvchi bor :\nIsmi : {instance.name}\nTelefon raqami : {instance.phone}"
            for i in CHAT_ID:
                bot.send_message(i, message)

