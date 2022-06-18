class Tree():
	def __init__(self, value):
		self.value = value # Елемент
		self.left = None # Ліва гілка
		self.right = None # Права гілка

	# Обходимо центровано дерево та виводимо його
	def output_tree(self):
		if self.left != None:
			self.left.output_tree()
		if self.value != None:
			print(self.value, end = "   ")
		if self.right != None:
			self.right.output_tree()

	# Видаляємо усі листки (ті елементи, у яких ліва та права гілка = None)
	def delete(self):
		if self.left != None:
			self.left.delete() # Обходимо ліву гілку
		if self.right != None:
			self.right.delete() # Обходимо праву гілку
		if self.left == None and self.right == None: # Видаляємо листок
			self.value = None	


def input_tree():
	tree = Tree(int(input("Введіть елемент дерева (Ціле число): "))) # Створюємо гілку дерева
	n = int(input("Введіть кількість нащадків (0, 1, 2): ")) # Вводимо кількість нащадків
	if n == 2:
		tree.left = input_tree() # Вводимо ліву гілку
		tree.right = input_tree() # Вводимо праву гілку
	elif n == 1:
		tree.left = input_tree() # Вводимо ліву гілку
	return tree # Повертаємо гілку

def main():
	tree = input_tree() # Вводимо дерево
	print("Початкове дерево: ")
	tree.output_tree() # Виводимо початкове дерево
	print("\nМодифіковане дерево: ")
	tree.delete() # Видаляємо листки
	tree.output_tree() # Виводимо модифіковане дерево
	print()

	
if __name__ == "__main__":
	main()