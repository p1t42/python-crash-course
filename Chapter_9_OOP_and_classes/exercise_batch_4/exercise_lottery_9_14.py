# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 
# numbers or letters from the list and print a message saying that any ticket matching these 4 numbers 
# or letters wins a prize.

from random import sample


class Ticket:
    """Represents a lottery ticket with a random selection of characters."""
    
    def __init__(self):
        """Initialize the ticket with the pool of available characters."""
        self.random_characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
        
    def create_ticket(self):
        """Randomly select 4 characters from the pool to create a ticket."""
        return sample(self.random_characters, 4)



class Lottery:
    """Represents the lottery drawing that generates the winning combination."""
    
    def __init__(self):
        """Initialize the lottery with the pool of available characters."""
        self.random_lottery_characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
        
    def create_lottery(self):
        """Randomly select 4 characters from the pool to create the winning combination."""
        return sample(self.random_lottery_characters, 4)
        
    

today_lottery = Lottery()
today_ticket = Ticket()

winning_ticket = today_lottery.create_lottery()
print(f"\nAny Ticket matching this will win a prize: {winning_ticket}")

count = 0
my_ticket = today_ticket.create_ticket()
while my_ticket != winning_ticket:
    my_ticket = today_ticket.create_ticket()
    count += 1

print(f"Your winning ticket is: {my_ticket}")
print(f"It took {count} attempts to match the winning ticket.")


