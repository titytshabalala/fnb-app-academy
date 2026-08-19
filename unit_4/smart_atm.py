"""
Simulate a bank transaction checking if a user has enough money.

1. Set a fixed variable
2. Ask the user how much they want to withdraw
3. If the request is less than or equal to the balance
deduct the amount and print: "Withdrawal successful! Remaining balance: RX".
4. If attempt to withdraw a negative amount or zero?
Add an elif statement checking if the request is less than or equal to 0.
If so, print: "Invalid amount". You must withdraw more than "R0".
5. Otherwise (else), print: "Declined. Insufficient funds"

"""
# Set current bank balance to R500
BANK_BALANCE = 500

withdrawal = int(input("How much are you looking to withdraw: "))

# check if user withdraws more than available bank balance

if withdrawal > BANK_BALANCE:
    print("Decline. Insufficient funds")
elif withdrawal < 0:
    print("Invalid amount")
else:
    amount = BANK_BALANCE - withdrawal
    print(f"Withdrawal successful! Remaining balance: R{str(amount)}")

