import unittest
from unittest.mock import patch
from parameterized import parameterized

from main import people, show_shelf, delete_doc, move_document, add_new_shelf
from main import documents, directories


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        print(">>> setUp")

    def tearDown(self) -> None:
        print(">>> tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print(">>> setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print(">>> tearDownClass")

    # Тестируем поиск человека по номеру документа:
    @parameterized.expand(
        [
            ("11-2", documents, "Геннадий Покемонов"),
            ("555", documents, "not_found")
        ]
    )
    def test_people(self, number_doc, doc_list, result):
        print(">>> test people()")
        self.assertEqual(people(number_doc, doc_list), result)

    # Тестируем наличие документа на полке:
    @parameterized.expand(
        [
            ("15-3", directories, 2),
            ("555", directories, False)
        ]
    )
    def test_show_shelf(self, number_doc, shelfs, result):
        print(">>> test show_shelf()")
        self.assertEqual(show_shelf(number_doc, shelfs), result)

    # Тестируем успешное добавление нового документа в базу и на полку:
    @patch("main.add_doc", return_value=f'Вы добавили: passport "6505 255178" Иван Иванов на 2 полку')
    def test_add_doc(self, func):
        print(">>> test add_doc()")
        new_type = "passport"
        new_number = "6505 255178"
        new_name = "Иван Иванов"
        shelf_number = "2"
        result = f'Вы добавили: {new_type} "{new_number}" {new_name} на {shelf_number} полку'
        self.assertEqual(func(documents, directories), result)

    # Тестируем добавление документа на полку
    @patch("main.add_doc_on_shelf", return_value="3")
    def test_add_doc_on_shelf(self, func):
        print(">>> test add_doc_on_shelf()")
        self.assertEqual(func("105", directories), "3")

    # Тестируем удаление документа из базы:
    # 1) Проверяем его наличие 2) Удаляем 3) Проверяем наличие еще раз
    @parameterized.expand(
        [
            ("10006", documents, directories, f'Документ с номером "10006" успешно удален', 'Аристарх Павлов', 'not_found'),
            ("101", documents, directories, 'Документ не найден', 'not_found', 'not_found')
        ]
    )
    def test_delete_doc(self, number_doc, docs, shelfs, result, check_result, not_found):
        print(">>> test delete_doc()")
        self.assertEqual(people(number_doc, docs), check_result)
        self.assertEqual(delete_doc(number_doc, docs, shelfs), result)
        self.assertEqual(people(number_doc, docs), not_found)

    # Тестируем перемещение документа с одной полки на другую
    # при условии, что документ есть:
    @patch("main.add_doc_on_shelf", return_value="4")
    def test_move_document_doc_exist(self, func):
        print(">>> test move_document().1")
        self.assertEqual(func("10855", directories), "4")
        result = 'Документ успешно перемещен с 2 на 4 полку'
        self.assertEqual(move_document("10855", directories), result)

    # Тестируем перемещение документа с одной полки на другую
    # при условии, что документа нет:
    def test_move_document_doc_not_exist(self):
        print(">>> test move_document().2")
        self.assertEqual(move_document("101", directories), "Документ не найден")

    # Тестируем добавление новой полки:
    @parameterized.expand(
        [
            ("5", directories, "Полка 5 успешно добавлена"),
            ("4", directories, "Такая полка уже есть")
        ]
    )
    def test_add_new_shelf(self, shelf_num, shelfs, result):
        print(">>> test add_new_shelf()")
        self.assertEqual(add_new_shelf(shelf_num, shelfs), result)