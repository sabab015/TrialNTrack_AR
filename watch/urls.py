# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from . import views
from django.urls import path


app_name = 'watch'
urlpatterns = [
    #/watch/
    path('', views.IndexClassView.as_view(), name='index'),
    #/watch/1
    path('<int:pk>/', views.WatchDetail.as_view(), name='detail'),
    path('product/', views.product, name='product'),
    # add product
    path('add', views.CreateProduct.as_view(), name='create_product'),
    # edit
    path('update/<int:id>', views.update_product, name='update_product'),
    # remove product
    path('remove/<int:id>', views.remove_product, name='remove_product'),
    
]