import time


def validate_input(input):
    """Receives a user-given input. Returns True if input is a valid integer or decimal number."""
    try:
        float(input)
        if str(input)[::-1].find('.') <= 2:
            return True
        else:
            print("Error: Only 2 decimals places allowed")
            return False
    except ValueError:
        print("Error: Please enter an integer or decimal")
        return False


def call_microservice(value):
    """Takes a monetary value as a parameter. Calls the microservice and receives data via money-service.txt"""
    value = str(value)
    if validate_input(value) is True:
        print("valid input")
        txt_file = open("money-service.txt", 'w')
        txt_file.write(value)
        txt_file.close()
        time.sleep(3)
        txt_file = open("money-service.txt", 'r')
        content = txt_file.readline()
        print(content)
        return content
