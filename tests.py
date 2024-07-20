from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # проверка добавления одной книги с использованием параметризации
    @pytest.mark.parametrize('book',
                             [
                                 'Маленькие женщины',
                                 'Джейн Эйр',
                                 'Ромео и Джульетта'
                             ]
                             )
    def test_add_new_book_add_one_book(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 1

    # проверка, что нельзя добавить книгу, которая есть в books_genre
    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Мастер и Маргарита')
        assert len(collector.get_books_genre()) == 1

    # проверка, что нельзя добавить книгу с названием больше 41 символа
    def test_add_new_book_add_book_more40_symbols(self):
        collector = BooksCollector()
        collector.add_new_book('Легенда о Тиле Уленшпигеле и Ламме Гудзаке, их приключениях — забавных, отважных'
                               ' и достославных во Фландрии и иных странах')
        assert len(collector.get_books_genre()) == 0

    # проверка корректного добавления жанра
    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.books_genre['Дюна'] == 'Фантастика'

    # проверка, что нельзя добавить жанр, которого нет в списке genre
    def test_set_book_genre_set_genre_not_included_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Роман')
        assert collector.books_genre['Мастер и Маргарита'] == ''

    # проверка вывода жанра добавленных книг
    def test_get_book_genre_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Десять негритят', 'Детективы')
        assert collector.get_books_genre() == collector.books_genre

    # проверка, что жанра мультфильмы нет среди добавленных книг с жанрами. Такого жанра для книг вообще быть не должно)
    def test_get_books_with_specific_genre_no_books(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == []

    # проверка вывода текущего словаря books_genre
    def test_get_books_genre_with_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == collector.books_genre

    # проверка книг для детей с одним подходящим жанром, тут - комедии
    def test_get_books_for_children_add_one_right_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Внутри убийцы')
        collector.set_book_genre('Внутри убийцы', 'Ужасы')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        assert collector.get_books_for_children() == ['Горе от ума']

    # проверка, что нельзя повторно добавить книгу в избранное
    def test_add_book_in_favorites_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('451 градус по Фаренгейту')
        collector.add_book_in_favorites('451 градус по Фаренгейту')
        collector.add_book_in_favorites('451 градус по Фаренгейту')
        assert len(collector.favorites) == 1

    # проверка корректного удаления книги из избранного
    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book('451 градус по Фаренгейту')
        collector.add_book_in_favorites('451 градус по Фаренгейту')
        collector.delete_book_from_favorites('451 градус по Фаренгейту')
        assert len(collector.favorites) == 0

    # проверка, что в списке избранного 3 конкретные книги
    def test_get_list_of_favorites_books_get_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('451 градус по Фаренгейту')
        collector.add_new_book('Внутри убийцы')
        collector.add_new_book('Горе от ума')
        collector.add_book_in_favorites('451 градус по Фаренгейту')
        collector.add_book_in_favorites('Внутри убийцы')
        collector.add_book_in_favorites('Горе от ума')
        assert collector.get_list_of_favorites_books() == collector.favorites
