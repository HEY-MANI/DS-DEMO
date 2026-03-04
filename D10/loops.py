# str1="you are handsome"
# x=1
# for i in str1:
#     # print(i)
#     # print('i')
#     # print(x,i)
#     print(i,str[x])
#     x+=1

# str1="DATA"
# y="HELLO"
# for i in str1:
#     print(f"{i}-{y}")


# list1=[4,6,8,2,3,1,8,9]
# for i in list1:
#     print(f"square of {i} is {i**2}")

# list1=['shiva','karthik','karun','tejaswini','yamini','deepak','satwik']
# for i in list1:
#     print(f"{i} length is {len(i)}")

# list1=[3,5,7,8,2,4,6,10]
# x=0
# # x=len(list1)-len(list1)
# for i in list1:
#     print(i*x)
#     x+=1

# str1="BANANA"
# dict1={}
# for x in str1:
#     if x in dict1:
#         dict1[x]+=1
#     else:
#         dict1[x]=1
# print(dict1)

# list1=['apple','banana','SOME','hello','WELCOME','oops']
# op=[]
# for i in list1:
#     if i==i.lower():
#         # print(i.upper())
#         op+=[i.upper()]
#     else:
#         # print(i.lower())
#         op+=[i.lower()]
# print(op)

# s1='soMetHINg'
# op=''
# for i in s1:
#     if i==i.lower():
#         op+=i.upper()
#     else:
#         op+=i.lower()
# print(op)
        
# x=int(input("enter the number : "))
# fact=1
# for i in range(1,x+1):
#     fact*=i
# print(fact)


ecommerce_data = [
    {
        "order_id": "O1001",
        "customer_name": "Ravi Kumar",
        "city": "Hyderabad",
        "product": "Wireless Mouse",
        "category": "Electronics",
        "price": 799,
        "quantity": 2,
        "total_amount": 1598,
        "payment_method": "UPI",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1002",
        "customer_name": "Sneha Reddy",
        "city": "Bangalore",
        "product": "Bluetooth Headphones",
        "category": "Electronics",
        "price": 1999,
        "quantity": 1,
        "total_amount": 1999,
        "payment_method": "Credit Card",
        "order_status": "Shipped"
    },
    {
        "order_id": "O1003",
        "customer_name": "Arjun Singh",
        "city": "Mumbai",
        "product": "Running Shoes",
        "category": "Fashion",
        "price": 2499,
        "quantity": 1,
        "total_amount": 2499,
        "payment_method": "Cash on Delivery",
        "order_status": "Processing"
    },
    {
        "order_id": "O1004",
        "customer_name": "Priya Sharma",
        "city": "Delhi",
        "product": "Smart Watch",
        "category": "Electronics",
        "price": 3499,
        "quantity": 1,
        "total_amount": 3499,
        "payment_method": "Debit Card",
        "order_status": "Delivered"
    },
    {
        "order_id": "O1005",
        "customer_name": "Kiran Patel",
        "city": "Chennai",
        "product": "Laptop Backpack",
        "category": "Accessories",
        "price": 1299,
        "quantity": 3,
        "total_amount": 3897,
        "payment_method": "UPI",
        "order_status": "Shipped"
    }
]
for x in ecommerce_data:
    if x["payment_method"] == "UPI":
        print(x["customer_name"])
    if x["quantity"]>1:
        print(x["customer_name"]) 
    if x["category"]!="Electronics":
        print(x["customer_name"])  


    

   
    
    
   
