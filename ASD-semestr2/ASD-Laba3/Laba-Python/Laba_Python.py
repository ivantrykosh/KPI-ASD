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
			if i < j:
				k = random.randint(0,2)
				if k // 2 == 0:
					A[i][j] = random.randint(1, n)
					A[j][i] = A[i][j]
	return A

def pryma(A):
	# Створюємо матрицю Т та заповнюємо її позначенням "inf"
	T = []
	for i in range(len(A)):
		temp = []
		for j in range(len(A)):
			if (i != j):
				temp += [float("inf")]
			else:
				temp += [0]
		T += [temp]

	M = A[:][:] # Робимо копію матриці А
	indexes = [0] # Список вершин, які є у графі(матриці) Т
	while len(indexes) != len(A[0]): # Поки у нас є нерозглянуті вершини
		k = None
		p = None

		e = float("inf")
		for i in indexes: # Проходимо по вже розглянутих вершинах
			for j in range(len(M[i])): # Проходимо по ребрах цієї вершини
				if i != j and e > M[i][j]: # Якщо число є цілим та меншим за "е", то присвоюємо його числу "е"
					e = M[i][j]
					k = i
					p = j
		
		for i in indexes: # Видаляємо всі ребра між розглянутими вершинами
			M[i][p] = M[p][i] = float("inf")
		T[k][p] = T[p][k] = e # Записуємо ребро у матрицю Т
		indexes += [p] # Додаємо індекс розглянутої вершини
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
	T = pryma(A)
	output(T, "T")

if __name__ == "__main__":
	main()