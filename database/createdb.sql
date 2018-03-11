DROP TABLE IF EXISTS Building;
DROP TABLE IF EXISTS University;
DROP TABLE IF EXISTS City;
DROP TABLE IF EXISTS STATE;
DROP TABLE IF EXISTS Trashcan;

CREATE TABLE Trashcan(id INT NOT NULL,
	nickname varchar(255) UNIQUE,
	value REAL,
	location varchar(255),
	PRIMARY KEY(id));
CREATE TABLE State(tid INT NOT NULL,
	state varchar(255) NOT NULL,
	FOREIGN KEY (tid) REFERENCES Trashcan(id));
CREATE TABLE City(tid INT NOT NULL,
	state varchar(255) NOT NULL,
	city varchar(255) NOT NULL,
	FOREIGN KEY (tid) REFERENCES Trashcan(id),
	PRIMARY KEY(tid, state, city));
CREATE TABLE University(tid INT NOT NULL,
	state varchar(255) NOT NULL,
	city varchar(255) NOT NULL,
	university varchar(255) NOT NULL,
	FOREIGN KEY (tid) REFERENCES Trashcan(id),
	PRIMARY KEY (tid, state, city, university));
CREATE TABLE Building(tid INT NOT NULL,
	state varchar(255) NOT NULL,
	city varchar(255) NOT NULL,
	university varchar(255) NOT NULL,
	building varchar(255) NOT NULL,
	FOREIGN KEY (tid) REFERENCES Trashcan(id),
	PRIMARY KEY (tid, state, city, university, building)); 
