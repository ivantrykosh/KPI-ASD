import random

def matrix(): # Вводимо кількість вершин та заповнюємо випадковими числами матрицю
	n = int(input("Введіть кількість вершин: "))
	A = []
	for i in range(n):
		temp = []
		for j in range(n):
			temp += [float("inf")]
		A += [temp]
	for i in range(n):
		for j in range(n):
			if i != j:
				k = random.randint(0,2)
				if k // 2 == 0:
					A[i][j] = random.randint(1, n)
			else:
				A[i][j] = 0
	#A = [  [0,  float("inf"),    1,  float("inf"),  float("inf"),    1  ,  3],
 # [1,    0,    3,    3 , float("inf") , float("inf") ,   2],
  #[5 ,   6 ,   0   , 3    ,1  ,float("inf") ,   7],
 # [5  ,  1  ,  5  ,  0 , float("inf") , float("inf") , float("inf")],
 # [6  ,float("inf"),  float("inf")  ,  3   , 0 ,   5 , float("inf")],
  #[2  ,  5,  float("inf"), float("inf") , float("inf") ,  0    ,3],
  #[1 ,   6 ,   4 , float("inf")  ,  1  ,float("inf")  ,  0]]
	return A

def danzig(A):
	T = [] # Вихідна матриця
	
	for m in range(len(A)): # Проходимо по матриці
		# Створюємо копію матриці та заповнюємо її нескінченностями та нулем
		D = T[:]
		D.append([float("inf") for i in range(m+1)])
		for i in range(m):
			D[i].append(float("inf"))
		D[m][m] = 0

		# Проходимо по новому рядку матриці
		for j in range(m):
			min = float("inf") # Мінімальний шлях
			for k in range(m):
				if A[m][k] + T[k][j] < min: # Якщо сума елементів менша за мінімальний шлях, то присвоюємо цю суму для мінімального шляху
					min = A[m][k] + T[k][j]
			D[m][j] = min # Присвоюємо мінімальний шлях елементу скопійованої матриці

		# Проходимо по новому стовпцю матриці
		for i in range(m):
			min = float("inf") # Мінімальний шлях
			for k in range(m):
				if  T[i][k] + A[k][m] < min: # Якщо сума елементів менша за мінімальний шлях, то присвоюємо цю суму для мінімального шляху
					min = A[k][m] + T[i][k]
			D[i][m] = min # Присвоюємо мінімальний шлях елементу скопійованої матриці
		
		# Проходимо по інших елементах матриці
		for i in range(m):
			for j in range(m):
				if i != j:
					min = float("inf") # Мінімальний шлях
					if D[i][m] + D[m][j] > T[i][j]: # Якщо сума елементів більша за поточний елемент
						min = T[i][j] # Мінімальний шлях дорівнює меншому елементу
					else:
						min = D[i][m] + D[m][j] # Мінімальний шлях дорівнює сумі елементів
					D[i][j] = min # Присвоюємо мінімальний шлях елементу скопійованої матриці
		T = D[:] # Присвоюємо змінену матрицю вихідній матриці
		#output(T, "T")
	return T

def output(M, name): # Виводимо матрицю
	print("\nMatrix", name, end = ":")
	for i in M:
		print()
		for j in i:
			print(f'{j:3}', end = "  ")
	print()

def main():
	A = matrix()
	output(A, "A")
	T = danzig(A)
	output(T, "T")
	
if __name__ == "__main__":
	main()