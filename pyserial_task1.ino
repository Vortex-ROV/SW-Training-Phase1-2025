const int ledPin = 13;  
String input = "";      

void setup() {
  pinMode(ledPin, OUTPUT);   
  Serial.begin(9600);        
}

void loop() {
  if (Serial.available() > 0) {
    input = Serial.readStringUntil('\n');  
    
    if (input == "on") {
      digitalWrite(ledPin, HIGH);  
      Serial.println("LED is ON");
    }
    else if (input == "off") {
      digitalWrite(ledPin, LOW);   
      Serial.println("LED is OFF");
    }
  }
}
