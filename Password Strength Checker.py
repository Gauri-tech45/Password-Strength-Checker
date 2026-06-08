while True:
    password = input("\nEnter a password (or type 'exit' to quit): ")

    if password.lower() == "exit":
        print("Program closed.")
        break

    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if has_upper:
        score += 1

    # Check digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if has_digit:
        score += 1

    # Check symbol
    has_symbol = False
    for char in password:
        if not char.isalnum():
            has_symbol = True
            break

    if has_symbol:
        score += 1

    print("\nPassword Analysis")
    print("Length:", len(password))
    print("Contains Uppercase:", has_upper)
    print("Contains Number:", has_digit)
    print("Contains Symbol:", has_symbol)

    if score <= 1:
        print("Strength: Weak")
        print("Validation Status: Failed")
        print("Recommendation: Add uppercase letters, numbers, symbols, and use at least 8 characters.")

    elif score <= 3:
        print("Strength: Medium")
        print("Validation Status: Passed")
        print("Recommendation: Password is acceptable, but can be made stronger.")

    else:
        print("Strength: Strong")
        print("Validation Status: Passed")
        print("Recommendation: Password meets basic security requirements.")