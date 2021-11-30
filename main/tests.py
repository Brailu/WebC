from django.test import TestCase
from django.core.exceptions import ValidationError
from main.models import Calculator
from main.forms import CalculatorForm


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


class CalculatorFormTest(TestCase):

    def test_is_invalid_if_name_is_none(self):
        form = CalculatorForm({"name": None})
        self.assertFalse(form.is_valid())
    
    def test_is_invalid_if_name_is_not_unique(self):
        Calculator.objects.create(name="test")
        form = CalculatorForm({"name": "test"})
        self.assertFalse(form.is_valid())


class CalculatorListViewTest(TestCase):

    def setUp(self):
        self.calculator = Calculator.objects.create(name="test")

    def test_render_list(self):
        response = self.client.get("/calculator/")
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["calculators"], ["<Calculator: test>"])
        self.assertTemplateUsed(response, "main/calculator/list.html")


class CalculatorDetailViewTest(TestCase):

    def setUp(self):
        self.calculator = Calculator.objects.create(name="test")
    
    def test_render_detail(self):
        response = self.client.get(f"/calculator/{self.calculator.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["calculator"], Calculator)
        self.assertTemplateUsed(response, "main/calculator/detail.html")

    def test_raise_404(self):
        response = self.client.get("/calculator/9999/")
        self.assertEqual(response.status_code, 404)


class CalculatorCreateViewTest(TestCase):
    
    def test_render_form(self):
        response = self.client.get("/calculator/create/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CalculatorForm)

    def test_create_with_valid_data(self):
        data = {"name": "test"}
        response = self.client.post("/calculator/create/", data)
        self.assertRedirects(response, "/calculator/")
        calculator = Calculator.objects.get(name="test")
        self.assertEqual(calculator.name, "test")

    def test_render_form_with_invalid_data(self):
        data = {}
        response = self.client.post("/calculator/create/", data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["form"].is_valid())


class CalculatorUpdateViewTest(TestCase):
    
    def setUp(self):
        self.calculator = Calculator.objects.create(name="test")

    def teste_render_form(self):
        response = self.client.get(f"/calculator/{self.calculator.id}/update/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CalculatorForm)

    def test_raise_404(self):
        response = self.client.get(f"/calculator/9999/update/")
        self.assertEqual(response.status_code, 404)
        response = self.client.post("/calculator/9999/update/")
        self.assertEqual(response.status_code, 404)

    def test_update_with_valid_data(self):
        data = {"name": "updated"}
        response = self.client.post(f"/calculator/{self.calculator.id}/update/", data)
        self.assertRedirects(response, f"/calculator/{self.calculator.id}/")
        calculator = Calculator.objects.get(name="updated")
        self.assertEqual(calculator.name, "updated")

    def test_render_form_with_invalid_data(self):
        data = {}
        response = self.client.post(f"/calculator/{self.calculator.id}/update/", data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["form"].is_valid())


class CalculatorDeleteViewTest(TestCase):
    
    def setUp(self):
        self.calculator = Calculator.objects.create(name="test")

    def test_render_confirm(self):
        response = self.client.get(f"/calculator/{self.calculator.id}/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/calculator/delete.html")

    def test_raise_404(self):
        response = self.client.get(f"/calculator/9999/delete/")
        self.assertEqual(response.status_code, 404)
        response = self.client.post("/calculator/9999/delete/")
        self.assertEqual(response.status_code, 404)

    def test_delete_with_valid_data(self):
        response = self.client.post(f"/calculator/{self.calculator.id}/delete/")
        self.assertRedirects(response, "/calculator/")
        with self.assertRaises(Calculator.DoesNotExist):
            Calculator.objects.get(name="test"
