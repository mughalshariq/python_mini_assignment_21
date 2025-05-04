class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example usage
log = Logger()

# You can force destruction like this (for demonstration purposes):
del log
