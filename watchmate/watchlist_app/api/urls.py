from django.urls import path,include
from watchlist_app.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatFormViewSet,basename='steamplatforms')

urlpatterns = [
    path('list/', WatchListView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('watch/list/', WatchListViewSet.as_view(),name='watchlist-list'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatFormListView.as_view(),name='steam'),
    # path('stream/<int:pk>', StreamPlatFormDetailView.as_view(),name='steam'),
    path('<int:pk>/reviews/', ReviewList.as_view(),name='review-list'),
    path('<int:pk>/review-create',ReviewCreateView.as_view(),name='review-create'),
    path('reviews/<int:pk>', ReviewDetailView.as_view(),name='review-detail'),
    # path('/reviews/', ReviewList.as_view(),name='review-list'),
    # path('reviews/<int:pk>', ReviewDetailView.as_view(),name='review-detail'),
    # path('list/',movie_list,name='movie-list'),
    # path('<int:pk>',movie_detail,name='movie-detail'),
    path('review/<str:username>/', UserReview.as_view(), name='review-user-detail'),
]
