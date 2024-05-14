weight = 1.5
method = 'Drone'

if method == 'Normal Ground':
  # Ground Shipping
  if weight <= 2:
    cost = weight * 1.5 + 20
  elif weight <= 6:
    cost = weight * 3 + 20
  elif weight <= 10:
    cost = weight * 4 + 20
  elif weight > 10 :
    cost = weight * 4.75 + 20
elif method == 'Premium Ground':
  # Premium Ground Shipping
  cost = 125
elif method == 'Drone':
  # Drone Shipping
  if weight <= 2:
    cost = weight * 4.5
  elif weight <= 6:
    cost = weight * 9
  elif weight <= 10:
    cost = weight * 12
  elif weight > 10 :
    cost = weight * 14.25

print(f'You selected the {method} Shipping method, and needs to pay ${cost:.2f}')


# Drone Shipping