#!/usr/bin/env python2
from polinomio import pol

A = pol([1., 2., 1.])
B = pol([1., 1.])

# IMPRESION EN PANTALLA
print "El primer polinomio es A =", A
print "El segundo polinomio es B =", B
print
# OPERACIONES BASICAS
print "A + B =", A+B
print "A - B =", A-B
print "A * B =", A*B
print
# OBTENER COEFICIENTES Y EVALUAR LOS POLINOMIOS
print "El segundo coeficiente del polinomio A es", A[1]
print "El polinomio B evaluado en x = 3 es", B(3)
print
# DERIVADAS E INTEGRALES
print "La derivada del polinomio A es", A.derivar()
print "La integral del polinomio B con constante de integracion 2 es", B.integrar(2.)
print
# CEROS Y GRAFICO
print "Uno de los ceros del polinomio A es", A.ceros(0.0)
print
A.graficar(-10., 10., "grafico.png")
print "Se ha guardado una grafica del polinomio A para valores de x entre (-10, 10)"


