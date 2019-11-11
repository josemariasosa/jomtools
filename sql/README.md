# Relational Databases

- Based on relational model of data.
- Virtually, all relational database management system uses SQL to manage them.
- Uses tables with columns and rows.
- Tables can relate to each other using keys.

Tables and data types:

- **Numeric**: `INT`, `TINYINT`, `BIGINT`, `FLOAT`.
- **String**: `VARCHAR`, `TEXT`, `CHAR`.
- **Dates**: `DATE`, `DATETIME`, `TIMESTAMP`.
- **Other**: `BINARY`, `JSON`.

There is not an explicit Boolean type, so commonly, `TINYINT` is used for booleans with 1 and 0. `VARCHAR` is great for names, emails, and small texts (255 chars). `TEXT` is for long texts, like blog posts.

The `primary key` is the unique identifier of the elements in the table. You don't want to use the name, or any other field that can be duplicated among the rows, for the primary key, so instead you should use an id.

## Database Management System (DBMS)

A database management system (DBMS) is a software package designed to define, manipulate, retrieve and manage data in a database. A DBMS generally manipulates the data itself, the data format, field names, record structure and file structure. It also defines rules to validate and manipulate this data.

A DBMS relieves users of framing programs for data maintenance. Fourth-generation query languages, such as SQL, are used along with the DBMS package to interact with a database.

Some other DBMS examples include:

- MySQL
- SQL Server
- Oracle
- dBASE
- FoxPro

## MySQL

- Open source relational DBMS.
- Uses the SQL (Structured Query Language).
- A leading database for web applications.
- Used from small applications to large enterprises.
- Used with multiple languages: PHP, node, python, C#.
- Cross platform: Windows, Mac, Linux.

## Basic SQL commands

### 1. Show Users

```sql
SELECT User, Host FROM mysql.user;
```

Response:

```text
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| root             | %         |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+
5 rows in set (0.01 sec)
```

### 2. Create a user

```sql
CREATE USER 'jose'@'localhost' IDENTIFIED BY '123456';
```

The `123456` is the password. To delete the user, we can use the `DROP` command.

```sql
DROP USER 'jose'@'localhost';
```

### 3. Granting privileges to a user

```sql
GRANT ALL PRIVILEGES ON * . * TO 'jose'@'localhost';
FLUSH PRIVILEGES;
```

If we want to check the privileges for a certain user, we can see all the stuff the user can do, using the following command:

```sql
SHOW GRANTS FOR 'jose'@'localhost';
```

To remove privileges, we use:

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'jose'@'localhost';
```

### 4. Create and manage databases

Show all the databases.

```sql
SHOW DATABASES;
```

Response:

```text
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test_db            |
+--------------------+
5 rows in set (0.00 sec)
```

To create a new database.

```sql
CREATE DATABASE acme;
```

To delete a database.

```sql
DROP DATABASE acme;
```

To select a database.

```sql
USE acme;
```

### 5. Create Table

```sql
CREATE TABLE users(
id INT AUTO_INCREMENT,
   first_name VARCHAR(100),
   last_name VARCHAR(100),
   email VARCHAR(50),
   password VARCHAR(20),
   location VARCHAR(100),
   department VARCHAR(100),
   is_admin TINYINT(1),
   register_date DATETIME,
   PRIMARY KEY(id)
);
```

To delete a table.

```sql
DROP TABLE tablename;
```

To show all the tables.

```sql
SHOW TABLES;
```

Response:

```text
+-------------------+
| Tables_in_test_db |
+-------------------+
| trips             |
+-------------------+
1 row in set (0.00 sec)
```

### 6. Create records in a table

For this exercise we load a full CSV file using the MySQL client. But you can also load individual and multiple records using the following commands.

```sql
INSERT INTO users(first_name, last_name, email, password, location, department, is_admin, register_date) VALUES ('John', 'Doe', 'john@gmail.com', '1233456', 'Jalisco', 'Data Science', 1, now());

SELECT * FROM users;
```

Response:

```text
+----+------------+-----------+----------------+----------+----------+--------------+----------+---------------------+
| id | first_name | last_name | email          | password | location | department   | is_admin | register_date       |
+----+------------+-----------+----------------+----------+----------+--------------+----------+---------------------+
|  1 | John       | Doe       | john@gmail.com | 1233456  | Jalisco  | Data Science |        1 | 2019-11-05 01:58:44 |
+----+------------+-----------+----------------+----------+----------+--------------+----------+---------------------+
1 row in set (0.00 sec)
```

Insert multiple records:

```sql
INSERT INTO users (first_name, last_name, email, password, location, department,  is_admin, register_date) values ('Fred', 'Smith', 'fred@gmail.com', '123456', 'New York', 'design', 0, now()), ('Sara', 'Watson', 'sara@gmail.com', '123456', 'New York', 'design', 0, now()),('Will', 'Jackson', 'will@yahoo.com', '123456', 'Rhode Island', 'development', 1, now()),('Paula', 'Johnson', 'paula@yahoo.com', '123456', 'Massachusetts', 'sales', 0, now()),('Tom', 'Spears', 'tom@yahoo.com', '123456', 'Massachusetts', 'sales', 0, now());
```

### 7. Queries to our tables

#### 7.1 Select

The `SELECT` command help us filtering the columns of our table. To get a grasp of the columns of our table, run the following command:

```sql
DESCRIBE my_table;
```

Response:

```text
+-----------------------+--------------+------+-----+---------+----------------+
| Field                 | Type         | Null | Key | Default | Extra          |
+-----------------------+--------------+------+-----+---------+----------------+
| trip_id               | int(11)      | NO   | PRI | NULL    | auto_increment |
| Genero_Usuario        | varchar(255) | NO   |     | NULL    |                |
| Edad_Usuario          | int(11)      | YES  |     | NULL    |                |
| Bici                  | int(11)      | YES  |     | NULL    |                |
| Ciclo_Estacion_Retiro | varchar(255) | NO   |     | NULL    |                |
| Fecha_Retiro          | varchar(255) | NO   |     | NULL    |                |
| Hora_Retiro           | varchar(255) | YES  |     | NULL    |                |
| Ciclo_Estacion_Arribo | varchar(255) | YES  |     | NULL    |                |
| Fecha_Arribo          | varchar(255) | YES  |     | NULL    |                |
| Hora_Arribo           | varchar(255) | YES  |     | NULL    |                |
+-----------------------+--------------+------+-----+---------+----------------+
10 rows in set (0.01 sec)
```

Having this info in hand, let's run some `SELECT` commands.

```sql
SELECT * FROM trips;
```

The response of this command is the whole table, so maybe we just want to get the trip_id and the user gender, so let specify that.

```sql
SELECT trip_id, Genero_Usuario FROM trips;
```

Response:

```
+---------+----------------+
| trip_id | Genero_Usuario |
+---------+----------------+
|       1 | M              |
|       2 | M              |
|       3 | M              |
|     ... | ...            |
|     998 | F              |
|     999 | M              |
|    1000 | F              |
+---------+----------------+
1000 rows in set (0.00 sec)
```

#### 7.2 Where

The `WHERE` statement help us filter our results, keep only records that match a condition.

```sql
SELECT * FROM trips WHERE Edad_Usuario > 30;
```

Some more examples using `AND` and `OR` statements.

```sql
SELECT * FROM users WHERE location='Massachusetts';
SELECT * FROM users WHERE location='Massachusetts' AND department='sales';
SELECT * FROM users WHERE location='Massachusetts' OR location='Jalisco';
SELECT * FROM users WHERE is_admin = 1;
SELECT * FROM users WHERE is_admin > 0;
```

#### 7.3 Sorting

Using the `ORDER BY` statement to sort the results in an ascending, `ASC`, or descending, `DESC`, way.

```sql
SELECT * FROM users ORDER BY last_name ASC;
SELECT * FROM users ORDER BY last_name DESC;
```

#### 7.4 Concatenate multiple columns

```sql
SELECT trip_id, CONCAT(Genero_Usuario, ' - ', Edad_Usuario) AS 'User' FROM trips;
```

Response:

```txt
+---------+--------+
| trip_id | User   |
+---------+--------+
|       1 | M - 53 |
|       2 | M - 48 |
|       3 | M - 63 |
|     ... | ...    |
|     998 | F - 43 |
|     999 | M - 27 |
|    1000 | F - 43 |
+---------+--------+
1000 rows in set (0.01 sec)
```

#### 7.5 Distinct values

```sql
SELECT DISTINCT Genero_Usuario FROM trips;
```

Response:

```txt
+----------------+
| Genero_Usuario |
+----------------+
| M              |
| F              |
+----------------+
2 rows in set (0.00 sec)
```

#### 7.6 Between

In order to select a range of values, we use the `BETWEEN` statement.

```sql
SELECT * FROM users WHERE age BETWEEN 20 AND 25;
```

#### 7.7 Like

The `LIKE` statement help us searching non specific values in our tables.

```sql
SELECT * FROM users WHERE department LIKE 'd%';
SELECT * FROM users WHERE department LIKE 'dev%';
SELECT * FROM users WHERE department LIKE '%t';
SELECT * FROM users WHERE department LIKE '%e%';
```

'd%' - starts with d, with dev.

#### 7.8 Not

Querying users that does not start with the letter `d`.

```sql
SELECT * FROM users WHERE department NOT LIKE 'd%';
```

Some more complex query using `NOT`, `IN`, and `AND`.

```sql
SELECT * FROM trips WHERE Edad_Usuario NOT IN (50, 30, 20) AND Bici IN (10643, 9648, 9929);
```

#### 7.9 In

```sql
SELECT * FROM users WHERE department IN ('design', 'sales');
```

### 8. More operations in our tables

#### 8.1 Deleting rows

Make sure that whenever you use a delete statement you add the where clause, cause if not you can be deleting all of your records at once!

```sql
DELETE FROM users WHERE id = 6;
```

#### 8.2 Updating rows

It is important to use the where statement, cause otherwise all of the users are going to have the same new email.

```sql
UPDATE users SET email = 'freddy@gmail.com' WHERE id = 2;
```

#### 8.3 Inserting a new column

```sql
ALTER TABLE users ADD age VARCHAR(3);
```

Remember, we can manually update the values of the table directly in the SQL workbench.


#### 8.4 Modify a column

Change the type of a row.

```sql
ALTER TABLE users MODIFY COLUMN age INT(3);
```

### 9. Indexes

Indexes are used in columns and tables to speed up queries and find things more quickly and effectively. Primary keys like our id are indexed, but we can generate custom indexes too. You should use indexes in the fields you are going to be searching by a lot.

Imagine we have an application that is going to be searching a lot by the location. `LIndex` is just the name we define for the location index.

```sql
CREATE INDEX LIndex On users(location);
DROP INDEX LIndex ON users;
```

#### 9.1 Foreign Key

Creating a table with a foreign key.

```sql
CREATE TABLE posts(
id INT AUTO_INCREMENT,
   user_id INT,
   title VARCHAR(100),
   body TEXT,
   publish_date DATETIME DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY(id),
   FOREIGN KEY (user_id) REFERENCES users(id)
);
``` 

