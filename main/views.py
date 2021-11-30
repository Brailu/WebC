from django.shortcuts import render
from django.views import View
from main.models import Calculator


class CalculatorListView(View):

    def get(self, request):
        calculators = Calculator.objects.all()
        context = {"calculators": calculators}
        return render(request, "main/calculator/list.html", context)
