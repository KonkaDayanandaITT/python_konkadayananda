class InsufficientBalanceError(Exception):
    pass

balance = 10000
withdraw = 12000

if withdraw > balance:
    raise InsufficientBalanceError("Not enough balance")