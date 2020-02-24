# R Introduction

![](images/datatime.png?raw=true)


https://www.forbes.com/sites/gilpress/2016/03/23/data-preparation-most-time-consuming-least-enjoyable-data-science-task-survey-says/#309bf1306f63

https://rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf

## Messing around

In order to create a data.frame from scratch we can call the `data.frame()` function and give a name to each column.

```R
df <- data.frame(
  product = c("TV", "DVD", "Speakers", "Cables"), 
  quantity = c(1, 1, 2, 10),
  price = c(500, 99, 120, 6))
```

Answer the following questions:

- How can we see a list of the products?
- How can we multiply `18.99` to the price? (const * n)
- How can we save the latter results in a new column?
- How can we multiply the price and the quantity to get the total? (n * n)
- How can we convert the product to the data.frame index? And vice versa?
- How can you rename the `total` column as `TOTAL`?
- What's the difference between a vectorized function and an atomic function?


```R
df$pesos = 18.99 * df$price
df$total = df$quantity * df$price

rownames(df) <- df$products
df$product <- NULL

df$product = rownames(df)
rownames(df) <- NULL

names(df)[names(df) == 'total'] <- 'TOTAL'
```

The library `dplyr` has a new kind of data.frame with extended functionalities that can be generated from a regular data.frame using the function `tbl_df()`.

```R
library(ggplot2)

diam = tbl_df(diamonds)
```

This is a very good way to manage large datasets. But there are times that you need to see the complete data, so you can use `View()`. Almost as it was an Excel Spreadsheet.

The **Pipe Operator** `%>%` help us work step by step. We can select the columns we need from a table, or we can even get the mean of a column.

```R
library(dplyr)

diam %>% 
  select(cut, price, x)

diam$price %>% mean()
# [1] 3932.8
```

Import the 3 datasets: storms, cases, pollution from the `data/` folder. These are three simple datasets, but the data that they contain are stored in different ways.

```R
storms <- read.csv("~/storms.csv")
cases <- read.csv("~/cases.csv")
pollution <- read.csv("~/pollution.csv")
```

If we open the tables we will see the following information.

![](images/datasets.png?raw=true)

Let's analyze how the data is saved in each table.

![](images/datastr.png?raw=true)

As you can see, the data have different structures. But let **discuss**:

```
Which of the 3 dataset have a better structure to do an analysis? And why?
```

Definitely, the `storms` dataset have the best structure because it checked the 3 requirements for a **tidy data**, popularized by Hadley Wickham, Chief Scientist at RStudio:

1. Each **variable** is saved in its own **column**. So you never ever mix different data types within the same column.
2. Each **observation** is saved in its own **row**.
3. Each "type" of observation stored in a **single table**.

## Gather and spread

So following these 3 simple rules, imagine how the data in the `cases` dataset would look if it were tidy.

The solution should look like the following table.

![](images/fixcases.png?raw=true)

To get the correct structure in R, we are going to use the `gather()` function from the `tidyr` library.

```R
library(tidyr)

cases %>% 
  gather("year", "n", 2:4)
```

Now imagine how the data in the `pollution` dataset would look if it were tidy.

The solution should look like the following table.

![](images/fixpollution.png?raw=true)

To get the correct structure in R, we are going to use the `spread()` function from the `tidyr` library.

```R
pollution %>% 
  spread("size", "amount")
```

You can think of **spread** as taking data that is in a key-value column format and put it and field to cell format. And you can think of **gather** as the inverse operation. Going back and forth with spread and gather you can change values into column names and column names into values.

![](images/spread_gather.png?raw=true)

## Unite and separate

If you see the storm table, you could notice that the date has: year, month and a day. If we want to separate each variable in a different column we can use the `separate()` function from the `tidyr` library.

![](images/separate_unite.png?raw=true)

```R
storms2 <- storms %>% 
  separate("date", c("year", "month", "day"), sep="-")
```

In order to do the opposite and concatenate multiple columns into a single one we use the `unite()` function.

```R
storms3 <- storms2 %>% 
  unite("date", "year", "month", "day", sep="-")
```

## Preparing our data

With the function `select()` from the `dplyr` library we can choose, remove or rearrange the columns from our dataset.

**Choose** some columns:

```R
library(datasets)

mtcars %>%
  select(mpg, cyl, hp) %>% 
  head

mtcars %>%
  select(starts_with('d')) %>% 
  head
```

**Remove** some columns:

```R
mtcars %>%
  select(-mpg, -cyl, -hp) %>% 
  head
```

**Rearrange** the columns order:

```R
mtcars %>%
  select(gear, carb, everything()) %>% 
  head
```

A list of useful **select** functions.

![](images/select_fun.png?raw=true)

What happens if we convert the `mtcars` dataset into a table of the `dplyr` library?

```R
cars <- tbl_df(mtcars)
print(cars)
```


We saw how to select columns from a dataset, but now let's figure how to **filter** specific rows in our dataset.













shortcuts:

option + '-' = <-

control + shift + 'm' = %>%

## Packages

Some common R packages.

- dplyr
- tidyr
- stringr
- lubridate
- httr
- ggvis
- ggplot2
- shiny
- rio
- rmarkdown

pacman is a package manager.

```R
# LOAD PACKAGES ############################################

# I recommend "pacman" for managing add-on packages. It will
# install packages, if needed, and then load the packages.
install.packages("pacman")

# Then load the package by using either of the following:
require(pacman)  # Gives a confirmation message.
library(pacman)  # No message.

# Or, by using "pacman::p_load" you can use the p_load
# function from pacman without actually loading pacman.
# These are packages I load every time.
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, 
  ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, 
  stringr, tidyr)

library(datasets)  # Load/unload base packages manually

# CLEAN UP #################################################

# Clear packages
p_unload(dplyr, tidyr, stringr) # Clear specific packages
p_unload(all)  # Easier: clears all add-ons
detach("package:datasets", unload = TRUE)  # For base

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)

```


## Plot

```r
# Plot with options
plot(iris$Petal.Length, iris$Petal.Width,
  col = "#cc0000",  # Hex code for datalab.cc red
  pch = 19,         # Use solid circles for points
  main = "Iris: Petal Length vs. Petal Width",
  xlab = "Petal Length",
  ylab = "Petal Width")
```






Para ver todos los objetos que contiene el paquete usaremos la función ls (list files):

ls("package:ggplot2")

De igual forma, para conocer todas las funciones disponibles en el package, usaremos la función lsf.str:

lsf.str("package:ggplot2")


Esta opcion solo la tengo que realizar una vez y ya queda almacenado en la memoria de nuestro RStudio

install.packages("ggplot2")
Cargando el paquete para poder usarlo. Esta operacion tendra que repetirla cada vez que reinicie el programa y quiera usar el paquete

library("ggplot2")
Solicito ayuda / informacion de la descripcion y uso de este paquete

?ggplot2



Revisar todas las variables creadas.
ls()





class() y typeof()

Conocer la clase y el tipo de dato de una variable.


## Establecer y modificar directorio de trabajo

getwd()

revisar los archivos/files que existen en nuestro directorio.
dir()

setwd("/Users/josemaria/Maria/Repositories/jomtools/R")


# Create a df
df <- data.frame(
  Nombre = c("Gato", "Perro", "Vaca", "Cerdo"), 
  Cuantos = c(5, 10, 15, 20),
  EsMascota = c(TRUE, TRUE, FALSE, FALSE))

# dplyr



> x1 <- c('A', 'B', 'C')
> x2 <- c(1,2,3)
> a <- data.frame(x1,x2)
> a
  x1 x2
1  A  1
2  B  2
3  C  3



> x1 <- c('A', 'B', 'D')
> x3 <- c(T,F,T)
> b <- data.frame(x1,x3)
> b
  x1    x3
1  A  TRUE
2  B FALSE
3  D  TRUE


library(dplyr)


> 'A' %in% a$x1
[1] TRUE


> left_join(a, b, by='x1')
  x1 x2    x3
1  A  1  TRUE
2  B  2 FALSE
3  C  3    NA

iris %>% # Datos que usare
  group_by(Species) %>% # Variable de agrupacion
  summarise(Media_Sepal_Length = mean(Sepal.Length), # Media de sepal length
            Media_Sepal_Width = mean(Sepal.Width)) %>% # Media de sepal width
  arrange(Species)

 Details
summarise() and summarize() are synonyms.

Useful functions
Center: mean(), median()

Spread: sd(), IQR(), mad()

Range: min(), max(), quantile()

Position: first(), last(), nth(),

Count: n(), n_distinct()

Logical: any(), all()


titanic_train %>% group_by(Survived) %>% summarise(Total = n())

# Usually, you'll want to group first
mtcars %>%
  group_by(cyl) %>%
  summarise(mean = mean(disp), n = n())



mtcars %>% select(mpg, cyl, disp)

mtcars %>% select(mpg, cyl, disp, everything())

everything() help us get "everything else". so we select this columns first, then everything else.

ecobici <- ecobici %>% 
  count(Colonia) %>% 
  arrange(Colonia)

> mtcars %>% summarize_all(max)
   mpg cyl disp  hp drat    wt qsec vs am gear carb
1 33.9   8  472 335 4.93 5.424 22.9  1  1    5    8

> mtcars %>% summarize_if(is.numeric, max)
   mpg cyl disp  hp drat    wt qsec am gear carb
1 33.9   8  472 335 4.93 5.424 22.9  1    5    8

# filter by the variables!
> mtcars %>% summarize_at(vars(starts_with('d')), max)
  disp drat
1  472 4.93


```R
## Introduccion al package dplyr 
install.packages("dplyr")
library(dplyr)

# Dplyr nos ayudara a hacer consultas, agregaciones y filtros de datos de manera rapida
# Su uso es similar al de SQL (dispone de funciones como select, left join, inner join y group by)
# Ademas, dispone de algunas propias (filter, summarise, arrange y mutate)

# Importamos el fichero llamado data para poder operar con el a continuacion 
datos <- read.csv("data.csv", header=TRUE)
head(data) # Para visualizar los primeros registros 

# Muestra aleatoria de la base. El segundo componente indica el numero de filas que queremos
# Atencion! Esta muestra aleatoria cambiara cada vez que ejecutemos el codigo, por lo que los resultados
# del analisis variaran 
sample_n(datos,8)

# Tambien podemos importar informacion de manera aleatoria pero indicando el porcentaje que deseamos
sample_frac(datos,0.1) # 10%

# Si dudamos de la existencia de duplicados, podemos usar la funcion distinct
distinct(datos)

# Para seleccionar informacion especifica de la tabla 
select(datos, Indice, Estado, A2008)

# Si nos es mas facil indicar que queremos llevar todas las variables excepto alguna/s, lo indicaremos 
# con el simbolo "-" delante de la variable
select(datos, -Indice, -Estado) # en este caso, solo el indice y el Estado seran omitidos 

# Tambien podemos filtrar segun el primer caracter 
select(datos, starts_with("A")) # Importara toda la informacion que contienen los anos 
select(mydata, -starts_with("A")) # Esta funcion traera la informacion complementaria al comando anterior

# Una de las maneras para cambiar el nombre de las columnas es la funcion rename
rename(datos, Indice1 = Indice)
datos <- rename(datos, Indice1 = Indice) # Asi logramos que los cambios se guarden 

# La funcion filter facilita la filtracion de informacion 
filter(datos, Indice1 == "A") # Informacion de aquellos Estados que su indice es "A"

# Multiples criterios de seleccion
filter(datos, Indice1 %in% c("A", "B")) 

# Filtrar por varias variables separando los comandos por "&" 
filter(datos, Indice1 %in% c("A", "B") & A2008 >= 1300000 )

# Para indicar condiciones disyuntivas (equivalente a "or" en SQL, seria "|" ) 
# Solo tiene que cumplir una de ambas condiciones para ser fitrado 
filter(datos, Indice1 %in% c("A", "B") | A2008 >= 1300000)

# Al igual que SQL, el simbolo "!" indica que no esta/cumpla una condicion
filter(datos, !Indice1 %in% c("A", "B"))

# La funcion grepl ayuda a extraer informacion de un campo en particular 
filter(datos, grepl("kan", Estado)) # Informacion de aquellos estados que contengan "kan" 

# Summarise es una funcion muy util para hacer operaciones rapidas sobre variables
summarise(datos, A2012_mean = mean(A2012)) # Media de todos los estados en 2012 

# Summarise_at nos permite escribir varias condiciones de agrupacion de las operaciones 
summarise_at(datos, vars(A2012, A2013), funs(n(), mean, median))

# Funcion arrange para ordenar informacion segun varias variables
arrange(datos, Indice1, A2012) # Por defecto, esta ordenacion es ascendente 

# Otra manera de separar varias funciones es usar "%>%"
datos %>%
  group_by(Indice1)%>%
  summarise(Media2012 = mean(A2012, na.rm=TRUE), #NA remove para evitar tener registros vacios que sesguen la informacion 
            Media2014 = mean(A2014, na.rm=TRUE)) %>%
  arrange(desc(Media2012))
```


- Make a data frame from vectors in R

> employee <- c('John Doe','Peter Gynn','Jolie Hope')
> salary <- c(21000, 23400, 26800)
> startdate <- as.Date(c('2010-11-1','2008-3-25','2007-3-14'))

> employ.data <- data.frame(employee, salary, startdate)

> str(employ.data)
'data.frame': 3 obs. of 3 variables:
 $ employee : Factor w/ 3 levels "John Doe","Jolie Hope",..: 1 3 2
 $ salary  : num 21000 23400 26800
 $ startdate: Date, format: "2010-11-01" "2008-03-25" ...

- Keep characters as characters in R

> employ.data <- data.frame(employee, salary, startdate, stringsAsFactors=FALSE)

> str(employ.data)
'data.frame': 3 obs. of 3 variables:
 $ employee : chr "John Doe" "Peter Gynn" "Jolie Hope"
 $ salary  : num 21000 23400 26800
 $ startdate: Date, format: "2010-11-01" "2008-03-25" ...


summary(mtcars)


# Coerse

mtcars$vs = as.logical(mtcars$vs)
mtcars$am = as.logical(mtcars$am)
class(mtcars$vs)
class(mtcars$am)

# transform columns

mtcars.new <- transform(mtcars, wt = wt * 1000 / 2.204623)




# if else

if (mtcars[1, 'mpg'] > 20) {
  status = "saver"
} else {
  status = "not saver"
}


if (mtcars[1, 'mpg'] > 20) {
  status = "saver"
} else if (mtcars[1, 'mpg'] < 20) {
  status = "not saver"
} else {
  status = "average"
}

ifelse(1 < 2, T, F)

x = sample(-1:13, 10)
y = sample(-1:13, 10)

all(x > 0)

any(x == y)

x > 0 & y > 0

x > 0 | y > 0

# The which

find the indexes that satisfy a condition.

big = mtcars$drat > 4

Returns the index of the ones that are true!
which(big)

Work equal:
> mtcars[big,]
> mtcars[which(big),]


x <- 0
while(x < 5){
  x <- x+1;
  if (x == 3)
    next; 
  print(x);
  }

 ## REPEAT IF BREAK
suma <- 0
repeat{
  suma = suma+1
  print(suma)
  if (suma == 8){
    print("El loop termino");
    break
  }
}






### ggplot2

library(ggplot2)

ggplot(data=iris,
       aes(Sepal.Length, Petal.Length))
Este gráfico contiene los ejes que especificamos pero no contiene los datos. Para dibujarlos, debemos decirle a ggplot cómo hacerlo (por ejemplo, puntos).

ggplot(iris, aes(Sepal.Length, Petal.Length)) +
  geom_point()


ggplot(iris, aes(Sepal.Length, Petal.Length, color = Species)) +
  geom_point()




The apply() Family


The R base manual tells you that it’s called as follows: apply(X, MARGIN, FUN, ...)

where:

X is an array or a matrix if the dimension of the array is 2;
MARGIN is a variable defining how the function is applied: when MARGIN=1, it applies over rows, whereas with MARGIN=2, it works over columns. Note that when you use the construct MARGIN=c(1,2), it applies to both rows and columns; and
FUN, which is the function that you want to apply to the data. It can be any R function, including a User Defined Function (UDF).


# Construct a 5x6 matrix
X <- matrix(rnorm(30), nrow=5, ncol=6)

# Sum the values of each column with `apply()`
apply(X, 2, sum) # Sum col by col
apply(X, 1, sum) # Sum row by row


sapply is like a Series.apply() or Series.map()

apply(MARGIN=1) is like a Pd.apply(axis=1)

jose = function(s) {
  if (s == 'male') {
    return('onvre')
  } else if (s == 'female') {
    return('mujel')
  } else {
    return('NOSE')
  }
}
head(df)
df = titanic_test
sapply(df$Sex, jose)

loco = function(row) {
  return (c(row['Sex'], row['Pclass']))
}

apply(df, 1, loco)
