class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise RuntimeError("Title must not be empty.")
        self.__title = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if not self.is_valid_isbn(value):
            raise RuntimeError("ISBN must be a valid ISBN number.")
        self.__isbn = value

    @staticmethod
    def is_valid_isbn(isbn):
        digits = [int(char) for char in isbn if '0' <= char <= '9']
        if len(digits) != 13:
            raise RuntimeError("ISBN needs to have 13 numbers.")
        else:
            sum = 0
            for i in range(len(digits)):
                if i % 2 == 0:
                    sum += int(digits[i])
                else:
                    sum += 3* int(digits[i])
            return sum % 10 == 0