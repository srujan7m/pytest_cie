from vehicle import vehicle_details
def test_vehicle_details():
    expected_output = (
        "Vehicle Number:KA27EM1234\n"
        "Owner name: Srujan Mattur\n"
        "Vehicle Type: Bike\n"
        "Year of Manufacture: 2018"
    )
    assert vehicle_details("KA27EM1234", "Srujan Mattur", "Bike", 2018) == expected_output