from django.urls import path, include
from . import views
from . views import article_list, article_detail, ArticleDetails, ArticleAPIView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('', views.homepage),
    path('list/', article_list),
    path('detail/<int:pk>', views.article_detail, name='article_detail'),
    path('details/<int:id>', ArticleDetails.as_view()), 
    path('article/', ArticleAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]