from django.urls import path
from main.views import CalculatorListView
from main.views import CalculatorDetailView
from main.views import CalculatorCreateView
from main.views import CalculatorUpdateView
from main.views import CalculatorDeleteView
from main.views import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("calculator/", CalculatorListView.as_view(), name="calculator_list"),
    path("calculator/create/", CalculatorCreateView.as_view(), name="calculator_create"),
    path("calculator/<int:id>/", CalculatorDetailView.as_view(), name="calculator_detail"),
    path("calculator/<int:id>/update/", CalculatorUpdateView.as_view(), name="calculator_update"),
    path("calculator/<int:id>/delete/", CalculatorDeleteView.as_view(), name="calculator_delete"),
]
