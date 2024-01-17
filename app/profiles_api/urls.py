from django.urls import path, include
from profiles_api import views  # Maybe the editor will complain about this import, but it works
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# basename is optional and means that we can use the name to retrieve the url
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
