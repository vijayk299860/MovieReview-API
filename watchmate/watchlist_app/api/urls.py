from django.urls import path,include
from watchlist_app.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatFormViewSet,basename='steamplatforms')

urlpatterns = [
    path('list/', WatchListView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    
    path('', include(router.urls)),
    # path('stream/', StreamPlatFormListView.as_view(),name='steam'),
    # path('stream/<int:pk>', StreamPlatFormDetailView.as_view(),name='steam'),
    path('stream/<int:pk>/reviews/', ReviewList.as_view(),name='review-list'),
    path('stream/<int:pk>/review-create',ReviewCreateView.as_view(),name='review-create'),
    path('stream/reviews/<int:pk>', ReviewDetailView.as_view(),name='review-detail'),
    # path('/reviews/', ReviewList.as_view(),name='review-list'),
    # path('reviews/<int:pk>', ReviewDetailView.as_view(),name='review-detail'),
    # path('list/',movie_list,name='movie-list'),
    # path('<int:pk>',movie_detail,name='movie-detail'),
]
