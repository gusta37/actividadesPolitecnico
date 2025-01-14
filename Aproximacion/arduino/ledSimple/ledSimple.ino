//Declaramos el pin que encenderá
int pin_dos = 2;
//Iniciamos los pines de ESP2
void setup(){
  //Declaramos que el pin del led es de tipo salida, osea que la señal va a salir
  pinMode(pin_dos, OUTPUT);
}
//Iniciamos la función bucle que se repetira indefinidamente.
void loop(){
  //Endendemos eel led
  digitalWrite(pin_dos, HIGH);
  //Esperamos un segundo
  delay(4000);
  //Apagamos el led
  digitalWrite(pin_dos, LOW);
  //Esperamos un segundo
  delay(4000);
}
