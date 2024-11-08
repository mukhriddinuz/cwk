from rest_framework import serializers
from .models import (
    Logo, BannerImage, Banner, Course, CourseLevelFields,
    CourseLevel, HomeAchievements, Result, Registration,
    AboutOwner, AboutAchievements, CourseCategory
)


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['id', 'logo']


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['image']


class BannerSerializer(serializers.ModelSerializer):
    images = BannerImageSerializer(many=True, read_only=True)

    class Meta:
        model = Banner
        fields = ['id', 'title', 'description', 'images']


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['name']


class CourseSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher_full_name', 'title', 'description', 'category', 'image']


class CourseLevelFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLevelFields
        fields = ['name']


class CourseLevelSerializer(serializers.ModelSerializer):
    fields = CourseLevelFieldsSerializer(many=True, read_only=True)

    class Meta:
        model = CourseLevel
        fields = ['id', 'name', 'fields']


class HomeAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAchievements
        fields = ['students', 'results', 'teachers']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['id', 'image']


class RegistrationSerializer(serializers.ModelSerializer):
    course = CourseLevelSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'course', 'name', 'phone', 'is_active']


class AboutOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutOwner
        fields = ['id', 'full_name', 'info', 'image']


class AboutAchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutAchievements
        fields = ['students', 'results', 'teachers']
