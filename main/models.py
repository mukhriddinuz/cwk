from django.db import models


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name='logo')

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logo lar"


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_image/', verbose_name='banner rasmi')

    def __str__(self):
        return f"Banner Image ID: {self.image}"

    class Meta:
        verbose_name = "Banner rasmlari"
        verbose_name_plural = "Banner rasmlari"


class Banner(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    description = models.CharField(max_length=255, verbose_name='Tavsifi')
    images = models.ManyToManyField(to=BannerImage)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"


class CourseCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kurs kategoriyasi nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs kategoriyasi"
        verbose_name_plural = "Kurs kategoriyasi"


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kurs nomi')
    teacher_full_name = models.CharField(max_length=255, verbose_name="O'qituvchi ism familiyasi")
    title = models.CharField(max_length=255, verbose_name='Kurs sarlavhasi')
    description = models.TextField(verbose_name="Kurs tavsifi")
    image = models.ImageField(upload_to='course_photo/', verbose_name='Kurs rasmi')
    category = models.ForeignKey(to=CourseCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Kurs kategoiryasi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class CourseLevelFields(models.Model):
    name = models.CharField(max_length=255, verbose_name='Kurs darajasi malumoti nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs darajasi ma'lumoti "
        verbose_name_plural = "Kurs darajasi ma'lumotlari"


class CourseLevel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kurs darajasi nomi")
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name="Darajaga tegishli kurs")
    fields = models.ManyToManyField(to=CourseLevelFields, verbose_name='Kurs darajasi ma\'lumotlari')
    image = models.ImageField(upload_to='level_images/', verbose_name='Kurs darajasi rasmi')

    def __str__(self):
        return f"{self.name} - {self.course.name}"

    class Meta:
        verbose_name = 'Kurs darajasi'
        verbose_name_plural = 'Kurs darajalari'


class HomeAchievements(models.Model):
    students = models.IntegerField(default=0, verbose_name='O\'quvchilar')
    results = models.IntegerField(default=0, verbose_name='Natijalar')
    teachers = models.IntegerField(default=0, verbose_name='O\'qituvchilar')

    def __str__(self):
        return f"Achievements: {self.students} students, {self.results} results, {self.teachers} teachers"

    class Meta:
        verbose_name = 'Asosiy sahifa yutuqlari ma\'lumoti'
        verbose_name_plural = 'Asosiy sahifa yutuqlari ma\'lumotlari'


class Result(models.Model):
    image = models.ImageField(upload_to='results/')

    class Meta:
        verbose_name = 'Natijalar'
        verbose_name_plural = 'Natijalar'


class Registration(models.Model):
    course = models.ForeignKey(to=CourseLevel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Kursi')
    name = models.CharField(max_length=255, verbose_name="Arizachi ismi")
    phone = models.CharField(max_length=50, verbose_name="Arizachi Telefon raqami")
    is_active = models.BooleanField(default=False, verbose_name="Ariza holati")

    def __str__(self):
        return f"{self.course.name if self.course else 'No Course'} - {self.name}"

    class Meta:
        verbose_name = "Ro'yhatdan o'tish arizalari"
        verbose_name_plural = 'Ro\'yhatdan o\'tish arizalari'


class AboutOwner(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='To\'liq ism familiyasi')
    info = models.TextField(verbose_name='Biografiyasi')
    image = models.ImageField(upload_to='owner_image/', verbose_name='Rasmi')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Direktor haqida'
        verbose_name_plural = 'Direktor haqida'


class AboutAchievements(models.Model):
    students = models.IntegerField(default=0, verbose_name='O\'quvchilar')
    results = models.IntegerField(default=0, verbose_name="Natijalar")
    teachers = models.IntegerField(default=0, verbose_name="O'qituvchilar")

    class Meta:
        verbose_name = 'Haqimizda sahifasi malumotlari'
        verbose_name_plural = 'Haqimizda sahifasi malumotlari'