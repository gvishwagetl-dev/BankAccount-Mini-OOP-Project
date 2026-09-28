class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = initial_balance
        self.is_active = True

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:,.2f}")
        else:
            print("The deposit has to be positive.")

    def withdrawl(self, amount: float) -> None:
        if amount <= 0:
            print("The withdrawal has to be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:,.2f}")

    def transfer(self, target_account: "BankAccount", amount: float) -> None:
        if amount <= 0:
            print("The transfer has to be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this transfer.")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"Successfully transferred ${amount:,.2f} to {target_account.owner}")

    def __str__(self) -> str:
        return f"{self.owner} (Balance: ${self.balance:,.2f})"


vishwag: BankAccount = BankAccount(owner="Vishwag", initial_balance=2_000_000_000_000)
friend: BankAccount = BankAccount(owner="Rush", initial_balance=2_000)

deposit_input = input("Input money to deposit money into your account.")
try:
  amount = float(deposit_input)
  vishwag.deposit(amount)
except ValueError:
  print("Please put a valid number")

withdrawl_input = input("Input money to withdrawl from your account.")
try:
  amount = float(withdrawl_input)
  vishwag.withdrawl(amount)
except ValueError:
  print("Please put a valid number")

transfer_input = input("Input money to tranfer to an account.")
try:
  amount = float(transfer_input)
  vishwag.transfer(friend, amount)
except ValueError:
  print("Please put a valid number")

