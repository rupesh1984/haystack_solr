from django.urls import path

from .views import CatalogViewSet, CatalogResp


urlpatterns = [
    path('catalog/list', CatalogResp.as_view(), name='catalog-list'),
    path('catalog/other', CatalogViewSet.as_view(), name='api-post-list'),
    #path('posts/<uuid:pk>/', blog_views.PostDetailsAPIView.as_view(), name='api-post-details'),
]