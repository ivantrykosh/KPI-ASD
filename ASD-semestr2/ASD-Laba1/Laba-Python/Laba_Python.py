import random

def buble_sort(array):
	size = len(array)
	counter1 = 0 #Для порівнянь
	counter2 = 0 #Для перестановок

	for i in range(size):
		for j in range(0, size - 1):
			counter1 += 1
			if array[j] > array[j+1]:
				#Міняємо елементи місцями, якщо попередній елемент більший за поточний
				counter2 += 1
				array[j], array[j+1] = array[j+1] , array[j]

	return array, counter1, counter2

def comb_sort(array):
	size = len(array)
	step = len(array)
	counter1 = 0 #Для порівнянь
	counter2 = 0 #Для перестановок
	while  step > 1:
		step = int(step / 1.247)
		if step < 1:
			step = 1
		for j in range(0, size - step):
			counter1 += 1
			if array[j] > array[j+step]:
				#Міняємо елементи місцями, якщо попередній елемент більший за поточний
				counter2 += 1
				array[j], array[j+step] = array[j+step] , array[j]

	return array, counter1, counter2

def test_buble(n):
	bestcase = [i for i in range(1, n + 1)]
	bestcase1 = bestcase[:]
	bestcase, counter1, counter2 = buble_sort(bestcase)
	output(bestcase1, bestcase, counter1, counter2, n, "Найкращий", "бульбашкою")
	
	randomcase = random.sample(range(1, n + 1), n)
	randcase = randomcase[:]
	randomcase, counter1, counter2 = buble_sort(randomcase)
	output(randcase, randomcase, counter1, counter2, n, "Випадковий", "бульбашкою")

	worstcase = [i for i in range(n, 0, -1)]
	worstcase1 = worstcase[:]
	worstcase, counter1, counter2 = buble_sort(worstcase)
	output(worstcase1, worstcase, counter1, counter2, n, "Найгірший", "бульбашкою")

	print("\n\n")

def test_comb(n):
	bestcase = [i for i in range(1, n + 1)]
	bestcase1 = bestcase[:]
	bestcase, counter1, counter2 = comb_sort(bestcase)
	output(bestcase1, bestcase, counter1, counter2, n, "Найкращий", "гребінцем")

	randomcase = random.sample(range(1, n + 1), n)
	randcase = randomcase[:]
	randomcase, counter1, counter2 = comb_sort(randomcase)
	output(randcase, randomcase, counter1, counter2, n, "Випадковий", "гребінцем")

	worstcase = [i for i in range(n, 0, -1)]
	worstcase1 = worstcase[:]
	worstcase, counter1, counter2 = comb_sort(worstcase)
	output(worstcase1, worstcase, counter1, counter2, n, "Найгірший", "гребінцем")

	print("\n")

def output(case1, case2, counter1, counter2, n, string1, string2):
	print()

	print("\n", string1," випадок для сортування ", string2, sep = "")
	if n <= 10:
		print("Вхідний масив\n", case1, "\nВихідний масив\n", case2)
	print("Кількість порівнянь:", counter1)
	print("Кількість перестановок:", counter2)

def buble_sort1(array):
	size = len(array)
	counter1 = 0 #Для порівнянь
	counter2 = 0 #Для перестановок

	for i in range(size):
		for j in range(0, size - 1):
			print(array)
			counter1 += 1
			if array[j] > array[j+1]:
				#Міняємо елементи місцями, якщо попередній елемент більший за поточний
				counter2 += 1
				array[j], array[j+1] = array[j+1] , array[j]

	print("Кількість порівнянь:", counter1)
	print("Кількість перестановок:", counter2)

def main():
	n = 100
	#array = [3, 5, 4, 1, 2]
	#buble_sort1(array)
	test_buble(n)
	test_comb(n)


main()
