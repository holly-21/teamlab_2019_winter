from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('create/', views.create, name='restaurants-create'),
    path('update/', views.update, name='restaurants-update'),
    # path('detail/', views.detail, name='restaurants-detail'),
    path('delete/', views.delete, name='restaurants-delete'),

    path('restaurants/<int:id>/', views.detail, name='restaurants-detail'),
    path('restaurants/<int:restaurants_id>/review/create/', views.review_create, name="review-create"),
    path('restaurants/<int:restaurants_id>/review/delete/<int:review_id>', views.review_delete, name="review-delete"),
    path('review/list/', views.review_list, name="review-list"),
]