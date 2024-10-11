"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000 print a message.

    You can assume that 1 Bitcoin is worth $40,000

    ===> You've redeemed a hint. Replace the _'s with code to complete this exercise.

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(investment_in_usd, usd_value):
  usd_value = investment_in_bitcoin * bitcoin_to_usd
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if investment_in_usd <= 30000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")


# 2) use function to calculate if its below $X