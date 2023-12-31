-- SQLBook: Code
-- Active: 1701794094340@@127.0.0.1@3306@ali
create table personality (
        Ncode int unique not null,
        fname varchar (20) not null,
        lname varchar (20) not null,
        dateofbirth date not null,
        tel int unique not null,
        email varchar (30) unique default 'exampel@gmali.com',
        proficiency varchar (20) not null,
        city varchar (15) not null,
        street varchar (15) not null,
        plaque int not null,
        primary key (Ncode)
    );

###########################################################################################

create table researcher (
        IDre int unique not null AUTO_INCREMENT,
        IDin int not null,
        Ncode int unique not null,
        Side varchar(10) not null,
        primary key (IDre),
        foreign key (Ncode) references personality (Ncode) on delete cascade on update cascade,
        foreign key (IDin) references institute (IDin) on delete cascade on update cascade
        );

CREATE PROCEDURE `add_researcher`(
	IN in_Ncode int,
  IN IN_IDIN INT,
	IN in_Side VARCHAR(10),
	in in_fname VARCHAR(20),
	in in_lname VARCHAR(255),
	in in_dateofbirth date,
	in in_tel int,
	in in_email VARCHAR(30),
	in in_proficiency VARCHAR(20),
	in in_city VARCHAR(15),
	in in_street VARCHAR(15),
	in in_plaque int,
  OUT out_result VARCHAR(255))
BEGIN
  START TRANSACTION;
  INSERT INTO personality (Ncode, fname, lname, dateofbirth, tel, email, proficiency, city, street, plaque)
  VALUES (in_Ncode, in_fname, in_lname, in_dateofbirth, in_tel, in_email, in_proficiency, in_city, in_street, in_plaque);
  INSERT INTO researcher (Ncode, Side, IDin)
  VALUES (in_Ncode, in_Side, IN_IDIN);
  SET out_result = 'Schools added successfully';
  COMMIT;
  ROLLBACK;
  END

CREATE PROCEDURE `delete_researcher`
  (IN ID_re INT, OUT out_result VARCHAR(255))
BEGIN
    DECLARE N_code INT;
    SELECT Ncode INTO N_code FROM researcher WHERE IDre = ID_re;
    DELETE FROM personality WHERE Ncode = N_code;
    SET out_result = 'Delete operation successful';
END

###########################################################################################

create table superrisor(
        IDsu int unique not null AUTO_INCREMENT,
        IDin int not null,
        Ncode int unique not null,
        primary key (IDsu),
        foreign key (Ncode) references personality (Ncode) on delete cascade on update cascade,
        foreign key (IDin) references institute (IDin) on delete cascade on update cascade
    );

CREATE PROCEDURE `ADD_SUPERRISOR`(
    IN IN_NCODE INT,
    IN IN_IDin INT,
    IN IN_FNAME VARCHAR(20),
    IN IN_LNAME VARCHAR(255),
    IN IN_DATEOFBIRTH DATE,
    IN IN_TEL INT,
    IN IN_EMAIL VARCHAR(30),
    IN IN_PROFICIENCY VARCHAR (20),
    IN IN_CITY VARCHAR(15),
    IN IN_STREET VARCHAR (15),
    IN IN_PLAQUE INT,
    OUT OUT_RESULT VARCHAR(255))
BEGIN
	START TRANSACTION;
	INSERT INTO
	  personality (Ncode,fname,lname,dateofbirth,tel,email,proficiency,city,street,plaque)
	  VALUES (in_Ncode,in_fname,in_lname,in_dateofbirth,in_tel,in_email,in_proficiency,in_city,in_street,in_plaque);
  INSERT INTO superrisor (Ncode, IDin)
    VALUES (in_Ncode, in_IDin);
	SET out_result = 'superrisor added successfully';
	COMMIT;
	ROLLBACK;
	END

CREATE PROCEDURE `delete_superrisor`
  (IN ID_su INT, OUT out_result VARCHAR(255))
BEGIN
      DECLARE N_code INT;
      SELECT Ncode INTO N_code FROM superrisor WHERE IDsu = ID_su;
      DELETE FROM personality WHERE Ncode = N_code;
      SET out_result = 'Delete operation successful';
  END

##########################################################################################

create table institute (
        college varchar (20) not null,
        IDin int unique not null AUTO_INCREMENT,
        date_of_es date not null,
        country varchar (15) not null,
        city varchar (15) not null,
        street varchar (15) not null,
        primary key (IDin)
    );

CREATE PROCEDURE `add_institute`(
    IN IN_COLLEGE VARCHAR (255),
    IN IN_DATE_OF_ESTABLISHMENT DATE,
    IN IN_COUNTRY VARCHAR(255),
    IN IN_CITY VARCHAR(255),
    IN IN_STREET VARCHAR(255),
    OUT OUT_RESULT VARCHAR(255))
BEGIN
  START TRANSACTION;
  INSERT INTO
      institute (college,date_of_es,country,city,street)
  VALUES
  (In_college,in_Date_of_Establishment,in_country,in_city,in_street);
  SET out_result = 'institute added successfully';
  COMMIT;
  ROLLBACK;
END


CREATE PROCEDURE `delete_institute`
  (IN ID_in INT, OUT out_result VARCHAR(255))
BEGIN
      DELETE FROM institute WHERE IDin = ID_in;
      SET out_result = 'Delete institute successful';
  END

-- ##########################################################################################

create table essey(
  IDes int unique not null,
  typee varchar(25) not null, 
  date_of_ar date not null, 
  IDre int not null,
  IDsu int not null,
  primary key (IDes),
  foreign key (IDre) references researcher (IDre) on delete cascade on update cascade,
  foreign key (IDsu) references superrisor (IDsu) on delete cascade on update cascade
  );

CREATE PROCEDURE `add_essey`(
    IN IN_IDes INT,
    IN IN_typee VARCHAR (255),
    IN IN_date_of_ar DATE,
    IN IN_IDre INT,
    IN IN_IDsu INT,
    OUT OUT_RESULT VARCHAR(255))
BEGIN
  START TRANSACTION;
  INSERT INTO essey
    (IDes, typee, date_of_ar, IDre, IDsu)
  VALUES  
    (IN_IDes, IN_typee, IN_date_of_ar, IN_IDre, IN_IDsu);
  SET out_result = 'institute added successfully';
  COMMIT;
  ROLLBACK;
  END


CREATE PROCEDURE `delete_essey`(IN ID_es INT, OUT 
OUT_RESULT VARCHAR(255))
BEGIN
      DELETE FROM essey WHERE IDes = ID_es;
	SET out_result = 'Delete institute successful';
	END

#############################################################

create table inventions(
  IDinven int unique not null,
  date_of_re date not null, 
  IDre int not null,
  IDsu int not null,
  primary key (IDinven),
  foreign key (IDre) references researcher (IDre) on delete cascade on update cascade,
  foreign key (IDsu) references superrisor (IDsu) on delete cascade on update cascade
  );

CREATE PROCEDURE `add_inventions`(
    IN IN_IDinven INT,
    IN IN_date_of_re DATE,
    IN IN_IDre INT,
    IN IN_IDsu INT,
    OUT OUT_RESULT VARCHAR(255))
BEGIN
  START TRANSACTION;
  INSERT INTO inventions
    (IDinven, date_of_re, IDre, IDsu)
  VALUES  
    (IN_IDinven , IN_date_of_re, IN_IDre, IN_IDsu);
  SET out_result = 'institute added successfully';
  COMMIT;
  ROLLBACK;
  END

  CREATE PROCEDURE `delete_inventions`(IN ID_inven INT, OUT 
OUT_RESULT VARCHAR(255))
BEGIN
      DELETE FROM inventions WHERE IDinven = ID_inven;
	SET out_result = 'Delete institute successful';
	END

##########################################################################################

create table budget(
    depositID int unique not null,
    valuee int default '0000',
    edate date default '1402-01-01',
    ddate date default '1402-01-01',
    sourcee varchar(25) default 'exampel', 
    IDinven int not null,
    primary key (IDinven , depositID),
    foreign key (IDinven) references inventions (IDinven)
    on delete cascade
    on update cascade);

CREATE PROCEDURE `add_budget`(
	  IN IN_depositID int,
    IN IN_valuee int,
    IN IN_edate date,
    IN IN_ddate date,
    IN IN_sourcee varchar(255),
    IN IN_IDinven int,
	  OUT OUT_RESULT VARCHAR(255)
      )
BEGIN
  START TRANSACTION;
  INSERT INTO budget
    (depositID, valuee, edate, ddate, sourcee, IDinven)
  VALUES  
    (IN_depositID, IN_valuee, IN_edate, IN_ddate, IN_sourcee, IN_IDinven);
  SET out_result = 'institute added successfully';
  COMMIT;
  ROLLBACK;
  END

CREATE PROCEDURE `delete_budget`(IN deposit_ID INT, OUT 
OUT_RESULT VARCHAR(255))
BEGIN
      DELETE FROM budget WHERE depositID = deposit_ID;
	SET out_result = 'Delete institute successful';
	END
##########################################################################################


##########################################################################################

SELECT * FROM researcher inner join personality on researcher.Ncode = personality.Ncode

UPDATE personality SET fname = 'fname', lname = 'lname', dateofbirth = 1111-1-1, tel = 123456, email = 'ali@gmail.com', proficiency = 'proficiency', city = 'city', street = 'street', plaque = 123 WHERE Ncode = 34676753;
UPDATE researcher SET Side = 'me' WHERE IDre = 2;
                                 
#-------------------------------------------------



#-------------------------------------------------



#-------------------------------------------------

CREATE PROCEDURE `edit_researcher`(
    IN in_Ncode int,
	IN in_Side VARCHAR(10),
	in in_fname VARCHAR(20),
	in in_lname VARCHAR(255),
	in in_dateofbirth date,
	in in_tel int,
	in in_email VARCHAR(30),
	in in_proficiency VARCHAR(20),
	in in_city VARCHAR(15),
	in in_street VARCHAR(15),
	in in_plaque int,
    OUT out_result VARCHAR(255)
  )
BEGIN


    UPDATE researcher SET Side = in_side WHERE IDre = in_IDre;

    UPDATE personality SET fname = in_fname, lname = in_lname, dateofbirth = in_dateofbirth, tel = in_tel, email = in_email, proficiency = in_proficiency, city = in_city, street = in_street, plaque = in_plaque WHERE Ncode = in_Ncode;

    SET out_result = 'Delete operation successful';
END

#---------------------------



#-----------------------------------





create table activity(
IDac int unique not null,
IDtitle varchar(40) not null,
primary key (IDac),
IDre int unique not null not null,
IDsu int unique not null, 
foreign key (IDre) references researcher (IDre) on delete cascade on update cascade,
foreign key (IDsu) references superrisor (IDsu) on delete cascade on update cascade
);





/* create table tel (
Ncode int unique not null, 
tel int unique ,
primary key (Ncode, tel),
foreign key (Ncode) references personality (Ncode)
on delete cascade 
on update cascade
); */



/* create table professor (
IDpro int unique not null,
IDre int unique not null,
primary key (IDpro),
foreign key (IDre) references researcher (IDre)
on delete cascade
on update cascade
);
create table Science_committee(
IDsc int unique not null,
IDre int unique not null,
primary key (IDsc),
foreign key (IDre) references researcher (IDre)
on delete cascade
on update cascade
); */
/* create table student(
IDst int unique not null,
IDre int unique not null,
primary key (IDst),
foreign key (IDre) references researcher (IDre)
on delete cascade
on update cascade
); */
/* create table employee(
IDem int unique not null,
IDre int unique not null,
primary key (IDem),
foreign key (IDre) references researcher (IDre)
on delete cascade
on update cascade
); */