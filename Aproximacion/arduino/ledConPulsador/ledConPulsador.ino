//Declaramos el pin al que estrá conectado el pulsador
int pinPulsador = 4;
//Declaramos el pin al que estará conectado el led
int pinLed = 2;

void setup() {

  //Determinamos que el pin del pulsador será para recibir
  pinMode(pinPulsador, INPUT);
  //Declaramos que el pin del led será para seguir
  pinMode(pinLed, OUTPUT);

}

void loop(){

  //Si la señal del pulsador es activa, encendemos el led
  if(digitalRead(pinPulsador) == HIGH){
    digitalWrite(pinLed, HIGH);
  }

  //De lo contrario apagamos el led
  else{
    digitalWrite(pinLed, LOW);
  }
  delay(10);
}
