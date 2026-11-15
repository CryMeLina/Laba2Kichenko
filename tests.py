import unittest
from main import is_valid_url, find_urls_in_text


class TestUrlRegex(unittest.TestCase):

    def test_valid_urls(self):
        self.assertTrue(is_valid_url("http://example.com"))
        self.assertTrue(is_valid_url("https://google.com"))
        self.assertTrue(is_valid_url("https://sub.domain-name.ru/path/to/page.html"))
        self.assertTrue(is_valid_url("https://site.org/search?q=python&page=1"))

    def test_invalid_urls(self):
        self.assertFalse(is_valid_url("ftp://example.com"))
        self.assertFalse(is_valid_url("http://invalid"))
        self.assertFalse(is_valid_url("https://example.c"))
        self.assertFalse(is_valid_url("просто какой-то текст"))
        self.assertFalse(is_valid_url("https://site.com/ссылка с пробелом"))

    def test_find_urls_in_html(self):
        html_sample = '''
        <html>
            <body>
                <a href="https://stankin.ru/news">Новости</a>
                <a href='http://test-site.org/index.html'>Тест</a>
                <p>Просто ссылка в тексте: https://python.org и конец строки.</p>
            </body>
        </html>
        '''
        expected = [
            "https://stankin.ru/news",
            "http://test-site.org/index.html",
            "https://python.org"
        ]
        result = find_urls_in_text(html_sample)
        self.assertEqual(result, expected)

    def test_find_urls_empty(self):
        text = "В этом тексте вообще нет никаких гиперссылок, только слова."
        result = find_urls_in_text(text)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()