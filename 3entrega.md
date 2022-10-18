# Tercer Entrega

## Objetivos
Determinar en que lavado insertar cada prenda minimizando el tiempo total de lavados, teniendo en cuenta las incopatibilidades entre prendas.

## Hipotesis y supuestos
- No hay fallas durante el lavado
- No se rompen las maquinas
- No hay costos de lavado
- No se considera el tiempo entre lavados
- Las prendas se lavan por unica vez, no se repiten.

## Variables

- Defino Yij donde:

Yij = 1 si la prenda i va en el lavado j

Yij = 0 si no

Donde i,j ∈ [0,n] siendo n la cantidad total de prendas

- Y el tiempo de cada prenda es definido por: 

Yi


- Ahora defino la variable Wj bivalente donde:

{1 si se realiza el lavado j para todo j = 1...n

{0 si no

- Finalmente tenemos:

Tj: tiempo del lavado j

Tij: tiempo de lavado de la prenda i en el lavado j

## Funcional

Como busco minimizar el tiempo total de todos los lavados, el funcional seria el siguiente:
$$Min Z = \displaystyle\sum_{j=1}^{n} T_{j}$$

## Restricciones
- Hay que poner una restriccion para evitar que prendas incompatibles vayan juntas. Entonces la prenda (a) no puede ir junto con la prenda (b)

$$Taj + Tbj <= 1;  ∀ j = 1,....,n$$

- Como pusimos en la hipotesis, las prendas se lavan por unica vez entonces:

$$\displaystyle\sum_{j=1}^{n} T_{ij} = 1; ∀i = 1,....,n$$

- Es importante que cada lavado tarde lo mismo  que la prenda que demore más tiempo, por lo tanto:

    $$Xij = Yi*Yij$$

    $$Xij <= Xj <= Xij + M(1 - max(Tj))$$