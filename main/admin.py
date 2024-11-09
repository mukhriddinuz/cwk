from django.contrib import admin
from .models import (
    Logo, BannerImage, Banner, Course, CourseLevelFields,
    CourseLevel, HomeAchievements, Result, Registration,
    AboutOwner, AboutAchievements, CourseCategory
)


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo')
    search_fields = ('id',)


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('image', )
    search_fields = ('image',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    filter_horizontal = ('images',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher_full_name', 'title')
    search_fields = ('name', 'teacher_full_name')
    ordering = ('name',)


@admin.register(CourseLevelFields)
class CourseLevelFieldsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(CourseLevel)
class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    list_filter = ('course',)
    filter_horizontal = ('fields',)
    search_fields = ('name', 'course__name')


@admin.register(HomeAchievements)
class HomeAchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'students', 'results', 'teachers')
    list_editable = ('students', 'results', 'teachers')
    list_display_links = ('id',)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('id',)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'course', 'is_active')
    list_filter = ('course', 'is_active',)
    search_fields = ('name', 'phone')
    list_per_page = 20


@admin.register(AboutOwner)
class AboutOwnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'info')
    search_fields = ('full_name',)


@admin.register(AboutAchievements)
class AboutAchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'students', 'results', 'teachers')
    list_editable = ('students', 'results', 'teachers')
    list_display_links = ('id',)


admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Boshqaruv paneliga xush kelibsiz"
