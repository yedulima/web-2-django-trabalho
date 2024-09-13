def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    # Testes
    print(is_number("2532.5")) # T
    print(is_number("345e24")) # T
    print(is_number("5432dasd52")) # F
    print(is_number("0")) # T
    print(is_number("-0")) # T
    print(is_number("-")) # F
    print(is_number("-53423.64")) # T
    print(is_number("e")) # F
    print(is_number("Eduardo")) # F