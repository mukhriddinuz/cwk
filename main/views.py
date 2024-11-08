from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Logo, Banner, Course, HomeAchievements,
    Result, AboutOwner, AboutAchievements, CourseLevel, Registration
)
from .serializers import (
    LogoSerializer, BannerSerializer, CourseSerializer,
    HomeAchievementsSerializer, ResultSerializer,
    AboutOwnerSerializer, AboutAchievementsSerializer, CourseLevelSerializer
)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def handle_request(view_func):
    """Yangi ko'rinishlar uchun umumiy xato ushlovchi funktsiya."""
    def wrapper(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except Logo.DoesNotExist:
            return Response({'error': 'Logo not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Banner.DoesNotExist:
            return Response({'error': 'Banner not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper


@api_view(['GET'])
@handle_request
def get_logo(request):
    logo = Logo.objects.last()
    serializer = LogoSerializer(logo)
    return Response(serializer.data)


@api_view(['GET'])
@handle_request
def get_banner(request):
    banner = Banner.objects.last()
    serializer = BannerSerializer(banner)
    return Response(serializer.data)


@api_view(['GET'])
@handle_request
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@handle_request
def get_result(request):
    results = Result.objects.all().order_by('-id')[:16]
    serializer = ResultSerializer(results, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@handle_request
def home_achievements_list(request):
    home_achievements = HomeAchievements.objects.last()
    serializer = HomeAchievementsSerializer(home_achievements)
    return Response(serializer.data)


@api_view(['GET'])
@handle_request
def course_level_info(request, pk):
    course = Course.objects.get(pk=pk)
    course_serializer = CourseSerializer(course).data
    course_levels = CourseLevel.objects.filter(course_id=pk)
    course_level_serializer = CourseLevelSerializer(course_levels, many=True).data
    data = {
        "course": course_serializer,
        "course_levels": course_level_serializer
    }
    return Response(data)


@api_view(['GET'])
@handle_request
def about_owner(request):
    about_owner = AboutOwner.objects.last()
    serializer = AboutOwnerSerializer(about_owner)
    return Response(serializer.data)


@api_view(['GET'])
@handle_request
def about_achievement(request):
    about_achievement = AboutAchievements.objects.last()
    serializer = AboutAchievementsSerializer(about_achievement)
    return Response(serializer.data)


@api_view(['GET'])
@handle_request
def home_page(request):
    logo = Logo.objects.last()
    banner = Banner.objects.last()
    results = Result.objects.all().order_by('-id')[:4]
    home_achievements = HomeAchievements.objects.last()

    data = {
        'logo': LogoSerializer(logo).data,
        'banner': BannerSerializer(banner).data,
        'results': ResultSerializer(results, many=True).data,
        'achievements': HomeAchievementsSerializer(home_achievements).data
    }
    return Response(data)


@api_view(['GET'])
@handle_request
def about_page(request):
    logo = Logo.objects.last()
    about_owner = AboutOwner.objects.last()
    about_achievement = AboutAchievements.objects.last()
    results = Result.objects.all().order_by('-id')[:4]

    data = {
        'logo': LogoSerializer(logo).data,
        'about_owner': AboutOwnerSerializer(about_owner).data,
        'achievements': AboutAchievementsSerializer(about_achievement).data,
        'results': ResultSerializer(results, many=True).data
    }
    return Response(data)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'phone'],
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Course ID'),
            'name': openapi.Schema(type=openapi.TYPE_STRING, description='User name'),
            'phone': openapi.Schema(type=openapi.TYPE_STRING, description='User phone number'),
        },
    ),
    responses={200: 'Registration created successfully', 400: 'Bad Request'},
)
@api_view(['POST'])
@handle_request
def create_registration(request):
    course = request.POST.get('id')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    if course:
        Registration.objects.create(
            course_id=course,
            name=name,
            phone=phone
        )
    else:
        Registration.objects.create(
            course=None,
            name=name,
            phone=phone
        )
    return Response({'status':200, 'messsage':f'name: {name}, phone: {phone}'})

