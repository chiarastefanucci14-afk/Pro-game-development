class Car():
    brand= "Lamborghini"
    speed= 2
    def accelerate(self):
        self.speed+= 10
car= Car()
car.accelerate()
print (car.speed)
car.accelerate()
print (car.speed)