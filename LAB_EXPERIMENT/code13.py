def knapsack01(weight, prices, W):
    n=len(weight)
    items=[]
    for i in range(n):
        ratio=prices[i]/weight[i]
        items.append((ratio, weight[i], prices[i],i))
    items.sort(key=lambda x:x[0],reverse=True)  
    total_profit=0
    selected_items=[]
    for ratio, w, p, i in items:
        if W>=w:
            selected_items.append(i)
            total_profit+=p
            W-=w
    print("Selected items:", selected_items)
    print("Total profit:", total_profit)        
    #return total_profit, selected_items          
    
weight=[10,30,25,60,90,140]
prices=[60,30,100,250,180,520]
W=100 #maximum carrying capacity of the bag
knapsack01=(weight,prices,W) 