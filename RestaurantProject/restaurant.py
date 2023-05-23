class Table:

    def __init__(self, diners):
        self.diners = diners
        self.bill = []

    def order(self, item: str, price: float, quantity: int = 1) -> None:
        order = {'item': item, 'price': price, 'quantity': quantity}
        ordered_previously = False # check if item already added to bill
        for orders in self.bill: 
            if item == orders['item'] and price == orders['price']:
                orders['quantity'] += quantity
                ordered_previously = True
                break
        if not ordered_previously:
            self.bill.append(order)

    def remove(self, item: str, price: float, quantity: int) -> bool:
        for i, orders in enumerate(self.bill):
            if item == orders['item'] and price == orders['price'] and quantity <= orders['quantity']:
                if self.bill[i]['quantity'] == quantity:
                    self.bill.remove({'item': item, 'price': price, 'quantity': quantity})            
                    return True 
                else:
                    self.bill[i]['quantity'] -= quantity
                    return True
            else:
                return False # quantity < quantity on bill or price or item not on bill
        
    def get_subtotal(self) -> float:
        subtotal = 0
        for item in self.bill:
            subtotal += item['price'] * item['quantity']
        return subtotal

    def get_total(self, tip: float = 0.10) -> dict:
        subtotal = self.get_subtotal()
        service_charge = subtotal * tip
        total = self.get_subtotal() + service_charge
        return {'Sub Total': f'£{subtotal:.2f}', 
                'Service Charge': f'£{service_charge:.2f}', 
                'Total': f'£{total:.2f}'}

    def split_bill(self) -> float:
        return round(self.get_subtotal() / self.diners, 2) 


