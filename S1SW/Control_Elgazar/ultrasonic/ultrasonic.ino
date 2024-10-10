#define echoPin 2
#define trigPin 3 
#define buzzer 4

long duration;
int distance;
int sensorValue = 0;

void setup() {
  pinMode(A0, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(trigPin,OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT

  // Serial Communication is starting with 9600 of
  // baudrate speed
  Serial.begin(9600);

  // The text to be printed in serial monitor
  Serial.println(
    "Distance measurement using Arduino Uno.");
  delay(500);
}

void loop() {
  sensorValue = analogRead(A0);
  sensorValue = (sensorValue / 1023.0) * 100.0;

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.0344 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  if (distance < sensorValue) {
    digitalWrite(buzzer, HIGH);
    // Serial.print("Buzzing");
  } else {
    digitalWrite(buzzer, LOW);
  }

  delay(100);
}