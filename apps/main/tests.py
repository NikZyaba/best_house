from django.test import TestCase
from .models import SaveDbConsulting
from termcolor import colored


class SaveDbConsultingModelTestCase(TestCase):

    def setUp(self):
        print("-" * 50)
        self.consulting1 = SaveDbConsulting.objects.create(
            buyer_name="Nick",
            phone_number="+375447295544",
            description="Test1")
        self.consulting2 = SaveDbConsulting.objects.create(
            buyer_name="John",
            phone_number="+3754471544",
            description="Test2")
        print(colored("Test data created", "yellow"))

    def test_creation(self):
        print("*" * 10)
        print(colored("Test 1: Object creation test", "blue"))

        # Проверка первого объекта
        self.assertEqual(self.consulting1.buyer_name, "Nick")
        print("buyer_name...", colored("OK", "green"))

        self.assertEqual(self.consulting1.phone_number, "+375447295544")
        print("phone_number...", colored("OK", "green"))

        self.assertEqual(self.consulting1.description, "Test1")
        print("description...", colored("OK", "green"))

        # Проверка, что объект сохранен в БД
        self.assertTrue(SaveDbConsulting.objects.filter(buyer_name="Nick").exists())
        print("object exists in DB...", colored("OK", "green"))

        print(colored("Test 1 finished", "green"))

    def test_get_all_records(self):
        print(colored("Test 2: Get all objects from DB", "blue"))

        consultings = SaveDbConsulting.objects.all()
        self.assertEqual(consultings.count(), 2)
        print("Length of consulting = 2", colored("OK", 'green'))

        # Дополнительная проверка имен
        names = [c.buyer_name for c in consultings]
        self.assertIn("Nick", names)
        self.assertIn("John", names)
        print("All names present...", colored("OK", "green"))

        print(colored("Test 2 finished", "green"))

    def test_string_representation(self):
        print(colored("Test 3: String representation", "blue"))

        expected_str = "Nick - +375447295544"
        self.assertEqual(str(self.consulting1), expected_str)
        print(f"__str__ method: {expected_str}", colored("OK", "green"))

        print(colored("Test 3 finished", "green"))

    def test_model_meta(self):
        print(colored("Test 4: Model meta options", "blue"))

        self.assertEqual(SaveDbConsulting._meta.db_table, 'main_savedbconsulting')
        print("db_table name...", colored("OK", "green"))

        self.assertEqual(SaveDbConsulting._meta.verbose_name, 'Consult')
        print("verbose_name...", colored("OK", "green"))

        print(colored("Test 4 finished", "green"))


