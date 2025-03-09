def is_valid_login(name, passw):
    if name == "Banane" and passw == "1234":
        print("LOGIN SUCCESSFUL!")
        return True
    else:
        print("ACCESS DENIED: Wrong name or password.\n> Try Banane and 1234.")


def is_valid_registration(name, passw, year):
    if name and passw and year:
        print("Registration successful!")
        return True
    else:
        print("REGISTRATION FAILED: All entries mandatory.")


def get_balance_if():
    return "1.000.000,00"


def deposit_if(amount):
    if amount:
        print(f"Deposit of {amount} € successful!")
    else:
        print("DEPOSIT AMOUNT MISSING.")


def withdrawal_if(amount):
    if amount:
        print(f"Withdrawal of {amount} € successful!")
    else:
        print("WITHDRAWAL AMOUNT MISSING.")


def transfer_if(name, amount, ref):
    if name and amount:
        print(f"Transfer of {amount} € to {name} successful!")
        if ref:
            print(f"Reference: {ref}")
    else:
        print("TRANSFER INFORMATION MISSING.")
