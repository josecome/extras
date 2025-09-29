# This is a basic decorator function
def hype(func):
    # The wrapper function adds behavior 
    # before and after the original function
    def wrapper():
        # Code before the original function
        print('Starting up...')
        # Call the original function
        func()
        # Code after the original function              
        print('Done!')      
        # Return the wrapper so it replaces
        # the original function     
    return wrapper  

# Apply the decorator using the @ symbol
@hype
def greet():
    # Original function content
    print('Y’all ready?')  

# Call the decorated function
greet()