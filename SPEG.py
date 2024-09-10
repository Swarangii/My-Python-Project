import random

class PyPasswordGenerator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate_password(self, nr_letters, nr_symbols, nr_numbers):
        password = []

        # Add letters
        password += [random.choice(self.letters) for _ in range(nr_letters)]

        # Add symbols
        password += [random.choice(self.symbols) for _ in range(nr_symbols)]

        # Add numbers
        password += [random.choice(self.numbers) for _ in range(nr_numbers)]

        # Shuffle the list to randomize the order
        random.shuffle(password)

        # Convert list to string
        return ''.join(password)


class PyPasswordApp:
    def __init__(self):
        self.generator = PyPasswordGenerator()

    def get_user_input(self):
        print("Welcome to the Secure Password Enforceable Generator (SPEG) !!")
        
        while True:
            nr_letters = self.get_valid_input("How many letters would you like in your password?\n")
            nr_symbols = self.get_valid_input("How many symbols would you like?\n")
            nr_numbers = self.get_valid_input("How many numbers would you like?\n")
            
            total_length = nr_letters + nr_symbols + nr_numbers

            # Check if the total length is within the allowed range
            if 12 <= total_length <= 20:
                return nr_letters, nr_symbols, nr_numbers
            else:
                print("The total length of the password must be between 6 and 20 characters.")
                print(f"Your current total is: {total_length}. Please try again.\n")

    def get_valid_input(self, prompt):
        while True:
            try:
                value = input(prompt)
                if value.strip() == "":  # Check if the input is empty
                    raise ValueError("Input cannot be empty.")
                value = int(value)  # Try to convert the input to an integer
                if value < 0:  # Ensure the number is non-negative
                    raise ValueError("Number cannot be negative.")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")

    def run(self):
        nr_letters, nr_symbols, nr_numbers = self.get_user_input()
        password = self.generator.generate_password(nr_letters, nr_symbols, nr_numbers)
        print(f"Your password is: {password}")


# Create the app and run it
if __name__ == "__main__":
    app = PyPasswordApp()
    app.run()
