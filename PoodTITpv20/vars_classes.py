import random as rnd
import datetime
class profile:
	def __init__(self):
		self.balance = rnd.choice(range(50,500,30))
		self.basket = []
		self.inventory = []
		self.looking_at = "shop"
	def add_good(self, gds : list, number):
		q = int(input("Введите количество "))
		self.basket.append(gds[number].take(q,gds))
	def clear_basket(self, target : list):
		for b in self.basket:
			target.append(b)
		self.basket.clear()
	def remove_from_basket(self):
		g = None
		while True:
			try:
				n = int(input("Введите номер товара "))
				q = int(input("Введите количество "))
				g = self.basket[n]
				break
			except:
				print("Ошибка!")

		return g.take(q,self.basket)
	def buy(self):
		self.inventory.extend(self.basket)
class good:
	def __init__(self, name, price, quantity=0):
		self.name = name
		self.price = price
		if quantity == 0 and not quantity < 0:
			self.quantity = rnd.randint(1,10)
		else:
			self.quantity = quantity
	def __str__(self):
		return " ".join([self.name,str(self.price)+"€",str(self.quantity)+" tk."])
	def __eq__(self, value): 
		if type(value) == good:
			return self.name == value.name and self.price == value.price
		elif type(value) == receipt:
			return False
	def __lt__(self, value):
		if type(value) == good:
			return ord(self.name[0]) < ord(value.name[0])
		else:
			return ord(self.name[0]) < ord(value.__str__()[0])



	def take(self, quantity, goods : list):
		if self.quantity <= quantity:
			goods.remove(self)
			return good(self.name,self.price,self.quantity)
		else:
			self.quantity -= quantity
			return good(self.name,self.price,quantity)
class receipt:
	def __init__(self, basket : list):
		self.history = basket.copy()
		self.date = datetime.datetime.now()
	def open(self):
		print("\n"*5)
		print(self)
		print()
		print_goods(self.history)
		print()
		print("Итого: ", sum_goods(self.history), "€")
		print("\n"*5)
	def __str__(self):
		return f"Чек на {self.date}"
	def __lt__(self,value):
		if type(value) == good:
			return ord(self.__str__()[0]) < ord(value.name[0])
		elif type(value) == receipt:
			return ord(self.__str__()[0]) < ord(value.__str__()[0])
names = ["Monster Energy","Молоко","Хлеб","Компьютер","Чипсы","Сметана",
		 "Батон","Шоколад","Лимонад","Огурец","Морковь","Банан","Яблоко","Апельсин"
		 ,"Динамик","Букет цветов","Капуста","Ананас","Диск Filosofem","Футболка",
		 "Штаны","Трусы","Носки","Смартфон","Сигареты","Пиво","Корм для собак","Бутылка воды","Сыр"
		 ]
goods = []
prof = profile()



for _ in range(rnd.randint(15,50)):
	new_good = good(rnd.choice(names),rnd.choice(range(1,200,rnd.randint(10,20))))
	goods.append(new_good)



def collapse(l : list):
	print()
	old_l = l
	new_l = [old_l[0]]
	old_l.pop(0)
	while old_l:
		if type(old_l[0]) == good:
			if old_l[0] in new_l:
				new_l[new_l.index(old_l[0])].quantity += old_l[0].quantity
			else:
				new_l.append(old_l[0])
			old_l.pop(0)
		else:
			new_l.append(old_l[0])
			old_l.pop(0)


	return new_l
goods = collapse(goods)
def print_goods(gds : list):
	i = 0
	if len(gds) == 0:
		print("Пусто")
		return
	for u in gds:
		print(f"{i}. {u}")
		i += 1


def find_expensive():
	expensive_goods = []
	expensive_price = 0
	for g in goods:
		if expensive_price < g.price:
			expensive_price = g.price
	for g in goods:
		if g.price == expensive_price:
			expensive_goods.append(g)

	return expensive_goods


def sum_goods(l : list):
	summa = 0
	for g in l:
		if type(g) == good:
			summa += g.price * g.quantity
	return summa
