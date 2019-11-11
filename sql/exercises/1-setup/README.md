# Config a MySQL client

## Objectives

- Use Docker to run a basic MySQL service
- Use MySQL Workbench to open our service
- Create a table loading a CSV file

## Requirements

1. Docker
2. Terminal
3. MySQL Workbench

## Docker

Official Mysql image:

- https://hub.docker.com/_/mysql

## Development

1. Make a directory named `1-setup/` and move inside.

```bash
mkdir 1-setup
cd 1-setup
```

2. Create a file with the following commands, and save it as `docker-compose.yml`.

```bash
version: '3'
services:
  my_db:
    image: mysql:8.0.17
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: test_db
    ports:
      - "3308:3306"
```

Important things to know about this file:

- `my_db` is the name of our service.
- `test_db` is the name of the default schema.

3. Using the terminal run the following command to run the container.

```bash
docker-compose up
```

The status of the container will be prompted in the terminal. As long as the container is running, the terminal will display details about it and we are no longer able to use this terminal, so we must open a new terminal window to move on. If we want to run the container in the back we can use the detach flag.

```bash
docker-compose up -d
```

4. Review or containers status

From another terminal, run the following command to get the containers status.

```bash
docker-compose ps
```

In the response, we can see how the container is running in the 3308 port.

```bash
     Name                   Command             State                 Ports
-----------------------------------------------------------------------------------------
1-setup_my_db_1   docker-entrypoint.sh mysqld   Up      0.0.0.0:3308->3306/tcp, 33060/tcp
```

5. Connect to the db using the MySQL Workbench client.

Open MySQL Workbench and generate a new connection using the `docker-compose.yml` parameters.

- host: `localhost`
- schema: `test_db`
- password: `password`
- default user: `root`

6. Create a new table.

In order to create a new table in our container run the following code from the client.

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

You can also, in case you don't want to use the MySQL client, open the `mysql` terminal from the container running:

```bash
docker-compose exec my_db mysql -uroot -ppassword test_db
```

If nothing goes wrong, you will see the prompt like this. Using the `SHOW` command from sql, we can check our database.

```text
mysql> SHOW databases;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test_db            |
+--------------------+
5 rows in set (0.01 sec)
```

Create the new table using the terminal or the `mysql` client. In order to see that our table was successfully created let's show all the tables and then do the simplest query.

```text
mysql> SHOW tables;

+-------------------+
| Tables_in_test_db |
+-------------------+
| trips             |
+-------------------+
1 row in set (0.00 sec)
```

Run the simplest query, where you select all the columns from the table.

```text
mysql> SELECT * FROM trips;
Empty set (0.00 sec)
```

All this code, can also be ran from the MySQL Workbench client. Try it!

And let's populate the table with the data from the CSV file: `mibici.csv`. Remember that the data is located in a different repository called **jomtools-data**.

7. Load the data using the `mysql` client.

After running the `SELECT` query in the client, a small window will be opened. That window have an icon that says Export/Import. Click it and follow the instructions to insert the data to an existing table, the one we created in the step 6.

Let's run again the `SELECT` query to see if our data was fully loaded.

```sql
mysql> SELECT * FROM trips;
```

**Final notes.**

If you stop the container, and then run it down.

```bash
docker-compose down
```

All the data you loaded will be lost.

In order to save the data inside the container, a **volume** in the `docker-compose.yml` file must be defined. To save data into the container we must add the following line to the yml file.

```bash
    volumes:
      - "./data:/var/lib/mysql:rw"
```
