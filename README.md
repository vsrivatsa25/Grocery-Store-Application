# Grocery-Store-Application
As part  of task for IET Round 2, VIT Vellore.
THE GROCER'S IDEAL APPLICATION
The application has 6 commands:
1)Restock
To restock an item, enter 'restock' when asked. Then enter the item name, cost price, selling price and quantity, each of them separated by a space.
2)Sell
To sell an item, enter 'sell' when asked. Then enter the same item name earlier given, and the quantity of the item being sold, separated by a space.
3)Profits
To view the profits made so far after an amount of restocking and selling, enter 'profits' when asked.
4)View
To view the amount of stocks still left after some restocking and selling, enter 'view' when asked.
5)Sales
To view which goods have been sold so far and the amount of the goods sold, enter 'sales' when asked.
6)End
Every grocer has to end a busy day's business, and go back home. Once done with the applications, type 'end' when asked.

TEST CASE INPUT:
restock
apple 20 25 100
restock
banana 15 20 100
restock
juice 48 60 50
restock
candy 7 10 200
sell
apple 30
sell
candy 100
sell
juice 12
sell
banana 55
view
profits
sales
end

OUPUT:
The items in your stock currently, their cost price, selling price and quantity respectively are: 
['apple', '20', '25', '70']
['banana', '15', '20', '45']
['juice', '48', '60', '38']
['candy', '7', '10', '100']
Your profits earned so far is 869
Your sales so far is 
30 apples
100 candys
12 juices
55 bananas
Have a nice day!
THANK YOU!
