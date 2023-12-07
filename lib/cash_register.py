#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount =0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = []
  def add_item(self, title, price, quantity= 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(title)
      self.last_transaction.append({
        "title": title, "quantity" : quantity, "price" : price
      })        