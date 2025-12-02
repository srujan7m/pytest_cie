def vehicle_details(vehicle_number, owner_name, vehicle_type, yom):
    result = (
        f"Vehicle Number: {vehicle_number}\n"
        f"Owner name: {owner_name}\n"   # <-- lowercase n (matches test)
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of Manufacture: {yom}"
    )
    return result

if __name__ == "__main__":
    print("Vehicle Details:\n" +
          vehicle_details("KA27EM1234", "Srujan Mattur", "Bike", 2018))
