from django.urls import path#パス関数のインポート
from . import views#アプリファイル内の全てのビューをインポートする
from django.conf.urls import url

urlpatterns = [
  path('user/list/',views.user_list,name='user_list'),
  path('user/index/',views.user_index.as_view(),name='user_index'),
  path('user/create/',views.user_create.as_view(),name='user_create'),
  path('user/<int:pk>/',views.user_detail.as_view(),name='user_detail'),
  #path('user/<int:pk>/update',views.user_update.as_view(),name='user_update'),
  path('user/<int:pk>/delete',views.user_delete.as_view(),name='user_delete'),
  path('',views.user_main,name='user_main'),#user_mainという名前のビューをルートURLに割り当て
  url(r'^user/(?P<pk>\d+)/update/$',views.user_update.as_view(),name='user_update'),
]
