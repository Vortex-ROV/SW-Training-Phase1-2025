const int ledPin = 13;  // Pin where the internal LED is connected
bool ledState = false;  // LED state (ON/OFF)

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 bps
  pinMode(ledPin, OUTPUT); // Set LED pin as output
  digitalWrite(ledPin, ledState); // Initialize LED state
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the incoming command
    command.trim(); // Remove any whitespace

    if (command.equalsIgnoreCase("ON")) {
      ledState = true; // Set LED state to ON
      digitalWrite(ledPin, HIGH); // Turn on the internal LED
      Serial.println("Internal LED is ON");
    } else if (command.equalsIgnoreCase("OFF")) {
      ledState = false; // Set LED state to OFF
      digitalWrite(ledPin, LOW); // Turn off the internal LED
      Serial.println("Internal LED is OFF");
    }
  }
}
