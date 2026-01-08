def Account_details(acc_no, acc_holder_name, acc_type, balance):
    result = (
        f"Account Number: {acc_no}\n"
        f"Account Holder Name: {acc_holder_name}\n"
        f"Account Type : {acc_type}\n"
        f"Balance: {balance}"
    )
    return result


if __name__ == "__main__":
    acc_no = 10001
    acc_holder_name = "Riya Kamat"
    acc_type = "Savings Account"
    balance = 10000

    print(Account_details(acc_no, acc_holder_name, acc_type, balance))