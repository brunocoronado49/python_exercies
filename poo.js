class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
    }

    readBook() {
        console.log(`I am reading ${this.title} from ${this.author}`);
    }
}

class Comic extends Book {
    constructor(title, author, editorial) {
        super(title, author);
        this.editorial = editorial;
    }

    readBook() {
        console.log(`Hello ${this.title} form ${this.editorial}`);
    }
}

const harry = new Book('Harry Potter', 'JK Rowlling');
harry.readBook();

const barman = new Comic('Batman Dark', 'Frank Miller', 'DC');
barman.readBook();
