// Sensors
const int potentiometer = A0;
const int echo = 7;

// Actuators
const int buzzer = 6;
const int trigger = 8;

// The distance in cm calculated using the ultrasonic sensor
int distance = 0;

// The minimum distance determined using the potentiometer
int minDistance = 0;

void setup()
{
  // Sensors
  pinMode(potentiometer, INPUT);
  
  // Actuators
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  // Reading the value of the potentiometer
  float voltage = analogRead(potentiometer);
  
  // Scaling From Range 0 -> 1023 To Range 3 -> 331 (the range of the ultrasonic sensor)
  minDistance = voltage * (328.0 / 1023.0) + 3.0;
  Serial.print("Minimum distance: ");
  Serial.println(minDistance);
  
  // Measure the ping time in cm
  distance = 0.01723 * readUltrasonicDistance(trigger, echo);
  Serial.print("Distance in cm: ");
  Serial.println(distance);
  
  // Open the buzzer if the distance is less than or equal to the minimum distance
  if (distance <= minDistance)
    	tone(buzzer, 450);
  else
    	noTone(buzzer);
  
  // Wait for 100 millisecond(s)
  delay(1000);
}

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  // Clear the trigger
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  
  // Set the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  
  // Read the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}