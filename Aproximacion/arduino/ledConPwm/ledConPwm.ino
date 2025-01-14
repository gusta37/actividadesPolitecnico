//int LEDpin = 11;   // for Arduino microcontroller
//int LEDpin = D4;   // for ESP8266 microcontroller
int LEDpin = 2;   // for ESP32 microcontroller

int bright = 0;    // initial value of LED brightness
int incremt = 5;   // incremental change in PWM frequency
int frecuency = 100;    // time period the PWM frequency is changing

void setup()
  {
    pinMode(LEDpin, OUTPUT);  // define the LEDpin as output pin
  }

void loop()
  {
    analogWrite(LEDpin, bright);  // set LED brightness as PWM signal
    delay(frecuency);                  // wait for a time period
    bright = bright + incremt;    // increment LED brightness
    // if the brightness is out of range, reduce brightness
    if (bright <=0 || bright >=255) incremt = - incremt;
  }
