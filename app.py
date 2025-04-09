# pip install sql_alchemy

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resibo.db'
app.config['SECRET_KEY'] = 'tajny_klic_obp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Identificator:
  def __init__(self, name):
    self.name = name

class Customer(Identificator, db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)

    def __init__(self, name, phone, email):
        db.Model.__init__(self)
        super().__init__(self, name)
        self.name = name
        self.phone = phone
        self.email = email

class InvoiceRule(Identificator, db.Model):
    __tablename__ = 'invoice_rules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    interval = db.Column(db.String, nullable=True)

    def __init__(self, name, interval):
        db.Model.__init__(self)
        super().__init__(self, name)
        self.name = name
        self.interval = interval

class PriceList(Identificator, db.Model):
    __tablename__ = 'pricelists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)
    price = db.Column(db.Double, nullable=False)
    currency = db.Column(db.String, nullable=False)
    valid_from = db.Column(db.DateTime, nullable=True)
    valid_to = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, code, price, currency, valid_from, valid_to):
        db.Model.__init__(self)
        super().__init__(self, name)
        self.name = name
        self.code = code
        self.price = price
        self.currency = currency
        self.valid_from = valid_from
        self.valid_to = valid_to

class Contract(Identificator, db.Model):
    __tablename__ = 'contracts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    client = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    invoice_rules = db.Column(db.Integer, db.ForeignKey('invoice_rules.id'), nullable=False)
    price_list = db.Column(db.Integer, db.ForeignKey('pricelists.id'), nullable=False)
    valid_from = db.Column(db.DateTime, nullable=True)
    valid_to = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, client, invoice_rules, price_list, valid_from, valid_to):
        db.Model.__init__(self)
        super().__init__(self, name)
        self.name = name
        self.client = client
        self.invoice_rules = invoice_rules
        self.price_list = price_list
        self.valid_from = valid_from
        self.valid_to = valid_to

class Transaction(Identificator, db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    period = db.Column(db.DateTime, nullable=False)
    contract = db.Column(db.Integer, db.ForeignKey('contracts.id'), nullable=False)
    price_list = db.Column(db.Integer, db.ForeignKey('pricelists.id'), nullable=False)
    amount = db.Column(db.Double, nullable=False)
    change = db.Column(db.Integer, nullable=False)

    def __init__(self, name, period, contract, price_list, amount, change):
        db.Model.__init__(self)
        super().__init__(self, name)
        self.name = name
        self.period = period
        self.contract = contract
        self.price_list = price_list
        self.amount = amount
        self.change = change

with app.app_context():
    db.create_all()

# Hlavní stránka
@app.route('/')
def index():
  customers = Customer.query.all()
  return render_template('index.html', customers=customers)

if __name__ == '__main__':
#    app.run(debug=True)  

  with app.app_context():
    customers = Customer.query.all()
    result = ''
    for customer in customers:
      result += f'ID: {customer.id}, Name: {customer.name}, Phone: {customer.phone}, E-mail: {customer.email}'
    print(result)

  with app.app_context():
    invoice_rules = InvoiceRule.query.all()
    result = ''
    for invoice_rule in invoice_rules:
      result += f'ID: {invoice_rule.id}, Name: {invoice_rule.name}'
    print(result)

  with app.app_context():
    price_lists = PriceList.query.all()
    result = ''
    for price_list in price_lists:
      result += f'ID: {price_list.id}, Name: {price_list.name}'
    print(result)

  with app.app_context():
    contracts = Contract.query.all()
    result = ''
    for contract in contracts:
      result += f'ID: {contract.id}, Name: {contract.name}'
    print(result)    

  with app.app_context():
    transactions = Transaction.query.all()
    result = ''
    for transaction in transactions:
      result += f'ID: {transaction.id}, Name: {transaction.name}'
    print(result)    