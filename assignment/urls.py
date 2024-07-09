from django.urls import path
from . import views

urlpatterns = [
    path('', views.streamlit_view),
    path('exercise_two/', views.excercise_two_get_req, name='excercise_two'),
    path('exercise_two_three/', views.get_historical_events, name='historical_events'),
    path('exercise_four/', views.collect_user_data, name='collect_user_data'),
    path('exercise_five/', views.display_user_data, name='display_user_data'),
]