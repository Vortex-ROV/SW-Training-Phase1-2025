#define ledPin 13
// char receivedChar; 

void setup() {
  pinMode(ledPin, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // receivedChar = Serial.read(); 
    
    if (Serial.read() == '1') {
      digitalWrite(ledPin, HIGH); 
    }
    else if (Serial.read() == '0') {
      digitalWrite(ledPin, LOW); 
    }
  }
}
