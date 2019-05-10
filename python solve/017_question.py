class CreditCard:
    limit = 100000

    def __init__(self, customer, account, balance, bank):
        self.details = {
            "customer": customer,
            "account": account,
            "balance": balance,
            "limit": self.limit,
            "bank": bank
        }

    def get_customer(self): return self.details["customer"]

    def get_bank(self): return self.details["bank"]

    def get_account(self): return self.details["account"]

    def get_balance(self): return self.details["balance"]

    def get_limit(self): return self.details["limit"]

    def make_payment(self, amount):
        self.details["balance"] += amount

    def charge(self, price):
        self.details["balance"] -= price

    def printDetails(self):
        print("***** Account details *****")
        for k, v in self.details.items():
            print(k, ":", v)

        print("\n")


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, account, balance, apr, bank):
        super().__init__(customer, account, balance, bank)
        self.details["apr"] = apr  # Annual percentage rate


# CreditCard class demonstration
card = CreditCard("John", "Joint", 1000, "JPL")
card.printDetails()  # Print credit card details

# Make changes and print them
card.make_payment(2000)
card.charge(500)
card.printDetails()

anotherCard = PredatoryCreditCard("Hello", "Joint", 2000, 0.12, "KTM")
anotherCard.printDetails()
