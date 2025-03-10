from code.backend import *

def is_valid_login(name, passw):
    rc = login(name, passw)
    if rc == -1 or rc == -2:
        print("❌ ACCESS DENIED.")
        return rc
    print("✅ Login successful.")
    return True


def is_valid_registration(name, passw, year):
    if name and passw and year:
        rc = konto_erstellen(name, passw)
        if rc == -1:
            print("❌ REGISTRATION FAILED: Name is already in use.")
            return False
        print("✅ Registration successful.")
        return True
    else:
        print("❌ REGISTRATION FAILED: All entries mandatory.")


def get_balance_if():
    balance = round(get_kontostand(), 2)
    return str(balance).replace('.', ',')


def get_transactions_if():
    return get_kontoauszug()


def deposit_if(amount):
    if amount:
        amount = round(float(amount), 2)
        einzahlen(amount)
        print(f"✅ Deposit of {amount} € successful.")
    else:
        print("❌ DEPOSIT AMOUNT MISSING.")


def withdrawal_if(amount):
    if amount:
        amount = round(float(amount), 2)
        rc = abheben(amount)
        if rc == -1:
            print("❌ WITHDRAWAL DENIED: Not enough money in the bank.")
        else:
            print(f"✅ Withdrawal of {amount} € successful.")
    else:
        print("❌ WITHDRAWAL AMOUNT MISSING.")


def transfer_if(name, amount, ref):
    if name and amount:
        amount = round(float(amount), 2)
        rc = ueberweisung(name, amount)
        if rc == -1:
            print("❌ TRANSFER DENIED: Not enough money in the bank.")
        else:
            print(f"✅ Transfer of {amount} € to {name} successful.")
            if ref:
                print(f"> Reference: {ref}")
    else:
        print("❌ TRANSFER INFORMATION MISSING.")


def logout_if():
    logout()
    print("✅ Logout successful.")
