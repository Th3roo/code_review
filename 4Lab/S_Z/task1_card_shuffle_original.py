import random 
 
class Card: 
 
 def init(self, name, mast, cost): 
    self.name = name 
    self.mast = mast 
    self.cost = cost 
 
def create_deck(): 
 deck = list() 
 a = ('Туз','Двойка','Тройка','Четвёрка','Пятёрка','Шестёрка','Семёрка','Восьмёрка','Девятка','Десятка','Валет','Дама','Король') 
 for i in ('Пик', 'Червей','Бубен','Треф'): 
     for j in range(len(a)): 
        deck.append(Card(a[j], i, j + 1 if j<10 else 10)) 
        random.shuffle(deck) 
        return deck 
 
deck = create_deck() 
 
Diler = list() 
Player = list() 
for i in range(2): 
 Diler.append(deck.pop()) 
 Player.append(deck.pop()) 
 
 
 
for i in range(len(Player)): 
 print(deck[i].name, deck[i].mast)