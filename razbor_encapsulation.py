class Terminal:
    def __init__(self, card, pin) -> None:
        self.card = card
        self._pin = pin
        self.money = 0
        

    def validate_card(self, card):
        if len(card) == 16 and card.isdigit():
            print('Your card is valide')
        else:
            print('invalide card')

    def _validate_pin(self, pin):
        if len(pin) == 4 and pin.isdigit():
            self.pin = pin
            self.money = 0
            print('Your pin is valide')
        else:
            print('invalide pincode')

    def put(self, pin, money):
        if self._pin == pin:
            self.money += money
            print(f'''Your balance is replenished. Your bank account is {self.money}.''')
        else:
            print('Incorect pincode. Try again.')
    
    def get_money(self, pin, amount):
        if self._pin == pin:
            if self.money >= amount and amount % 10 == 0:
                self.money -= amount
                print(f'You withdrew {amount}. Current balance is {self.money}')
            elif self.money < amount:
                print(f'Not enough money. Your balance is {self.money}')
            else:
                print('Invalid withdrawal amount. Amount should be a multiple of 10.')
        else:
            print('Incorrect pin code. Try again.')


debit_card = Terminal('1234567891123456', '1234')

debit_card.validate_card('1231') 
debit_card.validate_card('1234567891123456') 

debit_card._validate_pin('fsd12')
debit_card._validate_pin('1234') 

debit_card.put('1234', 100000)   
debit_card.put('1233', 45000)

debit_card.get_money('12f', 342)
debit_card.get_money('1234', 50000)
debit_card.get_money('1234', 2500)
debit_card.get_money('1234', 15000)
debit_card.get_money('1234', 15000)
debit_card.get_money('1234', 10000)
debit_card.get_money('1234', 10000)
