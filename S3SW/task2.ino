const int buttonPin = 2;     // Pin connected to the button
int buttonState = 0;         // Variable to store the button state
int lastButtonState = LOW;   // Previous state of the button
unsigned long lastDebounceTime = 0;  // Time the button state was last changed
unsigned long debounceDelay = 50;    // Debounce delay time

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int reading = digitalRead(buttonPin);  // Read the button state

  // If the button state has changed
  if (reading != lastButtonState) {
    lastDebounceTime = millis();  // Reset the debounce timer
  }

  // If enough time has passed (debounce)
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;  // Save the new state
      // Send the button state over serial communication
      if (buttonState == HIGH) {
        Serial.println("Button Pressed");
      } else {
        Serial.println("Button Released");
      }
    }
  }

  lastButtonState = reading;  // Save the last state
}
