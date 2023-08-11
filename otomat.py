import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#keypad pinlerini ayarla
ROW=[5, 13, 6, 19]
COL=[21, 20, 16, 12]

#giriş pinlerini ayarla
for pin in ROW:
    
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#output pinlerini ayarla
for pin in COL:
    GPIO.setup(pin,GPIO.OUT)
#keypad matrix'ini oluştur.
KEYS= [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
    ]
#motor pinlerini ayarla
motor1_pin = 17
motor2_pin = 22
motor3_pin = 27
#gecikme
DELAY= 0.1
#keypad fonksiyonunu oluştur.
def get_key():
    #columnları output low olarak ayarlamak
    for pin in COL:
        GPIO.output(pin, GPIO.LOW)
     #columnları output high olarak ayarlamak
    for j in range(len(COL)):
        GPIO.output(COL[j], GPIO.HIGH)
        
        #row pinini okumak
        for i in range(len(ROW)):
            if GPIO.input(ROW[i]) == 0:
                #butona  basıldı
                #butonu bırakmayı beklemek
                while GPIO.input(ROW[i]) == 0:
                    time.sleep(DELAY)
                #fonksiyon sonucunu dışa döndür
                return KEYS[i][j]
        #column low
        GPIO.output(COL[j], GPIO.LOW)
    #hiçbir butona basılmadığında none
    return None

# GPIO pinlerini output olarak ayarla

GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)
GPIO.setup(motor3_pin, GPIO.OUT)
#motor çalıştırma fonksiyonu
def start_motor(motor_pin):

  GPIO.output(motor_pin, GPIO.HIGH)
 # motor durdurma fonksiyonu  
def stop_motor(motor_pin):
 
  GPIO.output(motor_pin, GPIO.LOW)

#motoru basılan butona göre ayarla        
def run_motor_based_on_key(key):
    if key in KEYS[0]:
        motor_pin=motor1_pin
        start_motor(motor_pin)
        time.sleep(0.7)
        stop_motor(motor_pin)
    elif key in KEYS[1]:
        motor_pin=motor2_pin
        start_motor(motor_pin)
        time.sleep(0.7)
        stop_motor(motor_pin)
    elif key in KEYS[2]:
        motor_pin=motor3_pin
        start_motor(motor_pin)
        time.sleep(0.7)
        stop_motor(motor_pin)
    else:
        motor_pin=motor3_pin
    stop_motor(motor_pin)
#ana döngü
while True:
    key=get_key()
    if key:
        print(f'Key pressed:{key}')
        run_motor_based_on_key(key)
