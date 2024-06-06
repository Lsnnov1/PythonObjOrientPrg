"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
   
        
    # init self and starting arg
    def __init__(self, start):
        self.start = start

    def __repr__(self):
        return f"<Start = {self.start} incrementing by 1>"
    
    def generate(self):
        """increment by 1"""
        self.start += 1
        return self.start
    
    def reset(self):
        """reset count"""
        self.start = 100
        return self.start
    
serial = SerialGenerator(100)
#  OR (START=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.reset())
print(serial.generate())
print(serial.generate())

