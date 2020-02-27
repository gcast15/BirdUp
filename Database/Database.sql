CREATE TABLE Entry(
entry_Id INTEGER REFERENCES Bird(bird_Id),
common_Name varchar (30),
wiki_link varchar(255),
conservation_Status varchar (25) ,
eats int REFERENCES Feed_Mix(feed_Id),
place_Seen int REFERENCES Location(location_Id),
seen_Date DATETIME NOT NULL,
seen_time DATETIME NOT NULL
)

CREATE TABLE Bird(
bird_Id INTEGER PRIMARY KEY,
common_Name varchar (30) ,
scientific_Name varchar (30) ,
conservation_Status varchar (25) ,
eats int REFERENCES Feed_Mix(feed_Id),
);

CREATE TABLE Feed_Mix(
feed_Id INTEGER PRIMARY KEY AUTOINCREMENT,
feed_Type varchar (30)
);

CREATE TABLE Location(
location_Id INTEGER PRIMARY KEY AUTOINCREMENT,
zip varchar (10),
city varchar (25),
state varchar (20),
weather_of int REFERENCES Weather(weather_Id)
);

