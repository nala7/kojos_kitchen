# Proyectos de Simulación basada en Eventos Discretos

> Nadia González Fernández C-412

- **Problema:** 
  
**La Cocina de Kojo (Kojo’s Kitchen)**

La cocina de Kojo es uno de los puestos de comida rápida en un centro 
comercial. El centro comercial está abierto entre las 10:00 am y 
las 9:00 pm cada día. En este lugar se sirven dos tipos de productos: 
sándwiches y sushi. Para los objetivos de este proyecto se asumirá que
existen solo dos tipos de consumidores: unos consumen solo sándwiches y 
los otros consumen solo productos de la gama del sushi. En Kojo hay dos 
períodos de hora pico durante un día de trabajo; uno entre las 11:30 am 
y la 1:30 pm, y el otro entre las 5:00 pm y las 7:00 pm. El intervalo de
tiempo entre el arribo de un consumidor y el de otro no es homogéneo pero, 
por conveniencia, se asumirá que es homogéneo. El intervalo de tiempo de 
los segmentos homogéneos, distribuye de forma exponencial.

Actualmente dos empleados trabajan todo el día preparando sándwiches y sushi
para los consumidores. El tiempo de preparación depende del producto en cuestión. 
Estos distribuyen de forma uniforme, en un rango de 3 a 5 minutos para la preparación 
de sándwiches y entre 5 y 8 minutos para la preparación de sushi.

El administrador de Kojo está muy feliz con el negocio, pero ha estado recibiendo
quejas de los consumidores por la demora de sus peticiones. Él está interesado en
explorar algunas opciones de distribución del personal para reducir el número de quejas. 
Su interés está centrado en comparar la situación actual con una opción alternativa donde 
se emplea un tercer empleado durante los períodos más ocupados. La medida del desempeño de 
estas opciones estará dada por el porciento de consumidores que espera más de 5 minutos 
por un servicio durante el curso de un día de trabajo.

Se desea obtener el porciento de consumidores que esperan más de 5 minutos cuando solo dos
empleados están trabajando y este mismo dato agregando un empleado en las horas pico.


- **Modelo de Simulación de Eventos Discretos:** sistema de atención con dos servidores en paralelo
- **Solución:** La solución dada simula los eventos de arribo de clientes en minutos. Es decir, como el centro comercial esá
abierto de 10:00 am a 9:00 pm, en la simulación el lugar está abierto desde el minuto 0 hasta el 660.
El intervalo de tiempo entre el arribo de un consumidor y el de otro distribuye
de forma exponencial. Se asume que el intervalo de minutos es \[0, 10\]. Por lo tanto se utilizó 
lambda = 0.2 para simular una baja frecuencia de clientes y lambda = 0.5 para frecuencias más altas   
  
```python
def exponential_distribution(lamba, a, b) -> float:
    u = uniform_distribution(a, b)
    x = - (1 / lamba) * np.log(u)
    if x < 0:
        x = x * (-1)

    return x
```
Para simular los tiempos de preparación de los productos se utilizó la distribución uniforme:
```python
def uniform_distribution(a: int, b: int) -> float:
    u = random.random()
    return a + (b - a) * u
```

Se utilizaron tres clases principales:

**Server**: contiene la información de un servidor

**Client**: contiene la información de un cliente

**Status**: mantiene la lista de servidores que están trabajando, la lista de clientes esperando en 
cola a ser atendidos y la lista de clientes que han salido de la tienda
      
El algoritmo utilizado se encuentra en `main.py`. Este sigue las pautas de un sistema de atención con 
dos servidores en paralelo que se encuentra en el libro "Temas de Simulación". Se utilizó el siguente
pseudo código para la implementación del algoritmo:

```
Inicialización
    t = Na = C1 = C2 = 0
    SS = (0)
    Genera T0 y tA = T0, t1 = t2 = infinito

Caso 1 SS = (n, i1, i2, ... , in) ^ tA = min(tA, t1, t2)
        t = tA
        NA = NA + 1
        Genera Tt y tA = t + Tt
        A(NA) = t
        Si SS = (0) entonces SS = (1, NA, 0), genera Y1 y t1 = t + Y1
        Si SS = (1, j, 0) entonces SS = (2, j, NA), genera Y2 y t2 = t + Y2
        Si SS = (1, 0, j) entonces SS = (2, NA, j), genera Y1 y t1 = t + Y1
        Si n > 1 entonces SS = (n + 1, i1, 12, ... , in, NA)
        
Caso 2 SS = (n, i1, i2, ... , in) ^ t1 < tA ^ t1 <= t2
        t = t1
        C1 = C1 + 1
        D(i1) = t
        Si n = 1 entonces SS = (0) y t1 = 1
        Si n = 2 entonces SS = (1, 0, i2) y t1 = 1
        Si n > 2 entonces SS = (n - 1, i3, i2, ... , in), genera Y1 y t1 = t + Y1
        
Caso 3 SS = (n, i1, i2, ... , in) ^ t2 < tA ^ t2 <= t1
        t = t2
        C2 = C2 + 1
        D(i2) = t
        Si n = 1 entonces SS = (0) y t2 = 1
        Si n = 2 entonces SS = (1, 0, i2) y t2 = 1
        Si n > 2 entonces SS = (n - 1, i2, i3, ... , in), genera Y2 y t2 = t + Y2
```

En un inicio se generan todos los clientes que llegarán al centro y se almacenan en una lista. 
Se crea una lista con los dos servidores que se utilizaran en toda la simulación y se crea una instancia de la clase `Status`, el cual se utilizará
para mantener actualizada la información del sistema. Este último será el encargado de mantener la lista de los clientes que se 
encuentran en la tienda esperando ser atendidos y también la lista de los clientes que ya fueron atendidos.  

Para la simulación de un tercer chef, se añade, a la lista de servidores, un tercer servidor durante los horarios picos. 


- **Consideraciones obtenidas a partir de la ejecución de las simulaciones del problema:**

Luego de analizar las simulaciones se ha llegado a la conclusión de que el desempeño mejora entre un 30 y un 40 por ciento cuando se agrega un chef
en el horario pico. También se pudo observar que a mayor frecuencia de clientes (mayor lambda en la función de distibución exponencial) los porcentajes
de mejora aumentan.


- **Repositorio de Github**: https://github.com/nala7/kojos_kitchen.git