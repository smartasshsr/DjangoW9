from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.posting_create, name='posting_create'),
    path('list/', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('<int:posting_id>/update/', views.posting_update, name='posting_update'),
    path('<int:posting_id>/delete/', views.posting_delete, name='posting_delete'),
    # [코드 작성] 댓글 삭제 기능을 동작하게 하는 url 작성 (posting_id, comment_id 인자 전달)
    path('<int:posting_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]
