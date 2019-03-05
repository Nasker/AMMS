from StepperControl import StepperControl

class LinearMotorControl:    
    "VIP's Linear Motor Stepper Control With suposed-Absolute Position API"
    
    def __init__(self, driverPinEnable, driverPinDirection, driverPinPulse):
        self.stepper = StepperControl(driverPinEnable, driverPinDirection, driverPinPulse)
        self.currentPosition = 0
    
    def move(self, position):
        self.currentPosition += position 
        self.stepper.move(position)
    
    def moveTo(self, position):
        nextPosition = position - self.currentPosition
        self.stepper.move(nextPosition)
        self.currentPosition = position
    
    def getCurrentPosition(self):
        return self.currentPosition
    
    def setZero(self):
        self.currentPosition = 0

if __name__ == '__main__':      
    enablePin = 17
    directionPin = 27
    pulsesPin = 22    
    moveMotor = LinearMotorControl(enablePin, directionPin, pulsesPin)
    
    print "Welcome to the almost-manual VIP's Linear Motor Control!\n"  
    cmd = 0
    
    while (cmd!='q'):
        cmd = raw_input("Type position in mm (+ goes up, - down) or 'q' to quit:")
        if (cmd != 'q'):
            try:
                int(cmd)
            except ValueError:
                print "Not a number, try again, is not that difficult!\n"
            else:
                position = int(cmd)
                moveMotor.moveTo(position)
            
    print("\nBye Hohe!") 