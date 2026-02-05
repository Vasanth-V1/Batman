def check_batarangs():
    stock = 5
    print(f"Batarang count: {stock}")
    assert stock > 0  # This will pass

def check_batmobile_fuel():
    fuel_level = 100
    print(f"Fuel level: {fuel_level}%")
    assert fuel_level > 10  # This will pass

if __name__ == "__main__":
    check_batarangs()
    check_batmobile_fuel()
    print("Bat-Computer: All systems are green!")
