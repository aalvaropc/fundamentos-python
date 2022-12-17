# FUNDAMENTOS DE PYTHON <img src="https://github.com/aalvaropc/FundamentosPython/blob/main/img/dsc-sticker-files-brackets.png " width="40">

<p><img src="https://github.com/aalvaropc/FundamentosPython/blob/main/img/learn-python.png" width="990" height="270"></p>

<details><summary><h2>SESION1</h2></summary>

<details><summary><h3>TIPOS DE DATOS</h3></summary>

- NUMERICOS

| Nombre | Descripción| Ejemplo |
|------|---|---|
| int | números enteros| 23, 1_000_000|
| float | números reales| 4.5, 1. |
| complex | números complejos| 3 + 3j, 1 + 4j|

- SECUENCIALES

| Nombre | Descripción| Ejemplo |
|------|---|---|
| list | secuencia mutable de valores| [23, .1, 1+4j, [1,2,3]]|
| tuple | secuencia inmutable de valores| ("hola", 'como estas') |
| range | secuencia inmutable de números y se usa comúnmente para <br>repetir un número específico de veces en bucles for| range(0,3)|

- TIPO DE SECUENCIA DE TEXTO

| Nombre | Descripción| Ejemplo |
|------|---|---|
| str | Las cadenas implementan todas las operaciones de secuencia <br>comunes, junto a métodos adicionales| "Hello world"|

- TIPO BOOLEANO

| Nombre | Descripción| Ejemplo |
|------|---|---|
| bool | Se utilizan para representar valores de verdad| True, False|

- TIPO DE MAPEO

| Nombre | Descripción| Ejemplo |
|------|---|---|
| dict | asigna valores hash a objetos arbitrarios| {2018 : "juan", 2022: "juana"}|

- TIPOS DE CONJUNTOS

| Nombre | Descripción| Ejemplo |
|------|---|---|
| set | almacena elementos unicos de manera desordenada y son mutables| {5, 8, 1}|
| frozenset | similar a los set, con la excepción de que son inmutables| frozenset({1, 2, 3}) |

- TIPO NONE

| Nombre | Descripción| Ejemplo |
|------|---|---|
| NoneType | Es devuelto por funciones que no devuelven explícitamente un valor| None|

</details>
<details><summary><h3>VARIABLES</h3></summary>

Son contenedores que almacenan valores.

<h3>REGLAS PARA CREAR VARIABLES</h4>

- Debe comenzar con una letra o el carácter de subrayado.

- No puede comenzar con un número.

- Solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _).

- Distinguen entre mayúsculas y minúsculas (nombre, Nombre y NOMBRE son tres variables diferentes).

- Las palabras reservadas (palabras clave) no se pueden usar para nombrar la variable.

<h3>DECLARANDO VARIABLES</h3>

```python
saludo = "hola"
edad = 30
```

<h3>CASTING</h3>

```python
x = str(3)    # x será '3'
y = int(3)    # y será 3
z = float(3)  # z será 3.0
```
</details>

<details><summary><h3>ESTRUCTURA CONDICIONAL IF, ELIF Y ELSE</h3></summary>
  
La estructura  if/elif/else es una forma común de controlar el flujo de un programa, lo que te permite ejecutar bloques de código específicos según el valor de algunos datos
  
<h3>SENTENCIA IF</h3>
  
Si la condición que sigue a la palabra clave if  se evalúa como verdadera, el bloque de código se ejecutará. Ten en cuenta que los paréntesis no se utilizan antes y después de la verificación de condición como en otros idiomas.
 
```python
if True:
  print("Se mustra este mensaje")
```
  
<h3>SENTENCIA ELSE</h3>
  
Opcionalmente, puedes agregar una respuesta else que se ejecutará si la condición es false.

```python
if not True:
  print('¡La sentencia If se ejecutará!')
else:
  print('¡La sentencia Else se ejecutará!')
```
  
<h3>SENTENCIA ELIF</h3>

Se pueden verificar varias condiciones al incluir una o más verificaciones elif después de su declaración if inicial. Ten en cuenta que solo se ejecutará una condición:

```python
z = 7

if z > 8:
  print("¡No voy a imprimir!") #esta sentencia no se ejecuta
elif z > 5:
  print("¡Yo lo haré!") #esta sentencia se ejecuta
elif z > 6:
  print("¡Tampoco voy a imprimir!") #esta sentencia no se ejecuta
else:
  print("¡Yo tampoco!") #esta sentencia no se ejecuta
``` 
Solo se ejecutará la primera condición que se evalúe como true. Aunque z > 6 es true, el bloque if/elif/else termina después de la primera condición verdadera. Esto significa que un else solo se ejecutará si ninguna de las condiciones es true.
  
<h3>SENTENCIAS IF ANIDADAS</h3>
  
También podemos crear if anidados para la toma de decisiones.
Tomemos un ejemplo de cómo encontrar un número que sea par y también mayor que 10

```python
x = 34
if x %  2 == 0:  # así es como creas un comentario y ahora comprueba número par.
  if x > 10:
    print("Este número es par y es mayor que 10")
  else:
    print("Este número es par, pero no mayor 10")
else:
  print("El número no es par. Así que punto de verificación más.")
``` 
<h3>DECLARACIÓN IF-ELSE EN LINEA</h3>

Podemos usar declaraciones if-else en funciones de Python en línea.
El siguiente ejemplo debe verificar si el número es mayor o igual que 50, si es así, retorna True:

```python
x = 89
es_mayor = True if x >= 50 else False

print(es_mayor) #True
``` 
</details>
</details>

