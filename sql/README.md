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

- Está basado en un modelo relaciónal de datos.
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

## Ingresando nuevos datos

### 1. Crear y eliminar una tabla.

Para crear una tabla nueva, debemos indicar:

- todos los campos que ha de llevar
- los tipos de datos que se van a almacenar
- especificar la longitud máxima de los campos
- establecer un primary key

La llave primaria, `Primary Key`, es el identificador único de los elementos dentro de una tabla. Los nombres o apellidos no deben ser utilizados como llave primaria porque pueden llegar a repetirse dentro de las columnas, en su lugar se debe definir un id.

Dentro de nuestra base de datos `fristdb` vamos a crear una tabla de usuarios que contenga la siguient información.

```sql
CREATE TABLE users(
   id INT AUTO_INCREMENT,
   nombre VARCHAR(100),
   apellido VARCHAR(100),
   email VARCHAR(50),
   password VARCHAR(20),
   ciudad VARCHAR(100),
   departamento VARCHAR(100),
   is_admin TINYINT(1),
   fecha_registro DATETIME,
   PRIMARY KEY(id)
);
```

Podemos observar cómo la tabla está creada, utilizando el comando `SHOW`, o dentro de Workbench debajo de nuestro schema.

```sql
SHOW TABLES;
# +-------------------+
# | Tables_in_firstdb |
# +-------------------+
# | users             |
# +-------------------+
# 1 row in set (0.00 sec)
```

Si quisiéramos borrar la tabla, podríamos utilizar el comando `DROP`.

```sql
DROP TABLE tablename;
```

### 2. Insertar registros nuevos.

Para poder visualizar valores dentro de nuestra tabla, hay que insertar **una fila nueva**.

```sql
INSERT INTO users(
   nombre,
   apellido,
   email,
   password,
   ciudad,
   departamento,
   is_admin,
   fecha_registro) VALUES (
   'Maria',
   'Campos',
   'campos@gmail.com',
   '1233456',
   'Guadalajara',
   'desarrollo',
   1,
   now());

SELECT * FROM users;
```

Resultado:

```text
+----+--------+----------+------------------+----------+-----------+--------------+----------+---------------------+
| id | nombre | apellido | email            | password | ciudad | departamento | is_admin | fecha_registro      |
+----+--------+----------+------------------+----------+-----------+--------------+----------+---------------------+
|  1 | Maria  | Campos   | campos@gmail.com | 1233456  | Guadalajara   | desarrollo   |        1 | 2019-11-13 07:50:04 |
+----+--------+----------+------------------+----------+-----------+--------------+----------+---------------------+
1 row in set (0.00 sec)
```

Si observamos con detalle, la **columna de id** se creó de manera automática y esperamos se vaya incrementado con cada registro nuevo. Ahora insertemos **múltiples registros** de una sola vez.

La función **now()** de MySQL nos permite generar automáticamente un valor con la fecha y hora actual.

```sql
INSERT INTO users (nombre, apellido, email, password, ciudad, departamento,  is_admin, fecha_registro) values ('Alfredo', 'Estevan', 'alfredo@gmail.com', '123456', 'Monterrey', 'diseño', 0, now()), ('Sara', 'Ibarra', 'sara@gmail.com', '123456', 'Monterrey', 'diseño', 0, now()),('Andrés', 'Sosa', 'andy@yahoo.com', '123456', 'Mérida', 'desarrollo', 1, now()),('Paula', 'García', 'paula@yahoo.com', '123456', 'Guadalajara', 'ventas', 0, now()),('Roberto', 'Ibanez', 'roberto@yahoo.com', '123456', 'Guadalajara', 'ventas', 0, now());
```

#### Ejercicio

1. Cómo podríamos visualizar la información de los usuarios de Guadalajara.
2. Cómo podríamos visualizar la información de los desarrolladores en Guadalajara.
3. Cómo podríamos visualizar el nombre y apellido de las personas de desarrollo y diseño.
4. Cuántos usuarios pertenecen a Guadalajara.

Respuestas.

```sql
# Respuesta 1
SELECT * FROM users WHERE ciudad='Guadalajara';

# Respuesta 2
SELECT * FROM users WHERE ciudad='Guadalajara' AND departamento='desarrollo';

# Respuesta 3
SELECT nombre, apellido, departamento FROM users WHERE departamento='desarrollo' OR departamento='diseño';

# Respuesta 4
SELECT COUNT(*) AS 'total' FROM users WHERE ciudad='Guadalajara';
```

### 3. Insertar registros nuevos a partir de un archivo.

Descargar el archivo con 1000 registros del [*Sitema de Mibici de Guadalajara*](https://raw.githubusercontent.com/josemariasosa/jomtools-data/master/sql/exercises/1-setup/mibici.csv). 

El archivo se puede desacargar directamente de la terminal utilizando el comando de `curl` y añadiendo una ubicación destino.

```bash
curl https://raw.githubusercontent.com/josemariasosa/jomtools-data/master/sql/exercises/1-setup/mibici.csv >> mibici.csv
```

Para poder ingresar los valores de nuestro archivo CSV, primero debemos generar una tabla nueva.

```sql
CREATE TABLE IF NOT EXISTS trips (
    trip_id INT AUTO_INCREMENT,
    Genero_Usuario VARCHAR(255) NOT NULL,
    Edad_Usuario INT,
    Bici INT,
    Ciclo_Estacion_Retiro VARCHAR(255) NOT NULL,
    Fecha_Retiro VARCHAR(255) NOT NULL,
    Hora_Retiro VARCHAR(255),
    Ciclo_Estacion_Arribo VARCHAR(255),
    Fecha_Arribo VARCHAR(255),
    Hora_Arribo VARCHAR(255),
    PRIMARY KEY (trip_id)
)  ENGINE=INNODB;
```

**InnoDB** es el motor de almacenamiento de la base de datos MySQL. Es el sistema que se utiliza por default, por lo tanto, no requiere aparecer explícitamente. Si se desean revisar más características ir a la [**documentación de MySQL**](https://dev.mysql.com/doc/refman/8.0/en/using-innodb-tables.html).

Observemos cuáles son las tablas con las que contamos en nuestra base de datos.

```sql
SHOW TABLES;
# +-------------------+
# | Tables_in_firstdb |
# +-------------------+
# | trips             |
# | users             |
# +-------------------+
# 2 rows in set (0.00 sec)
```

Para cargar los archivos desde un file, vayamos a MySQL Workbench y corramos el siguiente comando:

```sql
SELECT * FROM trips;
```

En la parte superior de los resultados podemos ver la opción `Export/Import`, presionemos el botón de importar y sigamos los pasos. Una vez cargados todos los datos corramos el mismo comando para verificar si han sido ingresados correctamente.

#### Ejercicio

1. Selecciona todos los viajes con usuarios con edad arriba de 30.
2. Selecciona todos los viajes empezados después de las 5 de la tarde hechos por una mujer.
3. Regresame los identificadores de las estaciones retiradas antes de las 8 de la mañana y después de las 5 de la tarde.

```sql
# Respuesta 1
SELECT * FROM trips WHERE Edad_Usuario > 30;

# Respuesta 2
SELECT * FROM trips WHERE Hora_Retiro > '17:00:00' and Genero_Usuario = 'F';

# Respuesta 3
SELECT Ciclo_Estacion_Retiro FROM trips WHERE Hora_Retiro > '17:00:00' OR Hora_Retiro < '8:00:00';
```

## Select

El comando `SELECT` nos ayuda a filtrar las columnas de nuestra tabla. Para generar una descripción de cualquier tabla y mirar las columnas que tiene podemos utilizar el comando de `DESCRIBE`.

```sql
DESCRIBE users;
# +----------------+--------------+------+-----+---------+----------------+
# | Field          | Type         | Null | Key | Default | Extra          |
# +----------------+--------------+------+-----+---------+----------------+
# | id             | int(11)      | NO   | PRI | NULL    | auto_increment |
# | nombre         | varchar(100) | YES  |     | NULL    |                |
# | apellido       | varchar(100) | YES  |     | NULL    |                |
# | email          | varchar(50)  | YES  |     | NULL    |                |
# | password       | varchar(20)  | YES  |     | NULL    |                |
# | ciudad         | varchar(100) | YES  |     | NULL    |                |
# | departamento   | varchar(100) | YES  |     | NULL    |                |
# | is_admin       | tinyint(1)   | YES  |     | NULL    |                |
# | fecha_registro | datetime     | YES  |     | NULL    |                |
# +----------------+--------------+------+-----+---------+----------------+
# 9 rows in set (0.00 sec)
```

Teniendo esta información a la mano, corramos algunos comandos `SELECT`.

```sql
SELECT * FROM users;
```

La respuesta de este comando es la tabla completa. Si quisieramos regresar solo los valores del email y ciudad, debemos especificarlos.

```sql
SELECT email, ciudad FROM users;
# +-------------------+-------------+
# | email             | ciudad      |
# +-------------------+-------------+
# | campos@gmail.com  | Guadalajara |
# | alfredo@gmail.com | Monterrey   |
# | sara@gmail.com    | Monterrey   |
# | andy@yahoo.com    | Mérida      |
# | paula@yahoo.com   | Guadalajara |
# | roberto@yahoo.com | Guadalajara |
# +-------------------+-------------+
# 6 rows in set (0.00 sec)
```

## Where

El comando `WHERE` nos ayuda a filtrar los resultados, manteniendo únicamente los que cumplen con cierta condición.

```sql
SELECT * FROM users WHERE ciudad='Guadalajara';
```

Los comandos `AND` y `OR` nos permiten generar consultas más completas.

```sql
SELECT * FROM users WHERE ciudad='Guadalajara' AND departamento='desarrollo';

SELECT nombre, apellido, departamento FROM users WHERE departamento='desarrollo' OR departamento='diseño';
```

## Ordenar los resultados

El comando `ORDER BY` nos permite ordenar los resultados de manera ascendente, `ASC`, o descendente, `DESC`.

```sql
SELECT nombre, apellido FROM users ORDER BY apellido ASC;
# +---------+----------+
# | nombre  | apellido |
# +---------+----------+
# | Maria   | Campos   |
# | Alfredo | Estevan  |
# | Paula   | García   |
# | Roberto | Ibanez   |
# | Sara    | Ibarra   |
# | Andrés  | Sosa     |
# +---------+----------+
# 6 rows in set (0.00 sec)

SELECT nombre, apellido FROM users ORDER BY apellido DESC;
# +---------+----------+
# | nombre  | apellido |
# +---------+----------+
# | Andrés  | Sosa     |
# | Sara    | Ibarra   |
# | Roberto | Ibanez   |
# | Paula   | García   |
# | Alfredo | Estevan  |
# | Maria   | Campos   |
# +---------+----------+
# 6 rows in set (0.00 sec)
```

Si se desea ordenar por más de una columna se especifica después de `ORDER BY` las columnas, en base al orden de prioridad.

```sql
SELECT ciudad, departamento, email FROM users ORDER BY ciudad ASC, departamento DESC;
# +-------------+--------------+-------------------+
# | ciudad      | departamento | email             |
# +-------------+--------------+-------------------+
# | Guadalajara | ventas       | paula@yahoo.com   |
# | Guadalajara | ventas       | roberto@yahoo.com |
# | Guadalajara | desarrollo   | campos@gmail.com  |
# | Mérida      | desarrollo   | andy@yahoo.com    |
# | Monterrey   | diseño       | alfredo@gmail.com |
# | Monterrey   | diseño       | sara@gmail.com    |
# +-------------+--------------+-------------------+
```

## Concatenar múltiples columnas

```sql
SELECT id, CONCAT(nombre, ' ', apellido) AS 'User', email FROM users;
# +----+-----------------+-------------------+
# | id | User            | email             |
# +----+-----------------+-------------------+
# |  1 | Maria Campos    | campos@gmail.com  |
# |  2 | Alfredo Estevan | alfredo@gmail.com |
# |  3 | Sara Ibarra     | sara@gmail.com    |
# |  4 | Andrés Sosa     | andy@yahoo.com    |
# |  5 | Paula García    | paula@yahoo.com   |
# |  6 | Roberto Ibanez  | roberto@yahoo.com |
# +----+-----------------+-------------------+
# 6 rows in set (0.00 sec)
```

## Obtener los valores únicos

```sql
SELECT DISTINCT departamento FROM users;
# +--------------+
# | departamento |
# +--------------+
# | desarrollo   |
# | diseño       |
# | ventas       |
# +--------------+
# 3 rows in set (0.00 sec)
```

#### Ejercicio

1. Cuáles son las ciudades distintas, ordenadas alfabéticamente.
2. Cuántas ciudades diferentes existen.

```sql
# Respuesta 1
SELECT DISTINCT ciudad FROM users ORDER BY ciudad ASC;

# Respuesta 2
SELECT COUNT(DISTINCT ciudad) AS 'Total' from users;
```

## Filtrado avanzado

### 1. Between

Para hacer obtener registros que se encuentren dentro de un rango de valores, utilizamos `BETWEEN`.

```sql
SELECT * FROM trips WHERE Edad_Usuario BETWEEN 20 AND 25;
```

#### Ejercicio

1. Qué porcentaje de los usuarios, de nuestra muestra de 1000 viajes, se encuentra entre el rango de edad de 20 a 25.

### 2. Like

El comando de `LIKE` nos ayuda hacer búsquedas dentro de los campos.

Queremos buscar todos los departamentos que comiencen con el texto ...

```sql
SELECT * FROM users WHERE departamento LIKE 'd%';
SELECT * FROM users WHERE departamento LIKE 'des%';
```

Que terminen con el texto ...

```sql
SELECT * FROM users WHERE departamento LIKE '%s';
```

Que incluya el siguiente texto ...

```sql
SELECT * FROM users WHERE departamento LIKE '%o%';
```

Queremos los usuarios que tengan correo de Yahoo.

```sql
SELECT * FROM users WHERE email LIKE '%yahoo%';
# +----+---------+----------+-------------------+----------+-------------+--------------+----------+---------------------+
# | id | nombre  | apellido | email             | password | ciudad      | departamento | is_admin | fecha_registro      |
# +----+---------+----------+-------------------+----------+-------------+--------------+----------+---------------------+
# |  4 | Andrés  | Sosa     | andy@yahoo.com    | 123456   | Mérida      | desarrollo   |        1 | 2019-11-13 07:59:08 |
# |  5 | Paula   | García   | paula@yahoo.com   | 123456   | Guadalajara | ventas       |        0 | 2019-11-13 07:59:08 |
# |  6 | Roberto | Ibanez   | roberto@yahoo.com | 123456   | Guadalajara | ventas       |        0 | 2019-11-13 07:59:08 |
# +----+---------+----------+-------------------+----------+-------------+--------------+----------+---------------------+
# 3 rows in set (0.00 sec)
```

### 3. Not

Si queremos hacer lo opuesto. Qué tal los departamentos que no incluyan el siguiente texto ...

```sql
SELECT * FROM users WHERE departamento NOT LIKE '%o%';
```

Y obtenemos la tabla complementaria, la que resultaría cuando la condición proporcionada no se cumple.

### 4. In

Podemos utilizar una lista, en lugar de combinar múltiples condiciones.

```sql
SELECT * FROM users WHERE departamento IN ('diseño', 'ventas');
```
#### Ejercicio

1. Leer el siguiente query y decir qué va a regresar.

  ```sql
  SELECT *
    FROM trips
    WHERE Edad_Usuario NOT IN (50, 30, 20)
    AND Bici IN (10643, 9648, 9929);
  ```

2. Selecciona todos los viajes que tengan usuarios con edades de 10, 20 y 30.

3. Selecciona todos los viajes que no tengan usuarios con edades de 35, 20 y 18.

4. Selecciona todos los viajes usuarios con edades de 35, 20 y 18 y que han usado las bicicletas 7486, 9299 y 7552.

5. Selecciona todos los viajes usuarios con edades diferentes a 50, 30 y 20 y que han usado las bicicletas 10643, 9648 y 9929.

6. Consulta el genero y edad del usuario en los viajes que terminaron a las 12 horas con x minutos.

7. Consulta el genero de los usuarios que viajaron a las 7 horas con x minutos y que son menores de edad.

```sql
# Respuesta 2
SELECT *
  FROM trips
  WHERE Edad_Usuario in (10, 20, 30);

# Respuesta 3
SELECT *
  FROM trips
  WHERE Edad_Usuario not in (35, 20, 18);

# Respuesta 4
SELECT *
  FROM trips
  WHERE Edad_Usuario IN (35, 20, 18)
  AND Bici IN (7486, 9299, 7552);

# Respuesta 5
SELECT *
  FROM trips
  WHERE Edad_Usuario NOT IN (50, 30, 20)
  AND Bici IN (10643, 9648, 9929);

# Respuesta 6
SELECT Genero_Usuario, Edad_Usuario
  FROM trips
  WHERE Hora_Arribo like '12%';

# Respuesta 7
SELECT Genero_Usuario
  FROM trips
  WHERE Hora_Retiro like '19%'
  AND Edad_Usuario < 18;
```
---

## Operaciones matemáticas

`COUNT`, `SUM`, `MAX`, `MIN` y `AVG` son **funciones** en MySQL que realizan algunos cálculos en un conjunto de valores y luego devuelve un solo valor.

### 1. COUNT, SUM y AVG

La función `SUM` calcula la suma de los valores presentes en una columna.

Hay que calcular la edad promedio de los usuarios.

```sql
SELECT SUM(Edad_Usuario)
  FROM trips;
# +-------------------+
# | sum(Edad_Usuario) |
# +-------------------+
# |             38282 |
# +-------------------+
# 1 row in set (0.00 sec)
 
SELECT SUM(Edad_Usuario)/1000
  FROM trips;
# +------------------------+
# | sum(Edad_Usuario)/1000 |
# +------------------------+
# |                38.2820 |
# +------------------------+
# 1 row in set (0.00 sec)
```

La función `AVG` nos regresa directamente el promedio, así nos ahorramos los pasos anteriores.

**¿Cómo sería el código?**

Podemos utilizar la media para crear queries más completos. Como por ejemplo, queremos hacer un query que nos regrese los viajes de todos los usuarios con edad mayor a la media.

```sql
SELECT trip_id, Edad_Usuario
  FROM trips 
  WHERE Edad_Usuario > (
  SELECT AVG(Edad_Usuario)
    FROM trips);
```

La función `COUNT` devuelve el número de filas que coinciden con un criterio específico. Como por ejemplo, cuántos usuarios están por encima de la media, y cuántos por debajo.

```sql
# Por encima de la media
SELECT COUNT(*)
  FROM trips 
  WHERE Edad_Usuario > (
  SELECT AVG(Edad_Usuario)
    FROM trips);

# Por debajo de la media
SELECT COUNT(*)
  FROM trips 
  WHERE Edad_Usuario < (
  SELECT AVG(Edad_Usuario)
    FROM trips);
```

#### Ejercicio

1. Calcular el porcentaje de usuarios, del total de 1000, que tienen una edad mayor o igual que el valor de la media.

```sql
# Respuesta 1
SELECT COUNT(*) / 1000
FROM trips
WHERE Edad_Usuario >= (
  SELECT AVG(Edad_Usuario)
    FROM trips);
```

### 2. MAX y MIN

La función `MAX` y `MIN` regresar el valor mayor y menor, respectivamente, de alguna columna seleccionada.

#### Ejercicio

1. ¿Cuántos ciclistas mujeres usaron ecobici el 1ero de Enero?

2. ¿Cuál es el promedio de la edad de los ciclistas?

3. ¿Cuántos años tenía el viajero más viejo el 27 de Enero? 

```sql
# Respuesta 1
SELECT COUNT(*) AS "cant_ciclistas_mujeres"
  FROM trips
  WHERE Fecha_Retiro LIKE '01%'
  AND Genero_Usuario = 'F';

# Respuesta 2
SELECT AVG(Edad_Usuario)
  FROM trips;

# Respuesta 3
SELECT MAX(Edad_Usuario)
  FROM trips
  WHERE Fecha_Retiro LIKE '27%';
```

## Operadores comparativos

Los operadores comparativos son utilizados dentro de una operación `WHERE` para determinar los registos que se seleccionarán. Aquí una lista con los operadores comparativos utilizados en MySQL.

| Operadores comparativos | Description                                                     |
|-------------------------|-----------------------------------------------------------------|
| =                       | Igual                                                           |
| <=>                     | Igual (Seguro para comparar valores NULL)                       |
| <>                      | Diferente                                                       |
| !=                      | Diferente                                                       |
| >                       | Mayor que                                                       |
| >=                      | Mayor o igual que                                               |
| <                       | Menor que                                                       |
| <=                      | Menor o igual que                                               |
| IN ( )                  | Encuentra valores de una lista                                  |
| NOT                     | Niega una condición                                             |
| BETWEEN                 | Dentro de un rango (inclusivo)                                  |
| IS NULL                 | Valor NULL                                                      |
| IS NOT NULL             | Valor no NULL                                                   |
| LIKE                    | Encuentra patrones utilizando % y _                             |
| EXISTS                  | Condición se cumple si el subquery regresa al menos una columna |

## Subconsultas

- Las subconsultas en SQL son consultas, dentro de otra consulta.
- Las subconsultas proporcionan datos a la consulta adjunta.
- Las subconsultas pueden regresar:
  - Listas
  - Valores únicos
- Las subconsultas deben ir entre paréntesis.

#### Ejercicio

1. Utilizando una subconsulta, regresar los trip_id como **tabla** junto con la edad, con los viajes con el usuario más joven.

2. Utilizando una subconsulta, regresar los trip_id como **lista**, con los viajes con el usuario más joven.

3. Regresar el: trip_id, Genero_Usuario, Edad_Usuario, Bici en donde el **trip_id** sea parte del la lista del ejercicio anterior.

4. Mira el siguiente código y analiza qué respuesta puede arrojar.

  ```sql
  SELECT DISTINCT((
    SELECT COUNT(*)
      FROM trips
      WHERE Fecha_Retiro LIKE '01%'
      AND Genero_Usuario = 'M') 
    / (
    SELECT COUNT(*)
      FROM trips
      WHERE Fecha_Retiro LIKE '01%'))
    AS 'TOTAL'
  FROM trips;
  ```

5. ¿Qué porcentaje de ciclistas fueron mujeres el 3 de Enero?

6. ¿Qué porcentaje de ciclistas salen a las 5 de la mañana?

```sql
# Respuesta 1
SELECT trip_id, Edad_Usuario
  FROM trips
  WHERE Edad_Usuario = (
    SELECT MIN(Edad_Usuario)
      FROM trips);

# Respuesta 2
SELECT trip_id
  FROM trips
  WHERE Edad_Usuario = (
    SELECT MIN(Edad_Usuario)
      FROM trips);

# Respuesta 3
SELECT trip_id, Genero_Usuario, Edad_Usuario, Bici
  FROM trips
  WHERE trip_id IN (
    SELECT trip_id
      FROM trips
      WHERE Edad_Usuario = (
        SELECT min(Edad_Usuario)
        FROM trips));

# Respuesta 5
SELECT count(*) FROM trips WHERE Genero_Usuario = 'F' AND Fecha_Retiro LIKE '01%'
SELECT count(*) FROM trips WHERE Fecha_Retiro LIKE '01%'

SELECT (SELECT count(*) FROM trips WHERE Genero_Usuario = 'F' AND Fecha_Retiro LIKE '01%') / (SELECT count(*) FROM trips WHERE Fecha_Retiro LIKE '01%') AS 'porcentaje';


# Respuesta 6
SELECT DISTINCT(
  (SELECT COUNT(*)
    FROM trips
    WHERE Hora_Retiro LIKE '5%') / (SELECT COUNT(*)
                                      FROM trips)
    ) AS 'porc_ciclistas_madrugaderos'
FROM trips
```

## Join

Una cláusula `JOIN` se usa para combinar filas de dos o más tablas, en función de una columna relacionada entre ellas. Existen cuatro tipos de joins.

- Inner join
- Full join `* Not in MySQL`
- Left join
- Right join

#### Ejercicio

1. Descargar los archivos en formato CSV de [**los productos**](https://docs.google.com/spreadsheets/d/1JhLMEdxBM_YqW2Db37Qf8O_PDJDpRB0QKKmQILqsjUw/edit?usp=sharing) y [**las ordenes**](https://docs.google.com/spreadsheets/d/1qjab_J_bldjtV9lN5nnUzbdKN-fcK0LFVUZGOvmVSmE/edit?usp=sharing).

2. Crear una tabla nueva para cada elemento.

3. Hacer un join para ver los productos y su precio dentro de cada orden.

4. Insertar una columna con el total de la venta por cada orden (precio * cantidad).

5. Qué pasa con los productos que están en la tabla de productos, pero no en las órdenes.

6. Qué ocurre si utilizamos `RIGHT JOIN`.

```sql
# Respuesta 2
CREATE TABLE products(
  product_id INT,
  product_name VARCHAR(100),
  price INT,
  PRIMARY KEY(product_id)
);

CREATE TABLE orders(
  order_id INT,
  product_id INT,
  quantity INT,
  PRIMARY KEY(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

# Respuesta 3
SELECT *
  FROM orders
  LEFT JOIN products USING(product_id);

# Respuesta 4
SELECT product_id, order_id, quantity, product_name, price, (quantity*price) AS Total
  FROM orders
  LEFT JOIN products USING(product_id);

# Respuesta 6
SELECT *
  FROM orders
  RIGHT JOIN products USING(product_id);
```

#### Ejercicios Adicionales

1. Utilizando [**reviewer**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/reviewer.csv) y [**rating**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/rating.csv). Escribe un query que encuentre los nombres únicos de los reviewers que hayan hecho evaluaciones mayores a 8.

```sql
SELECT DISTINCT(rev_name) AS reviewer
  FROM reviewer
  INNER JOIN rating USING(rev_id)
  WHERE rev_stars >= 8;
```

2. Utilizando [**actor**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/actor.csv) y [**movie_cast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie_cast.csv). Escribe un query que encuentre cuáles han sido los roles de Kevin Spacey.

```sql
SELECT act_fname, act_lname, role
  FROM actor
  LEFT JOIN movie_cast USING(act_id)
  WHERE act_fname = 'Kevin'
  AND act_lname = 'Spacey';
```

3. Utilizando [**actor**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/actor.csv), [**movie_cast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie_cast.csv) y [**movie**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie.csv). Escribe un query que encuentre cuáles han sido los roles y las películas de Kevin Spacey.

```sql
SELECT act_fname, act_lname, role, mov_title
  FROM actor
  LEFT JOIN movie_cast USING(act_id)
  LEFT JOIN movie USING(mov_id)
  WHERE act_fname = 'Kevin'
  AND act_lname = 'Spacey';
```

4. Utilizando [**actor**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/actor.csv), [**movie_cast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie_cast.csv) y [**movie**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie.csv). Escribe un query que regrese la lista con el primer y segundo nombre de todos los actores que estuvieron en la película `Annie Hall`, junto con los roles que tuvieron.

```sql
SELECT act_fname,act_lname,role
  FROM actor
  LEFT JOIN movie_cast USING(act_id)
  LEFT JOIN movie USING(mov_id)
  WHERE mov_title = 'Annie Hall';
```

5. Utilizando [**actor**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/actor.csv), [**movie_cast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie_cast.csv) y [**movie**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie.csv). Escribe un query que enliste todos los actores que no tuvieron participación en ninguna película entre 1990 y 2000.

```sql
SELECT act_fname, act_lname, mov_title, mov_year
  FROM actor
  LEFT JOIN movie_cast USING(act_id)
  LEFT JOIN movie USING(mov_id)
  WHERE mov_year NOT BETWEEN 1990 and 2000;
```

6. Utilizando [**movie**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie.csv) y [**rating**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/rating.csv). Escribe un query que encuentre todos los años en que se produjo un película que recibió un rating de 3 o 4, ordenar los resultados de manera incremental.

```sql
SELECT DISTINCT(mov_year)
  FROM movie
  LEFT JOIN rating USING(mov_id)
  WHERE rev_stars IN (3, 4)
  ORDER BY mov_year;
```

## Teoría de conjuntos

Unión
Intersección `* Not in MySQL`
Diferencia `* Not in MySQL`

#### Ejercicio

1. Cómo podríamos regresar todas las órdenes con una cantidad de 2 y 5. Ahora utilizando el comando de `UNION`.

```sql
# Sin unión
SELECT *
  FROM orders
  WHERE quantity IN (2, 5);

# Con unión
SELECT *
  FROM orders
  WHERE quantity = 2
  UNION
  SELECT *
    FROM trips
    WHERE quantity = 5;
```

#### Ejercicios Adicionales

1. Utilizando [**nobel_win**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/nobel_win.csv). Escribe un query para conocer el ganador del premio Nobel de 1971 en literatura.

```sql
SELECT winner
  FROM nobel_win
  WHERE year = 1971
  AND subject = 'Literature';
```

2. Utilizando [**nobel_win**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/nobel_win.csv). Escribe un query que regrese los detalles de los ganadores con un primer nombre Louis.

```sql
SELECT *
  FROM nobel_win 
  WHERE winner LIKE 'Louis%';
```

3. Utilizando [**nobel_win**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/nobel_win.csv). Escribe un query que regrese los ganadores del premio Nobel del año 1970 excepto Pysiology y Economics.

```sql
SELECT *
  FROM nobel_win
  WHERE year = 1970
  AND SUBJECT NOT IN ('Physiology', 'Economics');
```

4. Utilizando [**nobel_win**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/nobel_win.csv). Escribe un query que muestre los ganadores en Physiology en años menores a 1971 y los ganadores del precio de paz después del 1974.

```sql
SELECT * 
  FROM nobel_win
  WHERE (subject ='Physiology' AND year < 1971)
  UNION (
    SELECT *
      FROM nobel_win
      WHERE (subject ='Peace' AND year >= 1974));
```

## Más operaciones en tablas

### 1. Eliminando filas

Asegurarse de incluir el comando `WHERE` cada vez que se va a realizar una operación como esta. Sino podríamos correr el riesgo de eliminar todos los registros de una sola vez.

```sql
DELETE FROM orders WHERE order_id = 1012;
```

### 2. Actualizando columnas

Es importante utilizar el comando `WHERE` si no queremos modificar el valor de todas las filas.

```sql
UPDATE orders SET quantity = 2 order_id = 1013;
```

### 3. Insertando una nueva columna

```sql
ALTER TABLE orders ADD site VARCHAR(15);
```

Recordar que es posible utilizar el SQL Workbench directamente para modificar la información.

### 4. Modificar el tipo de una columna

```sql
ALTER TABLE users MODIFY COLUMN age INT(3);
```

## Los índices de una tabla

Los índices son utilizados en las columnas y en las tablas para acelerar los queries y encontrar información de manera más rápida y efectiva. Las llaves primarias, **Primary keys**, como el id de la orden, `order_id`, son índices, sin embargo nosotros podemos definir nuestros propios índices también. 

Se recomienda utilizar índices en todos los campos por los cuales se han de realizar múltiples búsquedas.

```sql
CREATE INDEX ProdIndex On products(product_name);
DROP INDEX ProdIndex ON products;
```

### Ejercicios Finales

Los recursos para estos ejercicios se encuentran en los archivos csv listados a continuación.

- [**actor**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/actor.csv)
- [**customer**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/customer.csv)
- [**item_mast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/item_mast.csv)
- [**movie**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie.csv)
- [**movie_cast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/movie_cast.csv)
- [**nobel_win**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/nobel_win.csv)
- [**rating**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/rating.csv)
- [**reviewer**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/reviewer.csv)
- [**sales_orders**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/sales_orders.csv)
- [**salesman**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/salesman.csv)


1. Utilizando [**salesman**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/salesman.csv). Escribe un query que regrese los nombres y las ciudades de los vendedores de Paris.

```sql
SELECT name, city
  FROM salesman
  WHERE city='Paris';
```

2. Utilizando [**sales_orders**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/sales_orders.csv). Escribe un query que regrese la información del id de todos los vendedores que han obtenido órdenes de algún cliente, sin ningún repetido.

```sql
SELECT DISTINCT salesman_id
  FROM sales_orders;
```

3. Utilizando [**item_mast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/item_mast.csv). Escribe un query que calcule el precio promedio de los productos manufacturados con el código 16.

```sql
SELECT AVG(pro_price)
  FROM item_mast 
  WHERE pro_com=16;
```

4. Utilizando [**item_mast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/item_mast.csv). Escribe un query que muestre el nombre y el precio de todos los productos con un precio igual o mayor que 25. La lista debe de contener el precio más alto primero, y luego, ordenar el nombre de manera ascendente.

```sql
SELECT pro_name, pro_price 
  FROM item_mast
  WHERE pro_price >= 250
  ORDER BY pro_price DESC, pro_name;
```

5. Utilizando [**item_mast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/item_mast.csv). Escribe un query que muestre el precio promedio de los items de cada compañía, mostrando solo el código de la compañía.

```sql
SELECT AVG(pro_price) AS ave_price, pro_com
  FROM item_mast
  GROUP BY pro_com;
```

6. Utilizando [**item_mast**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/item_mast.csv). Escribir un query que muestre los nombres y el precio de los productos más baratos.

```sql
SELECT pro_name, pro_price
  FROM item_mast
  WHERE pro_price = (
    SELECT MIN(pro_price)
      FROM item_mast);
```

7. Utilizando [**customer**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/customer.csv) y [**salesman**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/salesman.csv). Escribe un query que regrese una lista con el nombre del vendedor, del usuario, y la ciudad para el vendedor y cliente que pertenece a la misma ciudad.

```sql
SELECT name AS 'Salesman', cust_name, city
  FROM salesman
  INNER JOIN customer USING(city);
```

8. Utilizando [**sales_orders**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/sales_orders.csv) y [**customer**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/customer.csv). Escribe un query que regrese una lista con el número de orden, la cantidad comprada, el nombre del cliente, y la ciudad para aquellas órdenes en donde el total se encuentre entre 500 y 2000.

```sql
SELECT ord_no, purch_amt, cust_name, city
  FROM sales_orders
  LEFT JOIN customer USING(customer_id)
  WHERE purch_amt BETWEEN 500 AND 2000;
```

9. Utilizando [**customer**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/customer.csv) y [**salesman**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/salesman.csv). Escribe un query para conocer qué vendedor está trabajando con qué cliente.

```sql
SELECT a.cust_name AS "Customer Name", a.city, b.name AS "Salesman", b.commission
  FROM customer AS a
  INNER JOIN salesman AS b USING(salesman_id);
```

10. Utilizando [**sales_orders**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/sales_orders.csv), [**salesman**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/salesman.csv) y [**customer**](https://github.com/josemariasosa/jomtools-data/blob/master/sql/exercises/2-multi/customer.csv). Escribe un query que encuentre los detalles de la orden (numero de orden, fecha, cantidad, cliente, vendedor)

```sql
SELECT a.ord_no,a.ord_date,a.purch_amt, b.cust_name AS "Customer Name", b.grade, c.name AS "Salesman", c.commission 
  FROM sales_orders AS a 
  INNER JOIN customer AS b USING(customer_id)
  INNER JOIN salesman AS c 
  ON a.salesman_id=c.salesman_id;
```

---

## English edition

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

