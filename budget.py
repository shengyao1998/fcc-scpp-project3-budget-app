class Category:
  def __init__ (self, name):
    self.name = name
    self.ledger = []
    self.balance = 0
    self.spent = 0

  def __str__(self):
    title = self.name.center(30, "*") + "\n"
    lines = ""
    for item in self.ledger:
        des = item["description"][:23]
        amt = "{:.2f}".format(item["amount"])
        line = des.ljust(23) + amt.rjust(7) + "\n"
        lines += line

    return title + lines + "Total: {:.2f}".format(self.balance)


  ############
  # Depost
  ############
  def deposit(self, amount, description = ""):
      self.ledger.append({"amount": amount, "description": description})
      self.balance += amount

  
  ############
  # Withdraw
  ############
  def withdraw (self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -(amount), "description": description})
      self.balance -= amount
      self.spent += amount
      return True
    else:
      return False


  ############
  # Balance
  ############
  def get_balance(self):
    return self.balance


  ############
  # Transfer
  ############
  def transfer (self, amount, group):
    if self.check_funds(amount):
      self.withdraw(amount, description = "Transfer to " + group.name)
      group.deposit(amount, description = "Transfer from " + self.name)
      return True
    else:
      return False


  ############
  # Check Funds
  ############
  def check_funds(self, amount):
    return self.balance >= amount


############
# Generate Spending Chart
############
def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  total = 0
  percent = []
  max_len = 0
  
  for category in categories:
    total += category.spent
    max_len = len(category.name) if len(category.name) > max_len else max_len

  for category in categories:
    percent.append(int(((category.spent/total) * 100) // 10))

  for i in range(100, -1, -10):
    line = str(i).rjust(3) + "|"
    for j in percent:
      if j*10 >= i:
        line += " o "
      else:
        line += "   "
    line += " \n"
    chart += line
    
  chart += "    ----------\n"

  for i in range(max_len):
    line = "    "
    for cat in categories:
      if i < len(cat.name):
        line += " {0} ".format(cat.name[i])
      else:
        line += "   "

    line += " \n"
    chart += line

  return chart[:-1]