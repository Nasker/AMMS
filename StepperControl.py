import RPi.GPIO as GPIO
from time import sleep

class StepperControl:
    "VIP's Linear Motor Stepper Control API"
    
    def __init__(self, driverPinEnable, driverPinDirection, driverPinPulse):
        self._driverPinEnable = driverPinEnable
        self._driverPinDirection = driverPinDirection
        self._driverPinPulse = driverPinPulse
        self._waitingTime = 0.001
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self._driverPinEnable, GPIO.OUT)
        GPIO.setup(self._driverPinDirection, GPIO.OUT)
        GPIO.setup(self._driverPinPulse, GPIO.OUT)
        GPIO.output(self._driverPinEnable, True);

    def __del__(self):
        GPIO.cleanup()
        

    def _enableDriver(self, isEnable):
        GPIO.output(self._driverPinEnable, isEnable);
     
    def _distanceToSteps(self,distanceInmm):
        steps = int((abs(distanceInmm)/4.0)*200.0)
        print("Steps to run: ",steps)
        return steps
    
    def _setDirection(self, isForward):
        GPIO.output(self._driverPinDirection, isForward)
        
    def _doStep(self):
        GPIO.output(self._driverPinPulse, 1)
        sleep(self._waitingTime * .5)
        GPIO.output(self._driverPinPulse, 0)
        sleep(self._waitingTime * .5)
 
    def _stepsMove(self, distance):
        """
        According to the pitch of the linear axis and settimg the motor into full step mode:
        ONE REVOLUTION TAKES 200 steps WICH WILL MOVE 4mm IN THE AXIS
        
        """
        self._enableDriver(False)  
        for i in range(self._distanceToSteps(distance)):
            #print (i)
            self._doStep()
        self._enableDriver(True)  

    def move(self,distance):
        self._setDirection(distance < 0)
        self._stepsMove(distance)
            
    def setWaitingTime(self,time):
        self._waitingTime = time
        
    
if __name__ == '__main__':      
    enablePin = 17
    directionPin = 27
    pulsesPin = 22    
    moveMotor = StepperControl(enablePin, directionPin, pulsesPin)
    
    print "Welcome to the almost-manual VIP's Linear Motor Control!\n"  
    cmd = 0
    
    while (cmd!='q'):
        cmd = raw_input("Type distance in mm (+ goes up, - down) or 'q' to quit:")
        if (cmd != 'q'):
            try:
                int(cmd)
            except ValueError:
                print "Not a number, try again, is not that difficult!\n"
            else:
                distanceToMove = int(cmd)
                moveMotor.move(distanceToMove)
            
    print("\nBye Hohe!")   