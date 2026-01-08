from account import Account_details

def test_Account_details_output():
    result = Account_details(10001, "Riya Kamat", "Savings Account", 10000)

    expected = (
        "Account Number: 10001"
        "Account Holder Name: Riya Kamat\n"
        "Account Type: Savings Account\n"
        "Balance: 10000"
    )

    assert result == expected