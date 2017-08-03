.read sp17data.sql
.read su17data.sql

CREATE TABLE obedience AS
select seven, image FROM students AS obedience;  

CREATE TABLE smallest_int AS
  select time, smallest FROM students AS smallest_int WHERE smallest >5 ORDER BY smallest LIMIT 20; 

CREATE TABLE greatstudents AS
  select a.date, a.color, a.pet, a.number, b.number FROM students AS a, sp17students as b WHERE a.date=b.date AND a.color= b.color AND a.pet=b.pet;  

CREATE TABLE sevens AS
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE matchmaker AS
  select "REPLACE THIS LINE WITH YOUR SOLUTION";
