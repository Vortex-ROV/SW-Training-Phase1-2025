const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); 
    if (command == '1') {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED ON");
    } else if (command == '0') {
      digitalWrite(ledPin, LOW); 
      Serial.println("LED OFF");
    } else {
      Serial.println("Invalid command");
    }
  }
}
