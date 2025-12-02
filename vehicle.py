def vehicle_details(vehicle_number, owner_name, vehicle_type, yom):
    result = (
        f"Vehicle Number: {vehicle_number}\n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of Manufacture: {yom}"
    )
    return result

if __name__ == "__main__":
    print("Vehicle Details:",
          vehicle_details("KA27EM1234", "Srujan mattur", "Bike", 2018))
    