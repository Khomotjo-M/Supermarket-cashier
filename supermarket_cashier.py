#went to shoprite and wondered about the software the cashiers are using for products payments.


#----------------------items with prices stored in the system settings

stock =  {"bread": 15,"cereal":25,"beef":99,'porkribs':150,'rice':50,'fish':29,'water':30,'washing_powder':30,"milk":30,'toothpaste':19}




#getting products and calculating discounts:
    
prod = {}
turns = True

while turns:
    item = input("Enter item: ")
    if item in stock.keys():
        prod[item] = stock[item]
        if item == "milk":
            x =  stock[item]- (stock[item] *5/100)
            prod[item] = x
            print(f"{item} added to cart price= {prod[item]}")
        elif item == "beef":
            b = prod[item]-(prod[item]* 11/100)
            prod[item] = b
            print(f"{item} added to cart price= {prod[item]}")
        elif item == "bread":
            y = prod[item]-(prod[item]* 5/100)
            prod[item] = y
            print(f"{item} added to cart price= {prod[item]}")
            
        elif item == "cereal":
            n= prod[item]-(prod[item]* 10/100)
            prod[item] = n
        else:
            print(f"{item} added to cart price= {prod[item]}")
        
    else:
        turns = False
        print("Item not found")
    
        break

#total of cart price          
list1 = prod.values() 
print("Your bill = ",sum(list1  ))




