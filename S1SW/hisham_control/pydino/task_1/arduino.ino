const int LEDPin = 2; 

void setup() {
  Serial.begin(9600);
  pinMode(LEDPin,OUTPUT);

}

void loop() {
  if(Serial.available() > 0){
    String msg = Serial.readString();
    if(msg == "ON"){
      digitalWrite(LEDPin,HIGH);
      }
    else if(msg == "OFF"){
      digitalWrite(LEDPin,LOW);
      }
    }
}
