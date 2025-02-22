##Dates
# ? Se importa la libreria datetime
import datetime

now = datetime.datetime

# ? Se importa datetime para datetime
from datetime import datetime

now = datetime.now()  # ? se declara la variable para la funcion now()
print(now.year)  ## Se muestra el año
print(now.month)  ## Se muesta el mes del año
print(now.day)  ## Se muestra el dia del año
print(now.hour)  ## Se muestra la hora del año
print(now.minute)  ## Se muestra el minuto del año
print(now.second)  ## Se muestra el secundo del año

timestamp = now.timestamp()  # ? Se declara la variable timestamp
print(timestamp)


# ? Se crea una funcion print_date
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(
    now
)  # ? Se utiliza la funcion de print_date para saber cual es el dato de noew dentro de sus propiedades\

# ? Se declara una nueva variable year_2025
year_2025 = datetime(2025, 1, 1)

print_date(
    year_2025
)  ## Se necesitan los valores del año, mes y dia para poder utilizar la funcion
## Año 2025
## Mes 1
## Dia 1
## Hora, si no se establece el valor es 0
## Minuto, si no se establece el valor es 0
## Segundo, si no se establece el valor es 0

# ? Importacion del date
from datetime import time

current_time = timne()

print(current_time.hour)  ## No tiene datos
print(current_time.min)  ## No tiene datos
print(current_time.second)  ## No tiene datos

current_time = time(10, 51, 20)

print(current_time.hour)  ## El valor es 10
print(current_time.min)  ## El valor es 51
print(current_time.second)  ## El valor es 20

from date import datetime  # #Se importa de la libreria date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 1, 1)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.year)
print(current_date.month)
print(current_date.day)

diff_datetime = year_2025 - now
print(diff_datetime)

diff_datetime = year_2025.date() - current_date
print(diff_datetime)

from datetime import (
    timedelta,  # # Se utiliza para saber el rango de tiempo que va durar un evento
)

init_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)
