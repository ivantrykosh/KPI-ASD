class Priority_queue:
	def __init__(self):
		self.__queue = [] # Створюємо пусту чергу

	def add_element(self, element, priority):
		self.__queue += [[element, priority]] # Додаємо елемент до черги

	def delete_element(self):
		maxpriority = float("inf") # Максимальний пріоритет
		ind = float("inf") # Максимальний індекс
		for i in range(len(self.__queue)): # Проходимо по черзі
			if maxpriority >= self.__queue[i][1]: # Шукаємо елемент з найбільши пріоритетом
				maxpriority = self.__queue[i][1] # Запам'ятовуємо новий пріоритет
				ind = i # Запам'ятовуємо індекс елемента з таким пріоритетом
		temp = self.__queue.pop(ind) # Видаляємо елемент з найбільшим пріоритетом
		print(f"\nВидалено елемент \'{temp[0]}\' з пріоритетом {temp[1]}")

	def change(self, index, priority): # Змінюємо пріоритет елемента за індексом
		self.__queue[index][1] = priority
		print(f"\nНовий пріоритет елемента \'{self.__queue[index][0]}\' = {self.__queue[index][1]}")

	def get_queue(self): # Отримуємо чергу
		return self.__queue

	def get_length(self): # Отримуємо довжину черги
		return len(self.__queue)

def main():
	queue = Priority_queue() # Створюємо чергу

	# Вводимо елементи черги
	flag = True
	while flag:
		choice = int(input("Ви хочете додати елемент до черги? (1/0) - "))
		if choice == 1:
			symb = input("	Введіть елемент: ")
			prior = int(input("	Введіть пріоритет елемента: "))
			queue.add_element(symb, prior)
		else:
			flag = False
	print("\nЧерга:", queue.get_queue())

	# Видаляємо елемент з найбільшим пріоритетом
	queue.delete_element()
	print("\nЧерга:", queue.get_queue())

	# Змінюємо пріоритет елемента за індексом
	ind = int(input("\nВведіть індекс елемента, який хочете змінити: "))
	if ind > queue.get_length() or ind < 1:
		print("Елемент з таким індексом відсутній!")
	else:
		newprior = int(input("	Введіть новий пріоритет: "))
		queue.change(ind-1, newprior)
	print("\nЧерга:", queue.get_queue())
	
if __name__ == "__main__":
	main()