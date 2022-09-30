#include <SoftwareSerial.h>
SoftwareSerial mySerial(0,1);// RX TX
void setup() {
  Serial.begin(9600);
//  mySerial.begin(9600);
}

void loop() {
//  static int index = 0;
//  static char Buffet[4];
  static int val1;
  
  if(mySerial.available()>=0){
    static int data = mySerial.read();
    val1 = atoi(data);
    Serial.println(data);
  }
}
