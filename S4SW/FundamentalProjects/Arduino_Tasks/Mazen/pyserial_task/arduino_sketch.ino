const int ledPin = 13;  // LED connected to digital pin 13

void setup() {
  pinMode(ledPin, OUTPUT);    // Set the LED pin as output
  Serial.begin(9600);         // Start serial communication at 9600 baud
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming byte as a String
    String command = Serial.readStringUntil('\n');
    command.trim(); // Remove any newline or extra spaces

    // Turn LED on or off based on the command
    if (command == "ON") {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned ON");
    } else if (command == "OFF") {
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned OFF");
    } else {
      Serial.println("Unknown command");
    }
  }
}
