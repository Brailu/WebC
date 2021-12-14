

from django.http.response import Http404, HttpResponseServerError
from django.shortcuts import redirect, render
from django.views import View
from main.models import Calculator
from main.forms import CalculatorForm

import logging

logger = logging.getLogger(__name__)


class CalculatorListView(View):

    def get(self, request):
        calculators = Calculator.objects.all()
        context = {"calculators": calculators}
        return render(request, "main/calculator/list.html", context)


class CalculatorDetailView(View):

    def get(self, request, id):
        try:
            calculator = Calculator.objects.get(id=id)
            context = {"calculator": calculator}
            return render(request, "main/calculator/detail.html", context)
        except Calculator.DoesNotExist:
            raise Http404()


class CalculatorCreateView(View):

    def get(self, request):
        form = CalculatorForm()
        context = {"form": form}
        return render(request, "main/calculator/create.html", context)

    def post(self, request):
        form = CalculatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/calculator/")
        else:
            context = {"form": form}
            return render(request, "main/calculator/create.html", context)

    def post(self, request):
        form = CalculatorForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"Calculator \"{form.instance.name}\" saved!")
            return redirect("/calculator/")
        else:
            context = {"form": form}
            return render(request, "main/calculator/create.html", context)


class CalculatorUpdateView(View):

    def get(self, request, id):
        try:
            calculator = Calculator.objects.get(id=id)
            form = CalculatorForm(instance=calculator)
            context = {"form": form}
            return render(request, "main/calculator/update.html", context)
        except Calculator.DoesNotExist:
            raise Http404()

    def post(self, request, id):
        try:
            calculator = Calculator.objects.get(id=id)
            form = CalculatorForm(request.POST, instance=calculator)
            if form.is_valid():
                form.save()
                return redirect(f"/calculator/{id}/")
            else:
                context = {"form": form}
                return render(request, "main/calculator/create.html", context)
        except Calculator.DoesNotExist:
            raise Http404()
    
    def post(self, request, id):
        try:
            calculator = Calculator.objects.get(id=id)
            form = CalculatorForm(request.POST, instance=calculator)
            if form.is_valid():
                form.save()
                logger.info(f"Calculator \"{form.instance.name}\" updated!")
                return redirect(f"/calculator/{id}/")
            else:
                context = {"form": form}
                return render(request, "main/calculator/create.html", context)
        except Calculator.DoesNotExist:
            raise Http404()


class CalculatorDeleteView(View):
    
    def get(self, request, id):
        try:
            calculator = Calculator.objects.get(id=id)
            context = {"calculator": calculator}
            return render(request, "main/calculator/delete.html", context)
        except Calculator.DoesNotExist:
            raise Http404()

    def post(self, request, id):
        try:
            calculator = Calculator.objects.get(id=id)
            calculator.delete()
            return redirect("/calculator/")
        except Calculator.DoesNotExist:
            raise Http404()
    
    def post(self, request, id):
        try:
            calculator = Calculator.objects.get(id=id)
            calculator.delete()
            logger.info(f"Calculator \"{calculator.name}\" deleted!")
            return redirect("/calculator/")
        except Calculator.DoesNotExist:
            raise Http404()


class HomeView(View):

    def get(self, request):
        return render(request, "main/home.html")