// https://www.tinkercad.com/things/f2sIKYzhcuv-surprising-elzing/editel?returnTo=https%3A%2F%2Fwww.tinkercad.com%2Fdashboard%2Fdesigns%2Fcircuits&sharecode=nN15fsV2gIoJe9p5xGCUmSYwkS4_YOBb2p4mBaKBaF//d
#define trigPin 2
#define echoPin 4
#define BuzzerPin 7
int Pot = A0;
int POT_Reading = 0;
long duration, distance;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(Pot, INPUT);
  pinMode(BuzzerPin, OUTPUT);
}

void loop() {
  // Read potentiometer value
  POT_Reading = analogRead(Pot);

  // Send pulse to ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the duration of the echo
  duration = pulseIn(echoPin, HIGH);

  // Calculate distance in cm
  distance = (duration / 2) * 0.0343;

  // Print the potentiometer value and distance to the Serial Monitor
  Serial.print("Potentiometer Reading: ");
  Serial.print(POT_Reading);
  Serial.print("  |  Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(5);

  // Control buzzer based on distance and potentiometer reading
  if (distance <= POT_Reading) {
    digitalWrite(BuzzerPin, HIGH);
    delay(distance * 30);
    digitalWrite(BuzzerPin, LOW);
    delay(distance * 30);
  }

}
