// Define pin connections
const int trigPin = 10;
const int echoPin = 9;
const int buzzerPin = 8;
const int potentiometerPin = A0;


// Variables
long duration;
int distance;
int threshold;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Initialize sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  // Initialize buzzer and LED pins
  pinMode(buzzerPin, OUTPUT);
  
  // Initialize potentiometer pin
  pinMode(potentiometerPin, INPUT);
  
  // Ensure buzzer and LED are off at start
  digitalWrite(buzzerPin, LOW);

}

void loop() {
  // Read the potentiometer value (0 - 1023)
  int potValue = analogRead(potentiometerPin);
  
  // Map potentiometer value to distance threshold (e.g., 10cm to 400cm)
  threshold = map(potValue, 0, 1023, 10, 400);
  
  // Trigger the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the echo time
  duration = pulseIn(echoPin, HIGH, 30000); // Timeout after ~300ms
  
  // Calculate distance in cm
  distance = duration * 0.034 / 2;
  
  // Print distance to Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm\tThreshold: ");
  Serial.print(threshold);
  Serial.println(" cm");
  
  // Compare distance with threshold
  if (distance > 0 && distance >= threshold) {
    // Activate buzzer and LED
    digitalWrite(buzzerPin, HIGH);
  } else {
    // Deactivate buzzer and LED
    digitalWrite(buzzerPin, LOW);
  }
  
  delay(1000); // Short delay before next reading
}
