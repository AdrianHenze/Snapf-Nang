from code.backend import *

def is_valid_login(name, passw):
    if name and passw:
        rc = login(name, passw)
        if rc == -1 or rc == -2:
            print("❌ ACCESS DENIED.")
            return rc
        print("✅ Login successful.")
        return 0
    else:
        print("❌ LOGIN FAILED: Missing information.")
        return -3


def is_valid_registration(name, passw, year):
    if name and passw and year:
        try:
            y = int(year)
            current_year = datetime.now().year
            if y < 1900 or y > current_year:
                raise ValueError
        except ValueError:
            print("❌ REGISTRATION FAILED: Year of Birth invalid.")
            return False
        if y > current_year-18:
            print("❌ REGISTRATION FAILED: You are too young.")
            return False
        rc = konto_erstellen(name, passw)
        if rc == -1:
            print("❌ REGISTRATION FAILED: Name is already in use.")
            return False
        print("✅ Registration successful.")
        return True
    else:
        print("❌ REGISTRATION FAILED: All entries mandatory.")


def get_balance_if():
    balance = get_kontostand()
    f_balance = f"{balance:,.2f}"
    f_balance = f_balance.replace(',', '!').replace('.', ',').replace('!', '.')
    return f_balance


def get_transactions_if():
    return get_kontoauszug()


def deposit_if(amount):
    if amount:
        try:
            amount = round(float(amount), 2)
            if amount < 0.01:
                raise ValueError
            elif amount > 999999999999:
                print("❌ DEPOSIT AMOUNT TOO BIG.")
                return
        except ValueError:
            print("❌ DEPOSIT AMOUNT INVALID.")
            return
        einzahlen(amount)
        print(f"✅ Deposit of {amount:.2f} € successful.")
    else:
        print("❌ DEPOSIT AMOUNT MISSING.")


def withdrawal_if(amount):
    if amount:
        try:
            amount = round(float(amount), 2)
            if amount < 0.01:
                raise ValueError
            elif amount > 999999999999:
                print("❌ WITHDRAWAL AMOUNT TOO BIG.")
                return
        except ValueError:
            print("❌ WITHDRAWAL AMOUNT INVALID.")
            return
        rc = abheben(amount)
        if rc == -1:
            print("❌ WITHDRAWAL DENIED: Not enough money in the bank.")
        else:
            print(f"✅ Withdrawal of {amount:.2f} € successful.")
    else:
        print("❌ WITHDRAWAL AMOUNT MISSING.")


def transfer_if(name, amount, ref):
    if name and amount:
        try:
            amount = round(float(amount), 2)
            if amount < 0.01:
                raise ValueError
            elif amount > 999999999999:
                print("❌ TRANSFER AMOUNT TOO BIG.")
                return
        except ValueError:
            print("❌ TRANSFER AMOUNT INVALID.")
            return
        rc = ueberweisung(name, amount)
        if rc == -1:
            print("❌ TRANSFER DENIED: Not enough money in the bank.")
        else:
            print(f"✅ Transfer of {amount:.2f} € to {name} successful.")
            if ref:
                print(f"> Reference: {ref}")
    else:
        print("❌ TRANSFER INFORMATION MISSING.")


def logout_if():
    logout()
    print("✅ Logout successful.")
