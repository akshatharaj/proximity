CREATE DATABASE proximity;

CREATE TABLE Listing (
id INT(30) AUTO_INCREMENT NOT NULL PRIMARY KEY,
num_bedrooms INT(10),
num_bathrooms INT(10),
living_area VARCHAR(30),
lat VARCHAR(30),
lon VARCHAR(30),
exterior_stories VARCHAR(30),
pool INT(10),
dwelling_type VARCHAR(30),
list_date DATE,
list_price VARCHAR(30),
close_date DATE,
close_price VARCHAR(30) );