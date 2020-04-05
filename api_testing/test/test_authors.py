import unittest
from datetime import datetime
from core import api_authors as act


class ApiRequestsActivities(unittest.TestCase):
    now = datetime.now()




    def test_get_all_authors(self):

        self.response = act.get_all_authors()


    def test_response(self):
        self.response = act.get_all_authors()
        self.assertEqual(self.response.status_code, 200)

    def test_create_author(self):

        self.response = act.create_authors("20",
                                            "5",
                                            "Luis",
                                            "Ordoñez")
        return self.response


    def test_delete_authors(self):

        self.response = act.delete_authors("20")
        self.assertEqual(self.response.status_code, 200)

    def test_get_authors(self):

        self.response = act.get_authors("1")
        self.assertEqual(self.response.status_code, 200)

    def test_put_author(self):

        self.response = act.put_authors("2",
                                            "5",
                                            "Luis",
                                            "Rodriguez")
        self.assertEqual(self.response.status_code, 200)

    def test_get_all_books(self):
        self.response = act.get_all_books()
        self.assertEqual(self.response.status_code, 200)

    def test_create_books(self):
        self.response = act.create_books("25",
                                           "Ciencia",
                                            "Descripcion ciencia",
                                            "100",
                                           "excerpt1",
                                           self.now)
        self.assertEqual(self.response.status_code, 200)

    def test_delete_books(self):
        self.response = act.delete_books("25")
        self.assertEqual(self.response.status_code, 200)

    def test_get_book(self):
        self.response = act.get_books("1")
        self.assertEqual(self.response.status_code, 200)

    def test_put_book(self):
        self.response = act.put_books("25",
                                           "Ciencia",
                                            "Descripcion ciencia",
                                            "100",
                                           "excerpt1",
                                           self.now)
        self.assertEqual(self.response.status_code, 200)



if __name__ == '__main__':
    unittest.main()

