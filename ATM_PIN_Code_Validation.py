# ATM PIN Code Validation

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot 
# contain anything but exactly 4 digits or exactly 6 digits. 
# Your task is to create a function that takes a string and 
# returns True if the PIN is valid and False if it's not.



# Examples

# is_valid_PIN("1234") ➞ True

# is_valid_PIN("12345") ➞ False

# is_valid_PIN("a234") ➞ False

# is_valid_PIN("") ➞ False


def is_valid_PIN(pin):
    if len(pin)== 4 or len(pin)== 6 :
        return True
    else:
        return False
print(is_valid_PIN("12344"))





def is_valid_PIN(pin):
    # Check if the length is either 4 or 6
    if len(pin) not in [4, 6]:
        return False
    
    # Check if all characters are digits
    if not pin.isdigit():
        return False
    
    return True

# Examples
print(is_valid_PIN("1234"))   # Output: True
print(is_valid_PIN("12345"))  # Output: False
print(is_valid_PIN("a234"))   # Output: False
print(is_valid_PIN(""))      # Output: False
