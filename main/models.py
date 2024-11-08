from django.db import models
from ckeditor.fields import RichTextField


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/')


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banner_image/')

    def __str__(self):
        return f"Banner Image ID: {self.id}"


class Banner(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    images = models.ManyToManyField(to=BannerImage)

    def __str__(self):
        return self.title


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_photo/')
    category = models.ForeignKey(to=CourseCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class CourseLevelFields(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CourseLevel(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    fields = models.ManyToManyField(to=CourseLevelFields)
    image = models.ImageField(upload_to='level_images/')

    def __str__(self):
        return f"{self.name} - {self.course.name}"


class HomeAchievements(models.Model):
    students = models.IntegerField(default=0)
    results = models.IntegerField(default=0)
    teachers = models.IntegerField(default=0)

    def __str__(self):
        return f"Achievements: {self.students} students, {self.results} results, {self.teachers} teachers"


class Result(models.Model):
    image = models.ImageField(upload_to='results/')


class Registration(models.Model):
    course = models.ForeignKey(to=CourseLevel, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.course.name if self.course else 'No Course'} - {self.name}"


class AboutOwner(models.Model):
    full_name = models.CharField(max_length=300)
    info = RichTextField()
    image = models.ImageField(upload_to='owner_image/')

    def __str__(self):
        return self.full_name


class AboutAchievements(models.Model):
    students = models.IntegerField(default=0)
    results = models.IntegerField(default=0)
    teachers = models.IntegerField(default=0)

    def __str__(self):
        return f"About Achievements: {self.students} students, {self.results} results, {self.teachers} teachers"
