int button = 2;
int reading = 0;
int buttonState = 0;
int lastButtonState = 0;

void setup() {
  pinMode(button, INPUT);
  Serial.begin(9600);  // Initialize the serial communication
}

void loop() {
  reading = digitalRead(button);

  // Check if the button state has changed
  if (reading != lastButtonState) {
    buttonState = reading;

    // Send the current state over the serial port
    if (buttonState == HIGH) {
      Serial.println("Button pressed");
    } else {
      Serial.println("Button released");
    }
  }

  // Save the current state for the next loop iteration
  lastButtonState = reading;
}
