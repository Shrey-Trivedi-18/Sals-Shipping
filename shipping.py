# Ground Shipping

weight = 4.8
cost = ""

if weight <= 2:
    cost = 1.5 * weight + 20
elif weight > 2 and weight <= 6:
    cost = 3 * weight + 20
elif weight > 6 and weight <= 10:
    cost = 4 * weight + 20
elif weight > 10:
    cost = 4.75 * weight + 20

print("Ground Shipping cost $:", cost)

# Ground Shipping Premium

cost_premium_ground_shipping = 125
print("Ground Shipping Premium $:", cost_premium_ground_shipping)

# Drone Shipping

if weight <= 2:
    cost = 4.5 * weight
elif weight > 2 and weight <= 6:
    cost = 9 * weight
elif weight > 6 and weight <= 10:
    cost = 12 * weight
elif weight > 10:
    cost = 14.25 * weight

print("Drone Shipping cost $:", cost)
