class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        print(f"{self.engine_type} engine started")
    
    def stop(self):
        print(f"{self.engine_type} engine stopped")

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition: Car has-an Engine
    
    def start_car(self):
        print(f"Starting {self.model}")
        self.engine.start()  # Accessing Engine's method
    
    def stop_car(self):
        print(f"Stopping {self.model}")
        self.engine.stop()

# Create an Engine
v8_engine = Engine("V8")

# Create a Car with the Engine
mustang = Car("Ford Mustang", v8_engine)

# Use Car's methods which access Engine's methods
mustang.start_car()
mustang.stop_car()