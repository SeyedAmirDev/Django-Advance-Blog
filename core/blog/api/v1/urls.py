from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api-v1"

router = DefaultRouter()
router.register(r'post', views.PostModelViewSet, basename='post')
router.register(r'category', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls

# urlpatterns = [
    # path('post/', views.PostListApi.as_view(), name='post-list'),
    # path('post/<int:pk>/', views.PostDetailApi.as_view(), name='post-detail'),
    # path('post/', views.PostViewSet.as_view({'get':'list'}), name='post-list'),
    # path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve'}), name='post-detail'),
# ]