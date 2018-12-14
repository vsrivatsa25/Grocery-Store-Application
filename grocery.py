li=['1']
profits=0
sales=[]
while(True):
    ins=input("List of commands are restock, sell, profits, sales, end, view. Enter one ")
    if ins=="restock":
        templi=list(map(str,input("Enter the item name, cost price, selling price, quantity all separated by a space \n").split()))
        count=0
        for i in range(len(li)):
            if templi[0]==li[i][0]:
                count+=1
                break;
        if count==0:
            li.append(templi)
        else:
            for i in range(len(li)):
                if(li[i][0])==templi[0]:
                    li[i][3]=str(int(li[i][3])+int(templi[3]))
                    break;
    elif ins=="sell":
        templi=list(map(str,input("Enter the item name, quantity seperated by a space \n").split()))
        for i in range(len(li)):
            if templi[0]==li[i][0] and int(li[i][3])>=int(templi[1]):
                sal=[li[i][0],templi[1]]
                li[i][3]=str(int(li[i][3])-int(templi[1]))
                break;
            elif templi[0]==li[i][0] and int(li[i][3])<int(templi[1]):
                print("Either you do not have sufficient quantity to sell, or this product is not in your stock.")
            
        profits+=int(templi[1])*(int(li[i][2])-int(li[i][1]))        
        sales.append(sal)
    elif ins=='profits':
        print("Your profits earned so far is",profits)
    elif ins=='sales':
        print("Your sales so far is ")
        for i in range(len(sales)):
            print(sales[i][1]+" "+sales[i][0]+"s")
    elif ins=='end':
        break;
    elif ins=='view':
        print("The items in your stock currently, their cost price, selling price and quantity respectively are: ")
        for i in range(1,len(li)):
            print(li[i])
    else:
        print("Invalid input. Try Again.")
print("Have a nice day!")

    
