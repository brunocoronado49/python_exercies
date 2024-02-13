class Book:
    def __init__(self, title: str, author: str, gender: str, price: float) -> None:
        self.__title = title
        self.__author = author
        self.__gender = gender
        self.__price = price
        
    def get_price(self) -> float:
        return self.__price
        
    def set_price(self, price: float) -> None:
        self.__price = price
            
    def attrs(self) -> None:
        print(f'Title: {self.__title}')
        print(f'Author: {self.__author}')
        print(f'Gender: {self.__gender}')
        print(f'Price: {self.__price}')
            
    def read_book(self) -> None:
        print(f'I am reading {self.__title} from {self.__author}')
            

book = Book('Book', 'Humano', 'Letters', 120.50)
book.attrs()


class Comic(Book):
    def __init__(self, title: str, author: str, gender: str, price: float, home: str) -> None:
        super().__init__(title, author, gender, price)
        self.__home = home
        
    def get_price(self) -> float:
        return self.__price
    
    def set_price(self, price: float) -> None:
        self.__price = price
        
    def attrs(self) -> None:
        super().attrs()
        print(f'Editorial Home: {self.__home}')
        
    def read_book(self) -> None:
        print(f'This is {self.__title} from the editorial {self.__home}')
        

batman = Comic('Batman Damage', 'Frank Miller', 'Fiction/Horror', 19.90, 'DC')
# print(batman.get_price())
# batman.set_price(15.70)
batman.attrs()