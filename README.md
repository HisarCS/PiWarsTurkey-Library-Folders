# PiWars Turkey 2019: Python library for the distributed robot kits by HisarCS

This python library was created for the purposes of easing the understanding between software, sensors, and movables on the robot kits designed by HisarCS for attendees of Pi Wars Turkey 2019.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PiWarsTurkiyeRobotKiti2019.

```bash 
sudo pip install PiWarsTurkiyeRobotKiti2019
```

Alternatively, its possible to install from Github.
```bash 
git clone https://github.com/HisarCS/PiWarsTurkey-Library-Folders.git
cd PiWarsTurkey-Library-Folders
sudo python setup.py install
```

## Usage

```python
import PiWarsTurkiyeRobotKiti2019
```
##Documentation

The library includes 5 classes as of now these are:
- HizlandirilmisPiKamera (for a simplified and fast way to use the Pi Camera and opencv)
- Kumanda (for an easy way to use the pygame Joystick class with the sixaxis PS3 controller)
- MotorKontrol (for an easy way to use the Pololu DRV8835 motor control circuit for the Raspberry Pi with a controller)
- ServoKontrol (for a simple way to use servo motors on the Raspberry Pi using GPIO pins)
- UltrasonikSensoru (for an easy way to use HC-SR04 ultrasonic distance sensors on the Raspberry Pi)

HizlandirilmisPiKamera:
-
- Methods -
```python
veriGuncelle()
```
Updates the data obtained from the Pi Camera.

```python
veriOkumayaBasla()
```
Creates a new Thread to call ```python veriGuncelle()``` in order to update the data without slowing down the main thread.

```python
veriOku()
```
Returns the current data of the camera as a numPy array.

```python
kareyiGostermeyiGuncelle()
```
Creates and updates the opencv window that shows the image the Pi Camera is seeing. The "q" key can be used to close the window.

```python
kareyiGoster()
```
Calls ```python kareyiGostermeyiGuncelle()``` in a new Thread to create a visual window without slowing down the main thread.

- Example Usage -
```python
import piwarsturkiyerobotkiti2019

camera = piwarsturkiyerobotkiti2019.HizlandirilmisPiKamera()
camera.veriOkumayaBasla()
camera.kareyiGoster()
```
The above example creates a new HizlandirilmisPiKamera object and uses it to show the image the camera is seeing until the "q" key is pressed. Keep in mind that the data has to be received using either ```python camera.veriOkumayaBasla()```or ```python camera.veriGuncelle()``` , depending on if you want to use it on the main thread or a separate thread, in order for it to be shown on a window.

Kumanda
-
- Methods -
```python
yenile()
```
Refreshes the values obtained from the controller inside a while loop.

```python
dinlemeyeBasla()
```
Calls ```python yenile()``` on another Thread. If ```python yenile()``` is called on the main thread, the code will be stuck on the while loop inside the function. This is not recommended.

```python
solVerileriOku()
```
Returns the values of the left joystick of the controller as two float values, x and y.

```python
sagVerileriOku()
```
Returns the values of the right joystick of the controller as two float values, x and y.

```python
butonlariOku()
```
Returns an array of the numerical values of all the buttons pressed.

```python
verileriOku()
```
Returns all values of the controller (```python solVerileriOku()```, ```python sagVerileriOku()```, ```python butonlariOku()```)

- Example Usage -
```python
controller = piwarsturkiyerobotkiti2019.Kumanda()
controller.dinlemeyeBasla()

while True:
  lx, ly = controller.solVerileriOku()
  rx, ry = controller.sagVerileriOku()
  buttons = controller.butonlariOku()
  
  print("The left joystick values are: ", lx, ly)
  print("The right joystick values are: ", rx, ry)
  
  if(0 in buttons):
    print("Button 0 was pressed!")
```
The above code initializes a Kumanda object and prints the values from the left and right joysticks, as well as a set string when a button is pressed. Keep in mind that ```python dinlemeyeBasla()``` has to be called or else the data won't be read from the controller.

MotorKontrol
-
- Methods -
```python
hizlariAyarla(rightSpeed, leftSpeed)
```
Sets the speeds of the motors using the pololu-drv8835-rpi library. The range for the speeds are -480 to 480 where -480 is maximum speed in reverse. The right and left speeds are for motor 1 and motor 2 depending on which side they are on.

```python
kumandaVerisiniMotorVerilerineCevirme(x, y, t)
```
Returns the speed for the motor according to the values of a joystick from the controller. x and y are the x and y values of the joystick and t is a boolean value with True for the right motor and False for the left motor.

- Example Usage -
```python
motors = piwarsturkiyerobotkiti2019.MotorKontrol()

while True:
  motors.hizlariAyarla(480, 480)
```
This code initializes motors and sets both of them to max speed.

- Example Usage w/ Controller -
```python
motors = piwarsturkiyerobotkiti2019.MotorKontrol()

controller = piwarsturkiyerobotkiti2019.Kumanda()
controller.dinlemeyeBasla()

while True:
  lx, ly = controller.solVerileriOku()
  rightSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx, -ly, True)
  leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx, -ly, False)
  
  motors.hizlariAyarla(rightSpeed, leftSpeed)
```
The above code initializes the motors and the controller and goes into a while loop. Inside the loop, the ```python kumandaVerisiniMotorVerilerineCevirme()```function is used to get the speed values for the motors. The y value is set to negative because on PS3 controllers sepicifically forwards on the joystick returns negative values. 

ServoKontrol
-
- Methods -
```python
surekliDonmeyeAyarla()
tekDonmeyeAyarla()
```
Switches the servo from continous and not continuous respectively. Continuous requires constant values to be provided while not continuous turns the servo between provided angles.

```python
aciAyarla(angle)
```
Turns the servo to the provided angle in degrees. Provides a sleep statement and a separate thread when the servo is set to not continuous. 

- Example Usage -
Continuous:
```python
servo = piwarsturkiyerobotkiti2019.ServoKontrol()
servo.surekliDonmeyeAyarla()

angle = 0
add = 0
while True:
  servo.aciAyarla(angle)
  
  if(angle == 180):
    add = -1
  elif(angle == 0):
    add = 1
  angle += add
```
In this case, the servo is set to continuous. A while loop is used to constantly change the angle of the servo by 1 and set the new angle.

UltrasonikSensoru
-
- Methods -
```python
mesafeOlc()
```
Returns the distance measured by the ultrasonic sensor

- Example Usage -
```python
ultra = piwarsturkiyerobotkiti2019.UltrasonikSensoru(38, 40)

while True:
  print(ultra.mesafeOlc())
```
The code above prints the distance. The integers inside the initializer for the class are the pins it is attached to.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
