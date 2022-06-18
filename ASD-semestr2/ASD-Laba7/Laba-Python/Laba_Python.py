from random import randint

class List_node:
	'''Цей клас є представленням елемента двозв'язного списку'''

	# Конструктор для ініціалізації значення елемента та покажчика на попередній та наступний елемент
	def __init__(self, value):
		self.value = value
		self.next = None
		self.previous = None
		return

	# Метод для визначення, чи дорівнює елемент списку переданому значенню
	def is_value(self, value):
		if value == self.value:
			return True
		else:
			return False

class Double_List:
	'''Цей клас є представленням двозв'язного списку'''

	# Констуктор для ініціалізації початку та кінця двозв'язного списку
	def __init__(self):
		self.head = None
		self.tail = None
		return

	# Метод для визначення довжини списку
	def length_of_list(self):
		count = 0
		this_node = self.head
		while this_node is not None:
			count = count + 1
			this_node = this_node.next
		return count

	# Метод для виводу двозв'язного списку
	def output_list(self):
		this_node = self.head
		while this_node is not None:
			print(this_node.value, end = ", ")
			this_node = this_node.next
		return

	# Пошук Фібоначчі для двозв'язного списку
	def search_of_fibonacci(self, value):
		fib_prev2 = 0 # Позапопереднє число
		fib_prev1 = 1 # Попереднє число
		fib_current = fib_prev2 + fib_prev1 # Поточне число
		n = self.length_of_list() # Довжина списку

		counter1 = 0 # Кількість порівнянь
		counter2 = 0 # Кількість звертань
		counter3 = 0 # Кількість ітерацій
		# Знаходимо мінімальне число Фібоначчі, яке більше за розмір списку
		while fib_current < n:
			counter1 += 1
			counter3 += 1
			fib_prev2 = fib_prev1
			fib_prev1 = fib_current
			fib_current = fib_prev2 + fib_prev1
		counter1 += 1

		offset = -1 # Для позначення виключених спереду значень
		while fib_current > 1:
			counter1 += 1
			counter3 += 1
			i = min(offset+fib_prev2, n-1)

			# Знаходимо елемент з індексом і
			temp = self.head
			counter2 += 1
			for j in range(i):
				counter2 += 1
				temp = temp.next

			counter1 += 1
			counter2 += 1
			# Якщо елемент менший за потрібний, то беремо ліву частину
			if temp.value < value:
				fib_current = fib_prev1
				fib_prev1 = fib_prev2
				fib_prev2 = fib_current - fib_prev1
				offset = i

			# Якщо елемент більший за потрібний, то беремо праву частину
			elif temp.value > value:
				counter1 += 1
				counter2 += 1
				fib_current = fib_prev2
				fib_prev1 = fib_prev1 - fib_prev2
				fib_prev2 = fib_current - fib_prev1

			# Інакше елемент знайдено
			else:
				counter1 += 1
				counter2 += 1
				return i, counter1, counter2, counter3

		counter1 += 1
		counter2 += 1
		# Перевірка останнього елемента
		if fib_prev1 and self.tail.value == value:
			return n-1, counter1, counter2, counter3
		return -1, counter1, counter2, counter3 # Елемент не знайдено

	# Метод для додавання елемента в кінець списку
	def add_node(self, node):
		if self.head is None:
			self.head = node
			node.previous = None
			node.next = None
			self.tail = node
		else:
			self.tail.next = node
			node.previous = self.tail
			self.tail = node
		return

# Пошук Фібоначчі для масиву
def search_of_fibonacci(value, arr):
	fib_prev2 = 0 # Позапопереднє число
	fib_prev1 = 1 # Попереднє число
	fib_current = fib_prev2 + fib_prev1 # Поточне число
	n = len(arr) # Довжина масиву

	counter1 = 0 # Кількість порівнянь
	counter2 = 0 # Кількість звертань
	counter3 = 0 # Кількість ітерацій
	# Знаходимо мінімальне число Фібоначчі, яке більше за розмір масиву
	while fib_current < n:
		counter1 += 1
		counter3 += 1
		fib_prev2 = fib_prev1
		fib_prev1 = fib_current
		fib_current = fib_prev2 + fib_prev1
	counter1 += 1

	offset = -1 # Для позначення виключених спереду значень
	while fib_current > 1:
		counter1 += 1
		counter3 += 1
		i = min(offset+fib_prev2, n-1)
		
		# Якщо елемент менший за потрібний, то беремо ліву частину
		counter1 += 1
		counter2 += 1
		if arr[i] < value:
			fib_current = fib_prev1
			fib_prev1 = fib_prev2
			fib_prev2 = fib_current - fib_prev1
			offset = i

		# Якщо елемент більший за потрібний, то беремо праву частину
		elif arr[i] > value:
			counter1 += 1
			counter2 += 1
			fib_current = fib_prev2
			fib_prev1 = fib_prev1 - fib_prev2
			fib_prev2 = fib_current - fib_prev1

		# Інакше елемент знайдено
		else:
			counter1 += 1
			counter2 += 1
			return i, counter1, counter2, counter3

	counter1 += 1
	counter2 += 1
	# Перевірка останнього елемента
	if fib_prev1 and arr[n-1] == value:
		return n-1, counter1, counter2, counter3

	return -1, counter1, counter2, counter3 # Елемент не знайдено

def main():
	# Введення розміру масиву
	n = int(input("Введіть розмір масиву/списку: "))

	# Ініціалізація масиву унікальними числами
	l = []
	for i in range(n):
		temp = randint(1, n ** 2)
		while temp in l:
			temp = randint(1, n ** 2)
		l += [temp]
	l.sort()

	# Створення двозв'язного списку
	doublelist = Double_List()
	for i in range(n):
		temp = List_node(l[i])
		doublelist.add_node(temp)
	
	# Виведення масиву та списку
	#print("Масив: ", l)
	print("Двозв'язний список:")
	doublelist.output_list()

	# Введення елемента
	value = int(input("\nВведіть елемент: "))

	# Пошук Фібоначчі
	index1, counter1, counter2, counter3 = search_of_fibonacci(value, l)
	if index1 == -1:
		print(f"Елемента {value} в масиві немає!")
	else:
		print(f"Елемент {value} має індекс {index1 + 1} у масиві")
		print(f"Кількість порівнянь у масиві: {counter1}, кількість звертань: {counter2}, кількість ітерацій: {counter3}")
	index2, counter1, counter2, counter3 = doublelist.search_of_fibonacci(value)
	if index2 == -1:
		print(f"Елемента {value} в списку немає!")
	else:
		print(f"Елемент {value} має індекс {index2 + 1} у списку")
		print(f"Кількість порівнянь у списку: {counter1}, кількість звертань: {counter2}, кількість ітерацій: {counter3}")

	return

if __name__ == "__main__":
	main()