# SQL y bases de datos relacionales

Aprendizajes de la última sesión:

```txt
- No importa cuánto te prepares, siempre habrán imprevistos.
- Los problemas de compatibilidad no son la excepción, son la regla.
- Hay que apoyarnos de nuestros compañeros.
- Respira e inténtalo de nuevo.
```

## Instalación de MySQL

### 1. Ubuntu Linux

Instalar el motor (engine) de MySQL a través de la terminal de Ubuntu. Si no es la primera vez que se lleva a cabo este proceso, es conveniente asegurarse que no esté previamente instalado. [Pasos para **desinstalar completamente MySQL de Ubuntu**](https://linuxscriptshub.com/uninstall-completely-remove-mysql-ubuntu-16-04/).

1. Abrir una ventana de la terminal.
2. Correr el siguiente comando:
   
```bash
sudo apt-get update
```

3. Ingresar la contraseña de la máquina.
4. Instalar el servicio de MySQL corriendo el comando siguiente. Cada vez que nos pregunte si deseamos continuar, indicar que sí.

```bash
sudo apt-get install mysql-server
```

5. Para verificar que ha quedado correctamente instalado, revisar la versión mediante el siguiente comando.

```bash
mysql --version
```

Ya que hayamos verificado que MySQL quedó correctamente instalado, es momento de instalar MySQL Workbench.

1. Abrir el instalador de [**Software de Ubuntu**](https://en.wikipedia.org/wiki/Ubuntu_Software_Center).
2. Buscar MySQL Workbench y descargarlo.

#### Alternativas de instalación en Ubuntu

Después de múltiples instalaciones en distintas máquinas, nos enfrentamos contra el mismo problema de la configuración de MySQL. Para resolverlo aquí dejo una serie de pasos que pueden ser llevados a cabo desde la terminal. Revisemos 3 alternativas para una máquina con Ubuntu.

**Alternativa 1**:

```bash
# Comandos de la terminal.
sudo apt update
sudo apt install mysql-server
sudo mysql

# Comandos de mysql.
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
FLUSH PRIVILEGES;
exit

# Comandos de la terminal.
mysql -u root -p
```

**Alternativa 2**:

```bash
# Comandos de la terminal.
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation

# Respuestas dentro de la configuración de mysql.
VALIDATE-PASSWORD: Y
LEVEL-OF-PASSWORD-VALIDATION: 0
SET-NEW-PASSWORD: password
CONTINUE-WITH-PROVIDED-PASS: Y
REMOVE-ANONYMOUS-USERS: Y
DISALLOW-REMOTE-LOGIN: Y
REMOVE-TEST-DATABASE: Y
RELOAD-PRIVILEGE-TABLES: Y
ALL-DONE!

# Comandos de la terminal.
sudo mysql -u root
```

**Alternativa 3**:

```bash
# Comandos de la terminal.
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation

# Respuestas dentro de la configuración de mysql.
VALIDATE-PASSWORD: Y
LEVEL-OF-PASSWORD-VALIDATION: 0
SET-NEW-PASSWORD: password
CONTINUE-WITH-PROVIDED-PASS: Y
REMOVE-ANONYMOUS-USERS: Y
DISALLOW-REMOTE-LOGIN: Y
REMOVE-TEST-DATABASE: Y
RELOAD-PRIVILEGE-TABLES: Y
ALL-DONE!

# Comandos de la terminal.
sudo mysql -u root -p

# Comandos de mysql.
use mysql;
UPDATE user SET plugin='mysql_native_password' WHERE User='root';
UPDATE mysql.user SET authentication_string=PASSWORD('thisisaSTRONGpassword') WHERE user='root';
FLUSH PRIVILEGES;
exit

# Comandos de la terminal.
mysql -u root -p
```

### 2. Unix Mac

1. Descargar y correr el instalador de [**MySQL Community Server**](https://dev.mysql.com/downloads/mysql/).
2. Descargar y correr el instalador de [**MySQL Workbench**](https://dev.mysql.com/downloads/workbench/).

Cuando se está instalando **MySQL Community Server** se debe definir la constraseña de `root`. Asegurate de no olvidarla.

3. Añadir mysql al PATH.

```bash
# Current Session
export PATH=${PATH}:/usr/local/mysql/bin
# Permanantly
echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.bash_profile
```

Por default, el servidor de MySQL se correrá al iniciar el computador. Para correr, detener y reiniciar el servidor de MySQL desde la terminal, correr los siguientes comandos.

**Correr MySQL**:

```bash
sudo /usr/local/mysql/support-files/mysql.server start
```

**Detener MySQL**:

```bash
sudo /usr/local/mysql/support-files/mysql.server stop
```

**Reiniciar MySQL**:

```bash
sudo /usr/local/mysql/support-files/mysql.server restart
```

Este mismo proceso puede ser llevado a cabo desde **Preferencias del Sistema** en el menú  de Apple. Seleccionar MySQL panel, y hacer click en "Start MySQL Server". Si el servidor está corriendo, el mismo botón dirá "Stop MySQL Server".

## Introducción a SQL

- Está basado en un modelo relacióanl de datos.
- Por lo general, todos los gestores de bases de datos utilizan SQL.
- SQL utiliza tablas, con filas y columnas.
- Las tablas se pueden relacionar entre ellas por medio de llaves.

## Sistema gestor de bases de datos (DBMS)

Un sistema gestor de bases de datos es un software diseñado para definir, manipular, extraer y manejar datos dentro de una base de datos. El sistema generalmente manipula los datos, el formato de los datos, los nombres de los campos, la estructura de los registros y archivos. También define las reglas para validar y manipular los datos.

Algunos ejemplos de sistemas gestores de bases de datos:

- MySQL
- SQL Server
- Oracle
- dBASE
- FoxPro

## MySQL

- Sistema gestor de bases de datos relacionales abierto (open-source).
- Utiliza el lenguaje SQL (Structured Query Language).
- Una base de datos lider en el desarrollo de aplicaciones web.
- Utilizada en aplicaciones pequeñas y en grandes compañías.
- Utilizada con múltiples lenguajes: PHP, node, python, C#.
- Multi plataforma: Windows, Mac, Linux.

## Las tareas del Administrador

Dentro de esta sección vamos a crear una base de datos nueva en MySQL y generar una conexión directa con esa base de datos.

Además, se revisarán algunos comandos básicos para la administración de las bases de datos y usuarios.

### 1. Abrir Workbench

- Levantar una conexión con el servidor local.
- Hostname: `localhost`
- Port: `3306`
- User: `root`
- Utilizar el password definido para root.

### 2. Generar un nuevo Schema

Revisar los schemas que actualmente tenemos.

```sql
SHOW DATABASES;
```

Respuesta:

```txt
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

Crear una nueva base de datos (Schema) con el siguiente comando desde Workbench.

```sql
CREATE DATABASE firstdb;
```

Asegurarse de que la base de datos haya sido creada, utilizando refresh en Workbench.

### 3. Crear una nueva conexión

1. Salirse de la sesión actual de MySQL Workbench.
2. Desde el home de Workbench buscar el símbolo de más (+) junto a **MySQL Connections**.
3. Utilizando los mismos parámetros de la conexión local, agregar como default schema el nuevo que acabamos de crear. En este caso `firstdb`.
4. Abrimos la nueva conexión y observamos cómo entramos directamente al schema con el que vamos a trabajar.

### 4. Comandos adicionales del Administrador

#### 4.1 Administrar las bases de datos.

**Crear** una nueva base de datos.

```sql
CREATE DATABASE acme;
```

**Eliminar** una base de datos.

```sql
DROP DATABASE acme;
```

**Seleccionar** una base de datos.

```sql
USE acme;
```

#### 4.2 Administrar a los usuarios.

Mostrar todos los usuarios de una base de datos.

```sql
SELECT User, Host FROM mysql.user;
```

Respuesta:

```txt
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+
4 rows in set (0.00 sec)
```

Para crear un usuario nuevo debemos correr el siguiente comando.

```sql
CREATE USER 'jose'@'localhost' IDENTIFIED BY '123456';
```

El valor `123456` es el password. Para eliminar el usuario, podemos utilizar el comando `DROP`.

```sql
DROP USER 'jose'@'localhost';
```

#### 4.3 Conceder todos los privilegios a un usuario

```sql
GRANT ALL PRIVILEGES ON * . * TO 'jose'@'localhost';
FLUSH PRIVILEGES;
```

Si deseamos revisar los privilegios de un usuario en particular, podemos revisar todo lo que el usuario puede hacer con el siguiente comando.

```sql
SHOW GRANTS FOR 'jose'@'localhost';
```

Para remover los privilegios de un usuario.

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'jose'@'localhost';
```

## Tipos de datos en SQL

- **Numeric**: `INT`, `TINYINT`, `BIGINT`, `FLOAT`.
- **String**: `VARCHAR`, `TEXT`, `CHAR`.
- **Dates**: `DATE`, `DATETIME`, `TIMESTAMP`.
- **Other**: `BINARY`, `JSON`.

Los tipos de datos `CHAR` y `VARCHAR`, por lo general, son declarados con una longitud que indica el número máximo de caracteres que sea desan almacenar. Por ejemplo, `CHAR(30)` indica que dicha variable puede almacenar hasta 30 caracteres.

La longitud de la columna `CHAR` se fija al valor que haya sido declarado y puede ir desde 0 hasta 255.

Los valores en las columnas declaradas como `VARCHAR` son cadenas de caracteres con una longitud variable. La longitud puede id desde 0 hasta 65,535. `VARCHAR` es perfecto para nombres, emails y pequeños textos. Se puede utilizar `TEXT` para almacenar texto largos, como los post en un blog.

No existe explícitamente un valor de tipo `BOOL`. `TINYINT(1)` es utilizado para representar valores booleanos con 0 y 1. El valor cero es considerado **falso**, y cualquier valor distinto de cero es considerado **verdadero**.

Correr los siguientes comandos en MySQL para **evaluar los resultados**.

```sql
mysql> SELECT IF(0, 'true', 'false');
# +------------------------+
# | IF(0, 'true', 'false') |
# +------------------------+
# | false                  |
# +------------------------+

mysql> SELECT IF(1, 'true', 'false');
# +------------------------+
# | IF(1, 'true', 'false') |
# +------------------------+
# | true                   |
# +------------------------+

mysql> SELECT IF(2, 'true', 'false');
# +------------------------+
# | IF(2, 'true', 'false') |
# +------------------------+
# | true                   |
# +------------------------+
```

## Inserting new data






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











La llave primaria, `Primary Key`, es el identificador único de los elementos dentro de una tabla. Los nombres o apellidos no deben ser utilizados como llave primaria porque pueden llegar a repetirse dentro de las columnas, en su lugar se debe de definir un id.








# SQL and Relational Databases

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

