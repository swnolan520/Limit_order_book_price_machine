# Limit order book practice
# I currently own shares in Berkshire Hathaway class B stock. Given the following price order sheet, how much can I buy 36780 shares for?

# BRBK: 356.66 
# _________________________________________
#       BID            |        ASK
#   Bid      Bid Size  |    Ask        Ask Size
#__________________________________________
# 356.65        50     |    356.67       1000
# 356.64        69     |    356.68        800
# 356.63       1000    |    356.69         30
# 356.62        41     |    356.70        100
# 356.61         1     |    356.71          1
# 356.60        10     |    356.70       1000

Shares = float(input("How many shares: "))
buy_or_sell = input("buy or sell: ")

if Shares <= 5000 and buy_or_sell == "buy" :
print("Buy For: " (356.65 * Shares))
elif Shares > 5000 or Shares <= 11900 and buy_or_sell == "buy" :
print("buy for: " ((356.65*5000)+356.64*Shares))
elif Shares > 11900 or Shares <= 21900 and buy_or_sell == "buy" :
print("buy for: " (((356.65*5000)+356.64*6900)+356.43 * Shares))
elif Shares > 21900 or Shares <= 26000 and buy_or_sell == "buy" :
print("buy for: " ((((356.65*5000)+356.64*6900)+356.43 * Shares)))
elif Shares  > 26000 or Shares <= 26100 and buy_or_sell == "buy" :
print("buy for: "((356.65*5000)+(356.64*6900)+(356.43 * 356.61)+()))
