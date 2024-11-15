# Generated by Django 4.2.7 on 2024-11-09 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_bannerimage_options_alter_logo_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutachievements',
            options={'verbose_name': 'Haqimizda sahifasi malumotlari', 'verbose_name_plural': 'Haqimizda sahifasi malumotlari'},
        ),
        migrations.AlterModelOptions(
            name='aboutowner',
            options={'verbose_name': 'Direktor haqida', 'verbose_name_plural': 'Direktor haqida'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner', 'verbose_name_plural': 'Banner'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Kurs', 'verbose_name_plural': 'Kurslar'},
        ),
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name': 'Kurs kategoriyasi', 'verbose_name_plural': 'Kurs kategoriyasi'},
        ),
        migrations.AlterModelOptions(
            name='courselevel',
            options={'verbose_name': 'Kurs darajasi', 'verbose_name_plural': 'Kurs darajalari'},
        ),
        migrations.AlterModelOptions(
            name='courselevelfields',
            options={'verbose_name': "Kurs darajasi ma'lumoti ", 'verbose_name_plural': "Kurs darajasi ma'lumotlari"},
        ),
        migrations.AlterModelOptions(
            name='homeachievements',
            options={'verbose_name': "Asosiy sahifa yutuqlari ma'lumoti", 'verbose_name_plural': "Asosiy sahifa yutuqlari ma'lumotlari"},
        ),
        migrations.AlterModelOptions(
            name='registration',
            options={'verbose_name': "Ro'yhatdan o'tish arizalari", 'verbose_name_plural': "Ro'yhatdan o'tish arizalari"},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': 'Natijalar', 'verbose_name_plural': 'Natijalar'},
        ),
        migrations.AlterField(
            model_name='aboutachievements',
            name='results',
            field=models.IntegerField(default=0, verbose_name='Natijalar'),
        ),
        migrations.AlterField(
            model_name='aboutachievements',
            name='students',
            field=models.IntegerField(default=0, verbose_name="O'quvchilar"),
        ),
        migrations.AlterField(
            model_name='aboutachievements',
            name='teachers',
            field=models.IntegerField(default=0, verbose_name="O'qituvchilar"),
        ),
        migrations.AlterField(
            model_name='aboutowner',
            name='full_name',
            field=models.CharField(max_length=300, verbose_name="To'liq ism familiyasi"),
        ),
        migrations.AlterField(
            model_name='aboutowner',
            name='image',
            field=models.ImageField(upload_to='owner_image/', verbose_name='Rasmi'),
        ),
        migrations.AlterField(
            model_name='aboutowner',
            name='info',
            field=models.TextField(verbose_name='Biografiyasi'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Tavsifi'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.coursecategory', verbose_name='Kurs kategoiryasi'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Kurs tavsifi'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course_photo/', verbose_name='Kurs rasmi'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Kurs nomi'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_full_name',
            field=models.CharField(max_length=255, verbose_name="O'qituvchi ism famuliyasi"),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Kurs sarlavhasi'),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Kurs kategoriyasi nomi'),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course', verbose_name='Darajaga tegishli kurs'),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='fields',
            field=models.ManyToManyField(to='main.courselevelfields', verbose_name="Kurs darajasi ma'lumotlari"),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='image',
            field=models.ImageField(upload_to='level_images/', verbose_name='Kurs darajasi rasmi'),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Kurs darajasi nomi'),
        ),
        migrations.AlterField(
            model_name='courselevelfields',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Kurs darajasi malumoti nomi'),
        ),
        migrations.AlterField(
            model_name='homeachievements',
            name='results',
            field=models.IntegerField(default=0, verbose_name='Natijalar'),
        ),
        migrations.AlterField(
            model_name='homeachievements',
            name='students',
            field=models.IntegerField(default=0, verbose_name="O'quvchilar"),
        ),
        migrations.AlterField(
            model_name='homeachievements',
            name='teachers',
            field=models.IntegerField(default=0, verbose_name="O'qituvchilar"),
        ),
        migrations.AlterField(
            model_name='registration',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.courselevel', verbose_name='Kursi'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ariza holati'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Arizachi ismi'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Arizachi Telefon raqami'),
        ),
    ]
