import graphviz

# Lista de diagramas a generar
diagramas = {}

# Ejercicio 1: Determinar el mayor de dos valores distintos
dot1 = graphviz.Digraph(format='png')
dot1.node('Inicio', 'Inicio', shape='oval')
dot1.node('LeerA', 'Leer A', shape='parallelogram')
dot1.node('LeerB', 'Leer B', shape='parallelogram')
dot1.node('Decision', 'A > B?', shape='diamond')
dot1.node('EscribirA', 'Escribir "El mayor es: A"', shape='parallelogram')
dot1.node('EscribirB', 'Escribir "El mayor es: B"', shape='parallelogram')
dot1.node('Fin', 'Fin', shape='oval')

dot1.edge('Inicio', 'LeerA')
dot1.edge('LeerA', 'LeerB')
dot1.edge('LeerB', 'Decision')
dot1.edge('Decision', 'EscribirA', label='Sí')
dot1.edge('Decision', 'EscribirB', label='No')
dot1.edge('EscribirA', 'Fin')
dot1.edge('EscribirB', 'Fin')

diagramas["MayorDeDosNumeros"] = dot1

# Ejercicio 2: Verificar si un número es divisible por 3
dot2 = graphviz.Digraph(format='png')
dot2.node('Inicio', 'Inicio', shape='oval')
dot2.node('LeerN', 'Leer N', shape='parallelogram')
dot2.node('Decision', 'N MOD 3 == 0?', shape='diamond')
dot2.node('EscribirSi', 'Escribir "Es divisible por 3"', shape='parallelogram')
dot2.node('EscribirNo', 'Escribir "No es divisible por 3"', shape='parallelogram')
dot2.node('Fin', 'Fin', shape='oval')

dot2.edge('Inicio', 'LeerN')
dot2.edge('LeerN', 'Decision')
dot2.edge('Decision', 'EscribirSi', label='Sí')
dot2.edge('Decision', 'EscribirNo', label='No')
dot2.edge('EscribirSi', 'Fin')
dot2.edge('EscribirNo', 'Fin')

diagramas["DivisiblePorTres"] = dot2

# Ejercicio 3: Calcular potencias de un número desde a¹ hasta a^k
dot3 = graphviz.Digraph(format='png')
dot3.node('Inicio', 'Inicio', shape='oval')
dot3.node('LeerA', 'Leer a', shape='parallelogram')
dot3.node('LeerK', 'Leer k', shape='parallelogram')
dot3.node('InicializarI', 'i = 1', shape='box')
dot3.node('Decision', 'i ≤ k?', shape='diamond')
dot3.node('Calcular', 'Calcular a^i', shape='box')
dot3.node('Escribir', 'Escribir "a^i = resultado"', shape='parallelogram')
dot3.node('IncrementarI', 'i = i + 1', shape='box')
dot3.node('Fin', 'Fin', shape='oval')

dot3.edge('Inicio', 'LeerA')
dot3.edge('LeerA', 'LeerK')
dot3.edge('LeerK', 'InicializarI')
dot3.edge('InicializarI', 'Decision')
dot3.edge('Decision', 'Calcular', label='Sí')
dot3.edge('Calcular', 'Escribir')
dot3.edge('Escribir', 'IncrementarI')
dot3.edge('IncrementarI', 'Decision')
dot3.edge('Decision', 'Fin', label='No')

diagramas["PotenciasDeNumero"] = dot3

# Ejercicio 4: Cálculo de precios de artículos con y sin IVA
dot4 = graphviz.Digraph(format='png')
dot4.node('Inicio', 'Inicio', shape='oval')
dot4.node('Menu', 'Mostrar menú', shape='parallelogram')
dot4.node('LeerOpcion', 'Leer opción', shape='parallelogram')
dot4.node('Decision', 'Opción == 1?', shape='diamond')
dot4.node('LeerPrecios', 'Leer precios', shape='parallelogram')
dot4.node('CalcularTotal', 'totalSinIVA = suma de precios', shape='box')
dot4.node('CalcularIVA', 'iva = totalSinIVA * 0.16', shape='box')
dot4.node('CalcularTotalIVA', 'totalConIVA = totalSinIVA + iva', shape='box')
dot4.node('EscribirResultados', 'Escribir totales', shape='parallelogram')
dot4.node('Repetir', 'Regresar al menú', shape='parallelogram')
dot4.node('Fin', 'Fin', shape='oval')

dot4.edge('Inicio', 'Menu')
dot4.edge('Menu', 'LeerOpcion')
dot4.edge('LeerOpcion', 'Decision')
dot4.edge('Decision', 'LeerPrecios', label='Sí')
dot4.edge('LeerPrecios', 'CalcularTotal')
dot4.edge('CalcularTotal', 'CalcularIVA')
dot4.edge('CalcularIVA', 'CalcularTotalIVA')
dot4.edge('CalcularTotalIVA', 'EscribirResultados')
dot4.edge('EscribirResultados', 'Repetir')
dot4.edge('Repetir', 'Menu')
dot4.edge('Decision', 'Fin', label='No')

diagramas["MenuCompraRopa"] = dot4

# Guardar y devolver rutas de los diagramas generados
rutas_imagenes = {}
for nombre, dot in diagramas.items():
    ruta = f"/home/h4ck10us/Escritorio/{nombre}.png"
    dot.render(ruta[:-4], format='png', cleanup=False)
    rutas_imagenes[nombre] = ruta

# Mostrar rutas generadas
rutas_imagenes
