def empty():
	chairs_list[0] += " "
	chairs_list[1] += " "
	chairs_list[2] += " "
	chairs_list[3] += " "
	chairs_list[4] += " "
	chairs_list[5] += " "

def alf(bukva, s):
	""" Описание функции прорисовки букв в массиве"""
	if bukva == "А":
		chairs_list[0] += f"      {s}      "
		chairs_list[1] += " "*5 + s + " " + s + " "*4
		chairs_list[2] += " "*4 + s + " "*3 + s + " "*3
		chairs_list[3] += " "*3 + s + " " + s + " " + s + " " + s + " "*2
		chairs_list[4] += " "*2 + s + " "*7 + s + " "
		chairs_list[5] += " " + s + " "*9 + s
	elif bukva == "Б":
		chairs_list[0] += " " + s + " " + s + " " + s + " " + s + " " + s + " "*2
		chairs_list[1] += " " + s + " "*10
		chairs_list[2] += " " + s + " " + s + " " + s + " " + s + " " + s + " "*2
		chairs_list[3] += " " + s + " "*9 + s
		chairs_list[4] += " " + s + " "*9 + s
		chairs_list[5] += " " + s + " " + s + " " + s + " " + s + " " + s + " "*2
	elif bukva == "В":
		chairs_list[0] += " " + s + " " + s + " " + s + " " + s + " "*4
		chairs_list[1] += " " + s + " "*7 + s + " "*2
		chairs_list[2] += " " + s + " " + s + " " + s + " " + s + " " + s + " "*2
		chairs_list[3] += " " + s + " "*8 + s + " "
		chairs_list[4] += " " + s + " "*8 + s + " "
		chairs_list[5] += " " + s + " " + s + " " + s + " " + s + " " + s + " "*2
	elif bukva == "Г":
		chairs_list[0] += " " + s + " " + s + " " + s + " " + s + " " + s + " "*2
		chairs_list[1] += " " + s + " "*10
		chairs_list[2] += " " + s + " "*10
		chairs_list[3] += " " + s + " "*10
		chairs_list[4] += " " + s + " "*10
		chairs_list[5] += " " + s + " "*10
	elif bukva == "Д":
		chairs_list[0] += "      " + s + "     "
		chairs_list[1] += "     " + s + " " + s + "    "
		chairs_list[2] += "    " + s + "   " + s + "   "
		chairs_list[3] += "   " + s + "     " + s + "  "
		chairs_list[4] += " " + s + " " + s + " " + s + " " + s + " " + s + " " + s + ""
		chairs_list[5] += " " + s + "         " + s + ""
	elif bukva == "Е" or bukva == "Ё":
		chairs_list[0] += " " + s + " " + s + " " + s + " " + s + " " + s + "  "
		chairs_list[1] += " " + s + "          "
		chairs_list[2] += " " + s + " " + s + " " + s + " " + s + " " + s + "  "
		chairs_list[3] += " " + s + "          "
		chairs_list[4] += " " + s + "          "
		chairs_list[5] += " " + s + " " + s + " " + s + " " + s + " " + s + "  "
	elif bukva == "Ж":
		chairs_list[0] += " " + s + "    " + s + "    " + s + ""
		chairs_list[1] += "  " + s + "   " + s + "   " + s + " "
		chairs_list[2] += "   " + s + "  " + s + "  " + s + "  "
		chairs_list[3] += "   " + s + "  " + s + "  " + s + "  "
		chairs_list[4] += "  " + s + "   " + s + "   " + s + " "
		chairs_list[5] += " " + s + "    " + s + "    " + s + ""
	elif bukva == "З":
		chairs_list[0] += "   " + s + " " + s + " " + s + " " + s + "  "
		chairs_list[1] += "           " + s + ""
		chairs_list[2] += "   " + s + " " + s + " " + s + " " + s + "  "
		chairs_list[3] += "           " + s + ""
		chairs_list[4] += "           " + s + ""
		chairs_list[5] += "   " + s + " " + s + " " + s + " " + s + "  "
	elif bukva == "И" or bukva == "Й":
		chairs_list[0] += " " + s + "         " + s + ""
		chairs_list[1] += " " + s + "       " + s + " " + s + ""
		chairs_list[2] += " " + s + "     " + s + "   " + s + ""
		chairs_list[3] += " " + s + "   " + s + "     " + s + ""
		chairs_list[4] += " " + s + " " + s + "       " + s + ""
		chairs_list[5] += " " + s + "         " + s + ""
	elif bukva == "К":
		chairs_list[0] += " " + s + "       " + s + "  "
		chairs_list[1] += " " + s + "     " + s + "    "
		chairs_list[2] += " " + s + "   " + s + "      "
		chairs_list[3] += " " + s + "   " + s + "      "
		chairs_list[4] += " " + s + "      " + s + "   "
		chairs_list[5] += " " + s + "         " + s + ""
	elif bukva == "Л":
		empty()
	elif bukva == "М":
		empty()
	elif bukva == "Н":
		empty()
	elif bukva == "О":
		empty()
	elif bukva == "П":
		empty()
	elif bukva == "Р":
		empty()
	elif bukva == "С":
		empty()
	elif bukva == "Т":
		empty()
	elif bukva == "У":
		empty()
	elif bukva == "Ф":
		empty()
	elif bukva == "Х":
		empty()
	elif bukva == "Ц":
		empty()
	elif bukva == "Ч":
		empty()
	elif bukva == "Ш":
		empty()
	elif bukva == "Щ":
		empty()
	elif bukva == "Ъ":
		empty()
	elif bukva == "Ы":
		empty()
	elif bukva == "Ь":
		empty()
	elif bukva == "Э":
		empty()
	elif bukva == "Ю":
		empty()
	elif bukva == "Я":
		empty()
	else:
		chairs_list[0] += " |" + s + "|"
		chairs_list[1] += " |" + s + "|"
		chairs_list[2] += " |" + s + "|"
		chairs_list[3] += " |" + s + "|"
		chairs_list[4] += " |" + s + "|"
		chairs_list[5] += " |" + s + "|"

def test(text):
	pass
	return False

# Запрашиваем Имя
name = input("Введите Имя, которое будем печатать: ").upper()
# Запрашиваем Сисвол
sim = input("Введите Символ, которым будем печатать: ")
# Задаем значение массива
chairs_list = [""]*6

# Вычесляем значение ячеек массива
#for bykva in name:
#	alf(bykva, sim)
# Выводим массив на печать
#for row in chairs_list:
#	print(row)

print("      {0}      {0} {0} {0} {0} {0}   {0} {0} {0} {0}     {0} {0} {0} {0} {0}        {0}     ".format(sim))
print(f"     {sim} {sim}     {sim}           {sim}       {sim}   {sim}               {sim} {sim}    ")
print(f"    +   +    + + + + +   + + + + +   +              +   +   ")
print(f"   + + + +   +         + +        +  +             +     +  ")
print(f"  +       +  +         + +        +  +           + + + + + +")
print(f" +         + + + + + +   + + + + +   +           +         +")