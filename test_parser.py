import unittest
from test_parser import parse_hh

class HHVacanciesParserTests(unittest.TestCase):
    def test_parse_hh_returns_non_empty_list(self):
        vacancies = parse_hh('Python developer')
        self.assertTrue(len(vacancies) > 0, "Expected non-empty list of vacancies")

    def test_parse_hh_contains_expected_fields(self):
        vacancies = parse_hh('Python developer')
        for vacancy in vacancies:
            with self.subTest(vacancy=vacancy):
                self.assertIn('title', vacancy)
                self.assertIn('link', vacancy)
                self.assertIn('company', vacancy)
                self.assertIn('location', vacancy)
                self.assertIn('salary', vacancy)

if __name__ == '__main__':
    unittest.main()