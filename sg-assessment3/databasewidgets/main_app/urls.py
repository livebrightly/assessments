from django.contrib import admin
from django.urls import include, path
# from main_app.views import *
from . import views


urlpatterns = [


    # /widgets/
    path('', views.index, name='index'),
    # /widgets/#n/
    # path('<int:widgets_id>/', views.detail, name='detail'),




    # path('', views.home, name='home'),
    # path('', views.widgets_index, name='index'),

    # path('', views.all_widgets, name='widgets'),
    # path('', views.widget_detail, name='widget_detail'),

    # path('widgets/create/', views.WidgetCreate.as_view(), name='widgets_create'),
    # path('<int:widget_id>/1add_widget/', views.add, name='add'),

    # path('widgets/<int:pk>/delete/',
    #      views.WidgetDelete.as_view(), name='widgets_delete'),
    # path('<int:widget_id>/delete_widget/', views.delete_widget, name='delete_widget'),


]


#   path('', views.home, name='home'),
#   path('widgets/', views.widgets_index, name='index'),
#   path('widgets/<int:widget_id>/', views.widgets_detail, name='detail'),
#   path('widgets/create/', views.WidgetCreate.as_view(), name='widgets_create'),
#   path('widgets/<int:pk>/update/', views.widgetUpdate.as_view(), name='widgets_update'),
#   path('widgets/<int:pk>/delete/', views.WidgetDelete.as_view(), name='widgets_delete'),
#   path('widgets/<int:widget_id>/add_feeding/', views.add_feeding, name='add_feeding'),
#   # associate a toy with a widget (M:M)
#   path('widgets/<int:widget_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
#   # unassociate a toy and widget
#   path('widgets/<int:widget_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
#   path('widgets/<int:widget_id>/add_photo/', views.add_photo, name='add_photo'),
#   path('toys/', views.ToyList.as_view(), name='toys_index'),
#   path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
#   path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
#   path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
#   path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
