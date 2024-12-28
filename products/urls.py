from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('category',views.category),
    path('about',views.about),
    path('contact',views.contact,name='contact'),
    path('book',views.book),
    path('mobile',views.mobile),
    path('beauty',views.beauty),
    path('rasan',views.rasan),
    path('vehicle',views.vehicle),
    # path('comments',views.commentsCreateView.as_view(),name='comments')
    path('buy/<id>',views.buy,name='buy')
    
]
