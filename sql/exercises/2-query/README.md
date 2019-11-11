# Basic SQL queries

## Objectives

- Run the most common-used queries in a db

## Requirements

1. Docker
2. Terminal
3. MySQL Workbench

## MySQL Locations

* Mac             */usr/local/mysql/bin*
* Windows         */Program Files/MySQL/MySQL _version_/bin*
* Xampp           */xampp/mysql/bin*

## Add mysql to your PATH

```bash
# Current Session
export PATH=${PATH}:/usr/local/mysql/bin
# Permanantly
echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.bash_profile
```

On Windows - https://www.qualitestgroup.com/resources/knowledge-center/how-to-guide/add-mysql-path-windows/

## Development

Using our previous setup, loading data from the **mibici.csv** file. Let's run some queries to the `test_db` database.

1. Filter all the trips from users with an age above 30.

```sql
SELECT * FROM trips WHERE Edad_Usuario > 30;
```

2. Filter all the trips started after 5 pm done by a woman.

```sql
SELECT * FROM trips WHERE Hora_Retiro > '17:00:00' AND Genero_Usuario = 'F';
```

3. Filter all the trips started before 8 am or after 5 pm.

```sql
SELECT Ciclo_Estacion_Retiro FROM trips WHERE Hora_Retiro > '17:00:00' OR Hora_Retiro < '8:00:00';
```
