from django.urls import path
from .views import (
    get_logo,
    get_banner,
    course_list,
    get_result,
    home_achievements_list,
    course_level_info,
    about_owner,
    about_achievement,
    home_page,
    about_page,
    create_registration
)

urlpatterns = [
    path('logo/', get_logo, name='get_logo'),
    path('banner/', get_banner, name='get_banner'),
    path('courses/', course_list, name='course_list'),
    path('results/', get_result, name='get_result'),
    path('home-achievements/', home_achievements_list, name='home_achievements_list'),
    path('courses/<int:pk>/levels/', course_level_info, name='course_level_info'),
    path('about/owner/', about_owner, name='about_owner'),
    path('about/achievement/', about_achievement, name='about_achievement'),
    path('registration/', create_registration, name='create_registration'),


    path('home/', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
]
