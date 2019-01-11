#!/usr/bin/env python2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#definimos la clase pol
class pol:
	#en el init solo se encuentran dos caracteristicas la misma lista entregada y el grado del polinomio
	def __init__(self, a):
		self.a = a
		self.grado = len(self.a)-1
	def __str__(self):
	#mostrar el polinomio en pantalla
		k = ""
		#se itera sobre un range con el largo de la lista entregada menos uno, debido a que el grado del polinomio es justo ese, se hace en el sentido contrario para que el primer i sea el de mas alto grado y el primero del polinomio, esto solo por convencion.
		for i in range(len(self.a)-1,-1,-1):
			#se definen los distintos casos que pueden exisitir en los coeficientes y exponentes en un polinomio,primero el del mas alto y si el coeficiente es positivo
			if (self.a[i]>0) and (i==len(self.a)-1):
				k+= str(self.a[i])+"x^"+str(i)
			#los tres casos para cuando el exponente es 0, coeficiente positivo, negativo o igual a cero.
			elif (i==0) and (self.a[i]>0):
				k+= "+"+str(self.a[i])
			elif (i==0) and (self.a[i]<0):
				k+= str(self.a[i])
			elif (i==0) and (self.a[i]==0):
				k+= ""
			#para cualquier exponente distinto de cero)
			elif (self.a[i]>0):
				k+= "+"+str(self.a[i])+"x^"+str(i)
			#para cuando el coeficiente es 0
			elif (self.a[i]==0):
				k+= ""
			#para todos los demas casos
			else:
				k+= str(self.a[i])+"x^"+str(i)
		return k
	#se define la funcion getitem para poder llamar a los coeficientes del polinomio
	def __getitem__(self,coef):
		 return self.a[coef]
	#se define la suma de polinomios, es necesario mencionar que al no tener la misma longitud las listas era dificil sumarlas con map por lo que se busca rellenarlas con 0 hasta que tengan la misma longitud
	def __add__(self,poli):
		b=self.a[:]
		c=poli.a[:]
		while len(b)!=len(c):
			if len(b)<len(c):
				b.append(0)
			elif len(b)>len(c):
				c.append(0)
		l=map(lambda x,y: x+y,b,c)
		return pol(l)
	#se define de la misma forma que la suma pero con un menos
	def __sub__(self, poli):
		b=self.a[:]
		c=poli.a[:]
		while len(b)!=len(c):
			if len(b)<len(c):
				b.append(0)
			elif len(b)>len(c):
				c.append(0)
		l=map(lambda x,y: x-y,b,c)
		return pol(l)
#la multiplicacion se define para dos instancias, si el multiplicador es escalar u otro polinomio
	def __mul__(self,poli):
		#se copia el polinomio para no cambiarlo a partir de esta funcion		
		b=self.a[:]
		if type(poli)==int or type(poli)==float:
			l=map(lambda x: poli*x , b)
			return pol(l)
		#la multiplicacion del polinomio por otro polinomion consta de al igual que en la suma y division tener la misma longitud y luego multiplicar termino a termino y colocandolos donde sumen sus indices.
		else:
			c=poli.a[:]
			while len(b)!=len(c):
				if len(b)<len(c):
					b.append(0)
				elif len(b)>len(c):
					c.append(0)
			l=(len(self.a)+len(poli.a)-1)*[0]
			for i in range(len(self.a)):
				for j in range(len(poli.a)):
					l[i+j]+=self.a[i]*poli.a[j]
			return pol(l)
#se define la multiplicacion por la derecha
	def __rmul__(self,poli):
		return self*poli
#se define la evaluacion del polinomio en un punto
	def __call__(self,x):
		l=0.0
		#se multiplica cada coeficiente por el punto elevado al indice que corresponda a ese coeficiente
		for i in range(len(self.a)):
			l+=self.a[i]*(x**i)
		return l
#la derivacion de polinomios sigue una regla simple de multiplicar el coeficiente por el indice y colocar este resultado un indice anterior.
	def derivar(self):
		l=[]
		for i in range(1,len(self.a)):
			l.append(self.a[i]*i)
		return pol(l)
#la integracion coloca la cte que se entrega en el primer indice del polinomio y para cada coeficiente del polinomio se le divide por el indice mas 1
	def integrar(self, cte):
		l=[cte]
		for i in range(len(self.a)):
			l.append(self.a[i]/(float(i+1)))
		return pol(l)
#por la definicion de newton rampson que ocupa la tangente a una funcion en un punto dado inicial y de esa tangente vuelve a obtener otro punto que evalua y asi hasta que el numero que evalua de entre -10**12 y 10**12
	def ceros(self,semilla):
		c=self.derivar()
		while not (-10**-12)<self(semilla)<(10**-12):
			semilla= semilla-self(semilla)/c(semilla)
		return semilla
#grafica del polinomio
	def graficar(self,xmin,xmax,nombre):
		#hacemos un arrreglo de puntos a evaluar entre xmin y xmax cada 0.01
		t1=np.arange(xmin,xmax,0.01)
		#se evalua el arreglo atraves de la funcion evaluar predefinida
		plt.plot(t1,self(t1),'r', label='p(x)='+pol.__str__(self))		
		plt.legend()
		#se guarda el grafico del polinomio con el nombre que ingresa el usuario
		plt.savefig(nombre)
#se define la integral definida, se ingresan los valores del intervalo a integrar, siempre con a<b		
	def integradef(self, a , b):
		l=0.0
		f=self.integrar(b)
		g=self.integrar(b)
		l=f(b)-g(a)
		return l

		
