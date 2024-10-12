#define LED_PIN 13 // Pin where the LED is connected

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  // Check if data is available to read
if (Serial.available()) 
  {
    char command = Serial.read(); // Read the command
    if (command == '1') {
      digitalWrite(LED_PIN, HIGH); // Turn LED on
    } else if (command == '0') {
      digitalWrite(LED_PIN, LOW); // Turn LED off
    }
  }
}
