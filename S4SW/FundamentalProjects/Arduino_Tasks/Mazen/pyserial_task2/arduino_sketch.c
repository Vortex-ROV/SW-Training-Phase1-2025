const int buttonPin = 2;      // Button connected to digital pin 2
const int ledPin = 13;        // LED connected to digital pin 13

int ledState = LOW;           // the current state of the LED
int buttonState;              // current reading from the button
int lastButtonState = LOW;    // previous reading from the button
unsigned long lastDebounceTime = 0; // the last time the output was toggled
const unsigned long debounceDelay = 50; // the debounce time in milliseconds

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);  // initialize the LED state
}

void loop() {
  int reading = digitalRead(buttonPin);

  // Check if the button state has changed
  if (reading != lastButtonState) {
    lastDebounceTime = millis(); // reset the debounce timer
  }

  // If the debounce delay has passed, take action
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // Only toggle the LED if the new reading is different from the last stable state
    if (reading != buttonState) {
      buttonState = reading;

      // Toggle the LED when the button is pressed
      if (buttonState == HIGH) {
        ledState = !ledState;
        digitalWrite(ledPin, ledState); // update the LED state
        Serial.println("pressed");
      } else {
        Serial.println("released");
      }
    }
  }

  lastButtonState = reading; // save the reading as the last state
}
