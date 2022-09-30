#include <SoftwareSerial.h>
SoftwareSerial mySerial(10,11);// RX TX

int ldr=A0;//Set A0(Analog Input) for LDR.
unsigned int value;

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  pinMode(3,OUTPUT);
}

void loop() {
  value=analogRead(ldr);
  Serial.println(value);
  mySerial.println(value);
  delay(200);
