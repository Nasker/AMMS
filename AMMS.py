'''
    AtomicMokhtar'sMotorServer v0.1
'''
from LinearMotorControl import LinearMotorControl
from flask import Flask, render_template, request

amms = Flask(__name__)

enablePin = 17
directionPin = 27
pulsesPin = 22
    
motorControl = LinearMotorControl(enablePin, directionPin, pulsesPin)
    

@amms.route("/")
def index():
    # Read Sensors Status
    currenPosition = motorControl.getCurrentPosition()
    templateData = {
              'title' : 'Linear Motor Position!',
              'currentPosition'  : currenPosition,
        }
    return render_template('index.html', **templateData)
    
@amms.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'move':
        actuator = motorControl
    if action == 'plusOneMM':
        motorControl.move(1)
    if action == "lessOneMM":
        motorControl.move(-1)
    if action == 'plusTenMM':
        motorControl.move(10)
    if action == "lessTenMM":
        motorControl.move(-10)
    if action == "gotoZero":
        motorControl.moveTo(0)
    if action == "setZero":
        motorControl.setZero()
             
    currentPosition = motorControl.getCurrentPosition()
   
    templateData = {
              'currentPosition'  : currentPosition,
        }
    return render_template('index.html', **templateData)
if __name__ == "__main__":
   amms.run(host='0.0.0.0', port=5000, debug=True)