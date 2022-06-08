from __future__ import annotations


class Order:
    def __init__(self, received: str, is_prepaid: bool, number: int, price: int, customer: Customer):
        self.received = received
        self.is_prepaid = is_prepaid
        self.number = number
        self.price = price
        self.customer = customer
        self.products: list[OrderLine] = []

    def dispatch(self):
        ...

    def close(self):
        ...


class OrderLine:
    def __init__(self, order: Order, product: str, quantity: int, price: int):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price


class Customer:
    def __init__(self, name: str, address: str, rating: int):
        self.name = name
        self.address = address
        self.credit_rating = rating
        self.orders: list[Order] = []


class PersonalCustomer(Customer):
    def __init__(self, name: str, address: str, rating: int, card_nr: int):
        super().__init__(name, address, rating)
        self.card_nr = card_nr


class CorporateCustomer(Customer):
    def __init__(self, name: str, address: str, rating: int, contact_name: str, credit_limit: int):
        super().__init__(name, address, rating)
        self.contact_name = contact_name
        self.credit_limit = credit_limit

    def remind(self):
        ...
