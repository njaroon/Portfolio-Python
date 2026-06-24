import sys

def main():
    print("Welcome to the NYC Fare Card Calculator\n")
    
    # 1. Base fare matrix stored as floating-point numbers
    # (0.0 represents free transit, like the Staten Island Ferry)
    fare_matrix = {
        "Staten Island": {
            "Staten Island": 0.00,
            "Brooklyn": 1.50,
            "Long Island": 3.00,
            "Manhattan": 2.50,
            "Queens": 2.50,
            "PATH": 3.00,
            "Bronx": 3.00
        },
        "Brooklyn": {
            "Staten Island": 2.50,
            "Brooklyn": 0.00,
            "Long Island": 3.00,
            "Manhattan": 2.50,
            "Queens": 2.50,
            "PATH": 2.90,
            "Bronx": 2.50
        },
        "Long Island": {
            "Staten Island": 3.00,
            "Brooklyn": 3.00,
            "Long Island": 0.00,
            "Manhattan": 5.00,
            "Queens": 4.00,
            "PATH": 5.50,
            "Bronx": 4.50
        },
        "Manhattan": {
            "Staten Island": 2.50,
            "Brooklyn": 2.50,
            "Long Island": 5.00,
            "Manhattan": 0.00,
            "Queens": 2.50,
            "PATH": 2.90,
            "Bronx": 2.50
        },
        "Bronx": {
            "Staten Island": 3.00,
            "Brooklyn": 2.50,
            "Long Island": 4.50,
            "Manhattan": 2.50,
            "Queens": 2.50,
            "PATH": 3.50,
            "Bronx": 0.00
        },
        "Queens": {
            "Staten Island": 2.50,
            "Brooklyn": 2.50,
            "Long Island": 4.00,
            "Manhattan": 2.50,
            "Queens": 0.00,
            "PATH": 3.50,
            "Bronx": 2.50
        },
        "PATH": {
            "Staten Island": 3.00,
            "Brooklyn": 2.90,
            "Long Island": 5.50,
            "Manhattan": 2.90,
            "Queens": 3.50,
            "PATH": 0.00,
            "Bronx": 3.50
        }
    }
    
    # 2. Get and validate starting point
    while True:
        starting_point = input("Please Enter Your Starting Point: ").strip()
        if starting_point in fare_matrix:
            print(f"Starting Point is {starting_point}.\n")
            break
        else:
            print("Invalid Start Point. Try Again.\n")

    # 3. Get and validate final destination
    while True:
        final_destination = input("Please Enter Your Final Destination: ").strip()
        if final_destination in fare_matrix:
            print(f"Final Destination is {final_destination}.\n")
            break
        else:
            print("Invalid Destination. Try Again.\n")

    # 4. Get and validate discount status
    has_discount = False
    while True:
        discount_input = input("Are you eligible for a reduced/discounted fare? (yes/no): ").strip().lower()
        if discount_input in ['yes', 'y']:
            has_discount = True
            break
        elif discount_input in ['no', 'n']:
            has_discount = False
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.\n")

    # 5. Extract base fare
    base_fare = fare_matrix[starting_point][final_destination]
    
    # 6. Apply discount calculation (e.g., standard MTA Reduced-Fare is 50% off)
    if has_discount:
        final_fare = base_fare * 0.50
    else:
        final_fare = base_fare

    # 7. Print final formatted result
    if final_fare == 0.0:
        print("\nResult: Free")
    else:
        # :.2f forces Python to always print 2 decimal places (e.g., $1.50 instead of $1.5)
        print(f"\nResult: Ticket Price is ${final_fare:.2f}")

if __name__ == "__main__":
    main()
