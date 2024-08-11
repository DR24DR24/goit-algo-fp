items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

sum_val=100

def greedy_algorithm(items,sum):
    list_food=[]
    for index,item in items.items():
        list_item={}
        list_item["cost"]=item["cost"]
        list_item["calories"]=item["calories"]
        list_item["name"]=index
        list_item["k"]=item["calories"]/item["cost"]
        list_food.append(list_item)
    list_food.sort(key=lambda x: -x["k"])
 
    od={}
    calories=0
    for item in list_food:
        quantity=sum//item["cost"]
        calories+=quantity*item["calories"]
        sum=sum%item["cost"]
        od[item['name']]=quantity
    return sum,calories,od

res=greedy_algorithm(items,sum_val)
print(f"\ngreedy_algorithm\nsum: {sum_val}, gap: {res[0]}, calories: {res[1]} \n  {res[2]}")



def dynamic_programming(dishes,sum):
    ld={i:0 for i in dishes}
    K = [{"cost":0,"calories":0,"dishesSet":ld}\
           for s in range(sum + 1)\
        ]
    for s in range(1,sum+1):
            options=[(K[s - item["cost"]]["calories"]-item["calories"],\
                      K[s - item["cost"]]["cost"    ]+item['cost'],\
                      key\
                     ) \
                     for key,item in dishes.items() if item["cost"]<=s]
            maxOption=min(options,default=\
                          ( K[s - 1]["calories"],\
                            K[s - 1]["cost"    ],\
                           None\
                          ) \
                         )
            K[s]["cost"    ]=maxOption[1]
            K[s]["calories"]=maxOption[0]
            if maxOption[2]!=None:
                 K[s]["dishesSet"   ]=K[s-dishes[maxOption[2]]['cost']]["dishesSet"   ].copy()
                 K[s]["dishesSet"   ][maxOption[2]]+=1
            else:
                 K[s]["dishesSet"   ]=K[s-1]["dishesSet"   ]
                 

    K[sum]["calories"]*=-1#-K[val]["coinNumber"]
    return K[sum]

          

res=dynamic_programming(items,sum_val)
print(f"\ndynamic_programming\nsum: {sum_val}, gap: {sum_val-res["cost"]},\n  {res}")