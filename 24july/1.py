price_per_litre = 70
mileage= 10
price_per_ticket = 80
km = int(input())
passenger = int(input())

cost = (km/mileage)*price_per_litre
ticket_cost = passenger*price_per_ticket
if  ticket_cost - cost > 0:
    print(ticket_cost - cost)
else:
    print(-1)