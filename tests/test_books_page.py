import pytest
from .base_test import TestBase
from pages.books_page.books_page import BooksPage
import locale

locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")

BOOKS_ON_PAGE_COUNT = 12
MAX_PRICE = 100
MIN_PRICE = 500

class TestBooksPage(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.books = BooksPage(self.driver)
        yield
        self.driver.delete_all_cookies()

    def test_all_books_visible(self):
        assert self.books.all_books_count() == BOOKS_ON_PAGE_COUNT

    def test_max_price_filter(self):
        self.books.filter_by_max_price()
        prices = self.books.get_books_prices()
        for price in prices:
            assert price < MAX_PRICE

    def test_min_price_filter(self):
        self.books.filter_by_min_price()
        prices = self.books.get_books_prices()
        for price in prices:
            assert price > MIN_PRICE

    def test_sort_price_desc(self):
        self.books.sort_by_price_desc()
        prices = self.books.get_books_prices()
        assert prices == sorted(prices, reverse=True)

    def test_sort_price_asc(self):
        self.books.sort_by_price_asc()
        prices = self.books.get_books_prices()
        assert prices == sorted(prices)

    def test_sort_name_desc(self):
        self.books.sort_by_name_desc()
        names = self.books.get_books_titles()
        assert names == sorted(names, key=locale.strxfrm, reverse=True)

    def test_sort_name_asc(self):
        self.books.sort_by_name_asc()
        names = self.books.get_books_titles()
        assert names == sorted(names, key=locale.strxfrm)

