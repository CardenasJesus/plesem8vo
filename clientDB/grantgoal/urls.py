from django.urls import path
from grantgoal import views

app_name = "gg"

urlpatterns = [
    path('client/list/grantgoal/', views.ListGrantGoalClientView.as_view(), name="list_gg_cl"),
    path('client/detail/grantgoal/<int:pk>/', views.DetailGrantGoalClientView.as_view(), name="detail_gg_cl"),
    path('client/create/grantgoal/', views.CreateGrantGoalClientView.as_view(), name="create_gg_cl")
]