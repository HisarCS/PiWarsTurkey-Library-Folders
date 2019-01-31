
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
## Documentation

The library includes 5 classes as of now these are:
- HizlandirilmisPiKamera (for a simplified and optimized way to use the Pi Camera and OpenCV)
- Kumanda (for an easy way to use the pygame Joystick class with the sixaxis PS3 controller)
- MotorKontrol (for an easy way to use the Pololu DRV8835 motor control circuit for the Raspberry Pi with a controller)
- ServoKontrol (for a simple way to use servo motors on the Raspberry Pi using GPIO pins)
- UltrasonikSensoru (for an easy way to use HC-SR04 ultrasonic distance sensors on the Raspberry Pi)

For the purposes of performance, some of the classes include multithtreading. This prevents some parts of the code to not have an effect on other parts of the code. Multithreading was especially implemented to HizlandirilmisPiKamera(for both grabbing and showing the frames), Kumanda(to get the controller values continuously), ServoKontrol(to prevent any sleep function in the class to affect the main thread).

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
Creates a new Thread to call ``` veriGuncelle()``` in order to update the data without slowing down the main thread.

```python
veriOku()
```
Returns the current data of the camera as a numpy array.

```python
kareyiGostermeyiGuncelle()
```
Creates and updates the opencv window that shows the image the Pi Camera is seeing. The "q" key can be used to close the window.

```python
kareyiGoster()
```
Calls ``` kareyiGostermeyiGuncelle()``` in a new Thread to create a visual window without slowing down the main thread.

- Example Usage -
```python
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera

camera = HizlandirilmisPiKamera()
camera.veriOkumayaBasla()
camera.kareyiGoster()
```
The above example creates a new HizlandirilmisPiKamera object and uses it to show the image the camera is seeing until the "q" key is pressed.  

The default resolution of 640x480 for camera is set when the constructor is called. If you want a different resolution settings, for instance 1280x720 ,then set the camera object as follows:
 ``` camera = HizlandirilmisPiKamera(cozunurluk=(1280, 720))```

Keep in mind that the data has to be received using  ``` camera.veriOkumayaBasla()``` with ``` camera.veriOku()```  or  ``` camera.suAnkiKare``` , if further vision processing is wanted. ``` camera.suAnkiKare``` is the current frame variable in numpy array, where the function ``` camera.veriOku()```  returns variable ``` camera.suAnkiKare```. 

The below example code will grab the frame from the camera in numpy array format, grayscale it, and display the frames in the **main thread**.
```python
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
import cv2

camera = HizlandirilmisPiKamera()
camera.veriOkumayaBasla()

while True:
	frame = camera.veriOku()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("gray", gray)
```
Wheras in the example below, the grayscaled frames are both grabbed and displayed in **different threads**, **not in the main thread**. This method is strongly encouraged to increase the performance as much as possible.
```python
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
import cv2

camera = HizlandirilmisPiKamera()
camera.veriOkumayaBasla()
camera.kareyiGoster()

while True:
	frame = camera.suAnkiKare
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	camera.suAnkiKare = gray
```
Kumanda
-
- Methods -
```python
yenile()
```
Refreshes the values obtained from the controller inside a while loop. **Not recommended** to call in the main thread since the program will stuck in this method.

```python
dinlemeyeBasla()
```
Calls ```python yenile()``` in a new thread. Allowing the while loop of the main thread to be faster. 

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
Returns all values of the controller ```(python solVerileriOku(), python sagVerileriOku(), python butonlariOku())```

- Example Usage -
```python
import PiWarsTurkiyeRobotKiti2019

controller = PiWarsTurkiyeRobotKiti2019.Kumanda()
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
The above code initializes a Kumanda object and prints the values from the left and right joysticks, as well as a set string when a button is pressed. Keep in mind that ```python dinlemeyeBasla()``` has to be called once when the main code is executed, or the data won't be read from the controller.

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
import PiWarsTurkiyeRobotKiti2019
motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol()

while True:
  motors.hizlariAyarla(480, 480)
```
This code initializes motors and sets both of them to max speed.

- Example Usage w/ Controller -
```python
import PiWarsTurkiyeRobotKiti2019

motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol()

controller = PiWarsTurkiyeRobotKiti2019.Kumanda()
controller.dinlemeyeBasla()

while True:
  lx, ly = controller.solVerileriOku()
  rightSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx, -ly, True)
  leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx, -ly, False)
  
  motors.hizlariAyarla(rightSpeed, leftSpeed)
```
The above code initializes the motors and the controller and goes into a while loop. Inside the loop, the ```kumandaVerisiniMotorVerilerineCevirme()```function is used to get the speed values for the motors. The y value is set to negative because on PS3 controllers sepicifically forwards on the joystick returns negative values. 

ServoKontrol
-
- Methods -
```python
surekliDonmeyeAyarla()
tekDonmeyeAyarla()
```
Switches the servo from continous and not continuous respectively. Continuous requires dynamic values to be provided while not continuous turns the servo between provided angles.

```python
aciAyarla(angle)
```
Turns the servo to the provided angle in degrees. Provides a sleep statement and a separate thread when the servo is set to not continuous. 

- Example Usage -
Continuous:
```python
servo = PiWarsTurkiyeRobotKiti2019.ServoKontrol()
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
  sleep(0.01)
```
In this case, the servo is set to continuous. A while loop is used to constantly change the angle of the servo by 1 and set the new angle.

- Example Usage -
Non-Continuous:
```python
import PiWarsTurkiyeRobotKiti2019
from time import sleep

servo = PiWarsTurkiyeRobotKiti2019.ServoKontrol()
servo.tekDonmeyeAyarla()

while True:
  servo.aciAyarla(180)
  sleep(1)
  servo.aciAyarla(0)
  sleep(1)
```
In this case, the servo is set to non-continuous. A while loop is used to set the angle of servo with one minute sleeps

UltrasonikSensoru
-
- Methods 
```python
mesafeOlc()
```
Returns the distance measured by the ultrasonic sensor

- Example Usage
```python
ultra = PiWarsTurkiyeRobotKiti2019.UltrasonikSensoru(38, 40)

while True:
  print(ultra.mesafeOlc())
```
The code above prints the distance. The integers inside the initializer for the class are the pins it is attached to.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
##

## PiWars Türkiye 2019: HisarCS tarafından dağıtılan robot kitleri için python kütüphanesi

Bu python kütüphanesi, PiWars Türkiye 2019 katılımcılarının HisarCS tarafınndan hazırlanan robot kitlerindeki yazılımı, sensörleri ve hareketli parçaları kullanmalarını kolaylaştırmak amacıyla yapılmıştır.


## Kurulum

PiWarsTurkiyeRobotKiti2019'u indirmek için [pip](https://pip.pypa.io/en/stable/) paketleme yöneticisini kullanın.

```bash 
sudo pip install PiWarsTurkiyeRobotKiti2019
```

Alternatif olarak Github'dan indirmek de mümkün.
```bash 
git clone https://github.com/HisarCS/PiWarsTurkey-Library-Folders.git
cd PiWarsTurkey-Library-Folders
sudo python setup.py install
```

## Kullanım

```python
import PiWarsTurkiyeRobotKiti2019
```
## Belgeleme

Şu anda bu kütüphane 5 sınıf bulundurmaktadır:
- HizlandirilmisPiKamera (Pi Kamera ve opencv kullanmayı basitleştirmek ve optimize etmek için)
- Kumanda (pygame'in Joystick sınıfını PS3 sixaxis kumandalar ile kullanmayı basitleştirmek için)
- MotorKontrol (Raspberry Pi için Pololu DRV8835 motor sürücü devresinin kullanımını kolaylaştırmak için)
- ServoKontrol (Raspberry Pi'ın GPIO pinleri ile servo kontrol etmeyi kolaylaştırmak için)
- UltrasonikSensoru (Raspberry Pi'ın GPIO pinleri ile HC-SR04 ultrasonik uzaklık sensörünü kullanmayı kolaylaştırmak için)

Performans sebeplerinden dolayı sınıfların bir kısmı multithreading kullanmaktadır. Bu yazılımın bir kısmının diğerlerinin performansını değiştirmesini engellemek içindir. Multithreading özellikle kullanıldığı sınıflar HizlandirilmisPiKamera (hem görüntüyü almak hem göstermek için), Kumanda (sürekli olarak kumanda değerlerini almak için) ve ServoKontrol (içindeki sleep fonksiyonlarının ana threadi durdurmasını engellemek için).

HizlandirilmisPiKamera:
-
- Metodlar
```python
veriGuncelle()
```
Pi Kameradan gelen verileri günceller.

```python
veriOkumayaBasla()
```
Ana threadi yavaşlatmadan veriyi güncellemek için yeni bir threadde ``` veriGuncelle()``` fonksiyonunu çağırır.

```python
veriOku()
```
numpy arrayi olarak kameranın o sıradaki değerlerini geri döndürür.

```python
kareyiGostermeyiGuncelle()
```
Pi Kamera'nın gördüklerini (sadece görenler için)  gösteren yeni bir opencv penceresi açar ve pencereyi günceller. "q" tuşu ile pencere kapatılabilir.

```python
kareyiGoster()
```
Ana threadi yavaşlatmadan görsel bir pencere açmak için  ``` kareyiGostermeyiGuncelle()``` fonksiyonunu başka bir threadde çağırır.

- Örnek Kullanım
```python
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera

camera = HizlandirilmisPiKamera()
camera.veriOkumayaBasla()
camera.kareyiGoster()
```
Yukarıdaki örnek yeni bir HizlandirilmisPiKamera objesi oluşturur ve onunla yeni bir görsel pencere oluşturur.

Kamera objesi çağırılınca varsayılan çözünürlük 640x480 dir. Eğer başka bir çözünürlük istiyorsanız, örneğin 1280x720, kamera objesini bu şekilde çağırabilirsiniz:  
 ``` camera = HizlandirilmisPiKamera(cozunurluk=(1280, 720))```

Aklınızda bulundurun ki eğer daha öte görsel işleme isteniyorsa veri ``` camera.veriOkumayaBasla()``` ve ``` camera.veriOku()``` veya ``` camera.suAnkiKare``` ile alınmalıdır. ``` camera.suAnkiKare``` o anki karenin numpy array temsili iken  ``` camera.veriOku()``` fonksiyonu ``` camera.suAnkiKare``` değişkenini verir.

Aşağıdaki örnek kod kameradan kareyi numpy array olarak alır, gri tonlama yapar ve kareyi **ana thread üzerinde** gösterir.
```python
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
import cv2

camera = HizlandirilmisPiKamera()
camera.veriOkumayaBasla()

while True:
	frame = camera.veriOku()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("gray", gray)
```
Buna karşılık aşağıdaki örnekte gri tonlanmış kareler **başka bir threadde** gösterilir, **ana threadde değil**. Bu kullanım performans arttırmak için tavsiye edilir. 
```python
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
import cv2

camera = HizlandirilmisPiKamera()
camera.veriOkumayaBasla()
camera.kareyiGoster()

while True:
	frame = camera.suAnkiKare
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	camera.suAnkiKare = gray
```
Kumanda
-
- Metodlar
```python
yenile()
```
Kumandadan alınan verileri bir while döngüsü içerisinde yeniler. Ana threadde çağırmak **tavsiye edilmez** çünkü program bu satırda takılacaktır.

```python
dinlemeyeBasla()
```
```python yenile()``` metodunu ayrı bir thread üzerinde çağırarak ana threadin kullanılabilmesini sağlar. 

```python
solVerileriOku()
```
Soldaki joystick değerlerini iki float değeri, x ve y, olarak verir.

```python
sagVerileriOku()
```
Sağdaki joystick değerlerini iki float değeri, x ve y, olarak verir.

```python
butonlariOku()
```
Basılan bütün düğmeleri sayı değeri olarak bir arrayde geri verir.

```python
verileriOku()
```
Kumandanın bütün değerlerini geri verir ```(python solVerileriOku(), python sagVerileriOku(), python butonlariOku())```

- Örnek Kullanım
```python
import PiWarsTurkiyeRobotKiti2019

controller = PiWarsTurkiyeRobotKiti2019.Kumanda()
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
Yukarıdaki kod bir Kumanda objesi oluşturur ve sol ve sağ joysticklerin değerlerini ekrana basarken aynı zamanda belirlenmiş bir stringi bir düğmeye basıldığında ekrana basar. ```python dinlemeyeBasla()```  metodunun veri alabilmek için ana kod başlatıldığında çağırılması gerektiğini unutmayınız.

MotorKontrol
-
- Metodlar
```python
hizlariAyarla(rightSpeed, leftSpeed)
```
 pololu-drv8835-rpi kütüphanesini kullanarak motorların hızını ayarlar. Hız -480den 480e kadar değerler olarak verilebilir (-480 geriye doğru tam hız olur). Sağ ve sol hız değerleri motor sürücüsünün birinci ve ikinci motorlarına denk gelir.

```python
kumandaVerisiniMotorVerilerineCevirme(x, y, t)
```
Motor hız değerlerini kumanda verisine dayanarak geri verir. x ve y, kumandanın joystick x ve y değerleri, t ise sağ motor için True, sol motor için False olan bir boolean değeridir. 

- Örnek Kullanım
```python
import PiWarsTurkiyeRobotKiti2019
motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol()

while True:
  motors.hizlariAyarla(480, 480)
```
Bu kod motorları başlatır ve ileri doğru tam hıza ayarlar.

- Kumanda ile Örnek Kullanım
```python
import PiWarsTurkiyeRobotKiti2019

motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol()

controller = PiWarsTurkiyeRobotKiti2019.Kumanda()
controller.dinlemeyeBasla()

while True:
  lx, ly = controller.solVerileriOku()
  rightSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx, -ly, True)
  leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx, -ly, False)
  
  motors.hizlariAyarla(rightSpeed, leftSpeed)
```
Yukarıdaki kod motorlar ve kumanda objelerini başlatır ve bir while döngüsünün içine girer. Döngüdeyken  ```kumandaVerisiniMotorVerilerineCevirme()``` metodu motorların hız değerlerini bulmak için kullanılır. y değerinin negatif olması, özellikle PS3 kumandalarında joystickteki ileri yönünün negatif değerler vermesinden dolayıdır.

ServoKontrol
-
- Metodlar
```python
surekliDonmeyeAyarla()
tekDonmeyeAyarla()
```
Servoyu sürekli dönme ve tek sefer dönmeye ayarlar. Sürekli dönme modu dinamik olarak değerler verilmesini gerektirirken tek dönme servoyu verilen açıya getirir.

```python
aciAyarla(angle)
```
Servoyu derece cinsinden verilen açıya çevirir. Servo tek dönmeye ayarlıyken sleep fonksiyonları ve ayrı bir thread oluşturur.

- Örnek Kullanım
Sürekli Dönme:
```python
servo = PiWarsTurkiyeRobotKiti2019.ServoKontrol()
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
  sleep(0.01)
```
Bu durumda servo sürekli dönmeye ayarlıdır. Bir while döngüsü servonun açısını 1er 1er arttırır ve servoyu yeni açıya getirir. 

Tek Dönme:
```python
import PiWarsTurkiyeRobotKiti2019
from time import sleep

servo = PiWarsTurkiyeRobotKiti2019.ServoKontrol()
servo.tekDonmeyeAyarla()

while True:
  servo.aciAyarla(180)
  sleep(1)
  servo.aciAyarla(0)
  sleep(1)
```
Bu durumda servo tek dönmeye ayarlıdır. Bir while döngüsü servonun açısını 1 saniye aralıklarla 180 ve 0 arasında değiştirir.

UltrasonikSensoru
-
- Metodlar
```python
mesafeOlc()
```
Ultrasonik sensörün ölçtüğü mesafeyi geri verir.

- Örnek Kullanım
```python
ultra = PiWarsTurkiyeRobotKiti2019.UltrasonikSensoru(38, 40)

while True:
  print(ultra.mesafeOlc())
```
Yukarıdaki kod ölçülen mesafeyi ekrana basar. Yapıcının içindeki değerler ultrasonik sensörün takıı olduğu pinlerdir.


## Katkıda Bulunma
Çekme istekleri kabul edilir. Büyük değişikler için lütfen önce bir issue açarak istediğiniz değişikliği anlatın.

Lütfen testleri uygun şekilde güncellediğinizden emin olun.

## Lisans
[MIT](https://choosealicense.com/licenses/mit/)
