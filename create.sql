CREATE TABLE User(USID varchar(5) primary key, name varchar(30), email varchar(50), password varchar(100)) CHARACTER SET utf8;

CREATE TABLE Entertainment(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;
CREATE TABLE SocialMedia(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;
CREATE TABLE Messaging(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;
CREATE TABLE Illegal(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;
CREATE TABLE News(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;
CREATE TABLE ECommerce(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;
CREATE TABLE Bookings(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;
CREATE TABLE Games(URLID varchar(5) primary key, name varchar(50), URL varchar(100)) CHARACTER SET utf8;

CREATE TABLE Plan(USID varchar(5) primary key, entertainment varchar(100), socialMedia varchar(100),
messaging varchar(100), illegal varchar(100), news varchar(100), eCommerce varchar(100), bookings varchar(100),
games varchar(100)) CHARACTER SET utf8;

CREATE TABLE Custom(USID varchar(5) primary key, block varchar(100), redirect varchar(100)) CHARACTER SET utf8;

alter table Plan add foreign key (USID) references User(USID);
alter table Custom add foreign key (USID) references User(USID);
