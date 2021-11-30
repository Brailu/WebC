from django.test import TestCase
from django.core.exceptions import ValidationError
from main.models import Calculator


class CalculatorModelTest(TestCase):

    def test_raise_if_name_is_none(self):
        calculator = Calculator(name=None)
        with self.assertRaises(ValidationError):
            calculator.full_clean()

    def test_raise_if_name_is_over_length(self):
        invalid_name = "t" * 33
        calculator = Calculator(name=invalid_name)
        with self.assertRaises(ValidationError):
            calculator.full_clean()

    def test_raise_if_name_is_not_unique(self):
        calculator = Calculator(name="test")
        calculator.save()
        duplicated = Calculator(name="test")
        with self.assertRaises(ValidationError):
            duplicated.full_clean()
    
    def test_to_str(self):
        calculator = Calculator(name="test")
        self.assertEqual(str(calculator), "test")

class CalculatorListViewTest(TestCase):

    def setUp(self):
        self.calculator = Calculator.objects.create(name="test")

    def test_render_list(self):
        response = self.client.get("/calculator/")
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["calculators"], ["<Calculator: test>"])
        self.assertTemplateUsed(response, "main/calculator/list.html")

