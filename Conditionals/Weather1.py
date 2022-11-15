temperature = 45
forecast = "rain"

if temperature < 80 or forecast != "rain":
    print("Go Inside!")
else:
    print("Stay inside!")


if not forecast == "rain":
    print("Go Outside!")
else:
    print("Stay inside!")