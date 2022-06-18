def sort_numb_inv(Array):
	lenght = len(Array) # Довжина масиву
	mid = lenght // 2 # Середина масиву
	if lenght <= 1: # Якщо довжина масиву <= 1, то повертаємо цей масив і кількість інверсій (0)
		return Array, 0
	else:
		LeftPart, leftnumb = sort_numb_inv(Array[:mid]) # Викликаємо функцію для лівої частини
		RightPart, rightnumb = sort_numb_inv(Array[mid:]) # Викликаємо функцію для правої частини
		Array, numb = merge_numb_inv(LeftPart, RightPart) # Викликаємо функцію для склеювання лівої та правої частин
		return Array, leftnumb + rightnumb + numb # Повертаємо масив та кількість інверсій

def merge_numb_inv(Leftpart, Rightpart):
	lenght_Leftpart = len(Leftpart) # Довжина лівої частини початкового масиву
	lenght_Rightpart = len(Rightpart) # Довжина правої частини початкового масиву
	i = j = 0 # Індекси лівої та правої частин початкового масиву
	numb = 0 # Кількість інверсій

	max_value = max(Leftpart) + max(Rightpart) + 1 # Максимальне значення для масивів
	Leftpart += [max_value] # Додаємо максимальне значення в лівий масив
	Rightpart += [max_value] # Додаємо максимальне значення в правий масив
	Array = [] # Склеєний масив

	for k in range(lenght_Leftpart + lenght_Rightpart):
		if Leftpart[i] <= Rightpart[j]: # Якщо елемент з лівого масиву менший за елемент з правого масиву, то додаємо його до склеєного масиву
			Array += [Leftpart[i]]
			i += 1
		else: # Інакше додаємо елемент з правого масиву і збільшуємо кількість інверсій
			Array += [Rightpart[j]]
			j += 1
			numb += lenght_Leftpart - i # Збільшуємо кількість інверсій

	return Array, numb # Повертаємо склеєний масив та кількість інверсій

def change(listofusers, usernumber):

	for i in range(len(listofusers)):
		if i != usernumber:
			k = 0 # Індекс елементів головного масиву (з індексом 'usernumber')
			for j in range(len(listofusers[i])):
				while listofusers[i][j] != listofusers[usernumber][k]: # Проходимо до головному масиву і шукаємо співпадіння елементів
					k += 1 # Збільшуємо індекс
				else: # Після зевершення циклу записуємо індекс шуканого елемента з головного масиву в масив і обнуляємо лічильник
					listofusers[i][j] = k + 1
					k = 0
				
	return listofusers

def main():
	filename1 = input("Введіть вхідного назву файлу (Наприклад: \"input_31\"): ") + ".txt" # Вводимо назву файлу
	filename2 = "ip11_trykosh_31_output.txt"
	fileIn = open(filename1, "r")
	fileOut = open(filename2, "w")

	infaboutusers = fileIn.readline()
	listofusers = fileIn.readlines()
	
	#Створюємо масив масивів і зводимо його до цілих чисел
	infaboutusers = infaboutusers.split()
	for i in range(int(infaboutusers[0])):
		listofusers[i] = listofusers[i].split()
	
	for i in range(len(listofusers)):
		listofusers[i] = listofusers[i][1:]
		for j in range(len(listofusers[i])):
			listofusers[i][j] = int(listofusers[i][j]) 
	
	#print("Початкові масиви:", *listofusers, sep = "\n")
	usernumber = int(input("\nВведіть номер масиву: ")) - 1 # Вводимо номер 
	numbofinv = 0 # Кількість інверсій
	listofusers = change(listofusers, usernumber) # Змінюємо масиви
	#print("\nЗмінені масиви:", *listofusers, sep = "\n", end = "\n\n")

	listofusers[usernumber], numbofinv = sort_numb_inv(listofusers[usernumber]) # Сортуємо головний масив
	#print("Змінений сортований головний масив: ", listofusers[usernumber], "\nВідсортовані масиви та кількість в них інверсій", sep = "\n", end = "\n") # Виводимо головний масив
	l = [] # Список з номером масиву та кількістю інверій
	for i in range(int(infaboutusers[0])):
		if i != usernumber:
			#print(i + 1,':',listofusers[i], '- ', end = '')
			listofusers[i], numbofinv = sort_numb_inv(listofusers[i]) # Сортуємо масиви та рахуємо інверсії
			#print(numbofinv)
			l += [[i + 1, numbofinv]]

	# Сортуємо списки за зростанням останнього елемента
	for i in range(len(l)):
		for j in range(len(l) - 1):
			if l[j][1] > l[j + 1][1]:
				l[j], l[j + 1] = l[j + 1], l[j]
	
	# Записуємо у файл
	fileOut.write(str(usernumber + 1) + "\n")
	for i in l: 
		fileOut.write(str(i[0]) + " " + str(i[1]) + "\n")
	fileOut.write(str(usernumber + 1))

	fileIn.close()
	fileOut.close()

if __name__ == "__main__":
	main()