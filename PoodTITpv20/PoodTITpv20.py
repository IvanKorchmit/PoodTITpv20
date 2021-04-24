import vars_classes as vr
import pickle as pc


def print_help():
	print()
	print("======================")
	print("1. Пробить на кассу")
	print("2. Добавить товар в корзину")
	print("3. Очистить корзину")
	print("4. Убрать товар из корзины")
	print("5. Найти самый дорогой товар")
	print("6. Открыть корзину")
	print("7. Посмотреть товары")
	print("8. Открыть инвентарь")
	print("9. Отсортировать товары")
	print("10. Открыть чек")
	print("11. Выйти из программы")
	print("\n"*2)
	if vr.prof.looking_at == "shop":
		print("== Доступные товары ==")
		print()
		vr.print_goods(vr.goods)
		print()
	elif vr.prof.looking_at == "basket":
		print("== Корзина ==")
		print()
		vr.print_goods(vr.prof.basket)
		print()
		print("Итоговая сумма: ",vr.sum_goods(vr.prof.basket),"€")
	elif vr.prof.looking_at == "inventory":
		print("== Инвентарь ==")
		print()
		vr.print_goods(vr.prof.inventory)
		print()
		print("Итоговая сумма: ",vr.sum_goods(vr.prof.inventory),"€")
	print("======================")
	print(f"Баланс: {vr.prof.balance}€")


while True:
	try:
		open("inv.pickle")
		ans = input("Мы нашли файл с инвентарем. Не хотите ли вы его загрузить? y/n ")
		if ans == "y":
			vr.prof.inventory = pickle.load(open("inv.pickle", "rb", -1))
			break
		elif ans == "n":
			break
	except:
		break


while True:
	print_help()
	comm = input()
	if comm == "1":
		s = vr.sum_goods(vr.prof.basket)
		if s == 0:
			print("У вас в корзине ничего нет!")
			continue
		while True:
			ans = input("Вы уверены? y/n ")
			if ans == "y":
				if vr.prof.balance >= s:
					vr.prof.balance -= s
					vr.prof.buy()
					vr.prof.inventory = vr.collapse(vr.prof.inventory)
					ans = input("Хотите сохранить чек? y/n ")
					while True:
						if ans == "y":
							vr.prof.inventory.append(vr.receipt(vr.prof.basket))
							break
						elif ans == "n":
							break
					break
				else:
					print("У вас не хватает средств")
					break
			elif ans == "n":
				break
	elif comm == "2":
		vr.prof.add_good(vr.goods,int(input("Введите номер товара: ")))
		vr.prof.basket = vr.collapse(vr.prof.basket)
	elif comm == "3":
		vr.prof.clear_basket(vr.goods)
		vr.goods = vr.collapse(vr.goods)
	elif comm == "4":
		vr.goods.append(vr.prof.remove_from_basket())
		vr.goods = vr.collapse(vr.goods)
	elif comm == "5":
		print("\n"*5)
		print("Самые дорогие товары:")
		vr.print_goods(vr.find_expensive())
		print("\n"*5)
	elif comm == "6":
		vr.prof.looking_at = "basket"
	elif comm == "7":
		vr.prof.looking_at = "shop"
	elif comm == "8":
		vr.prof.looking_at = "inventory"
	elif comm == "9":
		vr.goods.sort()
	elif comm == "10":
		while True:
			try:
				n = int(input("Введите номер чека: "))
				if type(vr.prof.inventory[n]) == vr.receipt:
					vr.prof.inventory[n].open()
					break
				else:
					print("Это не чек!")
			except:
				print("Ошибка!")
	elif comm == "11":
		break



print("Программа завершена")
while True:
	ans = input("Не хотите ли вы сохранить ваш инвентарь? y/n ")
	if ans == "y":
		with open("inv.pickle", "wb") as file_:
			pickle.dump(vr.prof.inventory, file_, -1)
			break
	elif ans == "n":
		break