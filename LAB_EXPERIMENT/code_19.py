def mincoins(coins,n,amount):
    if amount==0:
        return 0
    if amount<0:
        return 9999
    if n<=0 and amount>0:
        return 9999
    return min(1+mincoins(coins,n,amount-coins[n-1]),
        mincoins(coins,n-1,amount))

coins=[2,3]
amount=7
print(mincoins(coins,len(coins),amount))