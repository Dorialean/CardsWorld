CREATE TABLE Person(
	Id INTEGER GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) NOT NULL PRIMARY KEY,
	Nickname VARCHAR(200) UNIQUE NOT NULL,
	FirstName VARCHAR(200) NULL,
	EMail VARCHAR(30) NULL,
	Password BYTEA NOT NULL,
	Picture BYTEA NULL
);

CREATE TABLE Product(
	Id INTEGER GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) NOT NULL PRIMARY KEY,
	Name VARCHAR(200) NOT NULL,
	Price MONEY NOT NULL,
	Amount INT NOT NULL,
	Description VARCHAR(500) NULL,
	SIZE VARCHAR(10) NULL,
	CompanyName VARCHAR(200) NULL,
	Photo BYTEA NULL,
	Weight DECIMAL(18,0) NULL
);

CREATE TABLE PersonOrder(
	Id INTEGER GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) NOT NULL PRIMARY KEY,
	PersonId INT REFERENCES Person(Id),
	ProductId INT REFERENCES Product(Id),
	Amount INT NOT NULL,
	Price MONEY
);

CREATE TABLE Articles(
	Id INTEGER GENERATED ALWAYS AS IDENTITY(START WITH 1 INCREMENT BY 1) NOT NULL PRIMARY KEY,
	PersonId INT REFERENCES Person(Id),
	Title NCHAR(150) NOT NULL,
	Text TEXT NOT NULL,
	Link TEXT NULL
);

ALTER TABLE Person ADD Order_id INT REFERENCES PersonOrder(Id);

SELECT * FROM Articles;
SELECT * FROM Person;
SELECT * FROM PersonOrder;
SELECT * FROM Product;

INSERT INTO Person VALUES(DEFAULT,'Dorialean','Дима','lana.lakutina@mail.ru',sha256('12345'),null,null);
INSERT INTO Product VALUES(DEFAULT,'Карты таро',3.32,5,'Импортные игральные карты таро','ИП Ванги',null,'80шт');
INSERT INTO Articles VALUES(DEFAULT,1,'Как жесток покер?','Очень жесток','https://academypoker.ru/blogs/nauchis-myslit-kak-pokernyj-professional.htmlhttps://academypoker.ru/blogs/nauchis-myslit-kak-pokernyj-professional.html');
INSERT INTO PersonOrder VALUES(DEFAULT,1,1,1,(SELECT price FROM Product WHERE Id=1));


