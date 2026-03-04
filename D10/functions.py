def movie_tickets(tickets, price):
    total_amount =  tickets * price
    if total_amount > 2000:
     return('coke and popcorn')
    elif total_amount > 1500:
     return('coke')
    else:
     return('You do not get anything for this amount. Thank you')


price = int(input("Enter price:"))
tickets = int(input("Enter no.of tickets:"))

print(movie_tickets(tickets, price))