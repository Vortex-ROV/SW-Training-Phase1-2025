#define trigPin 12 
#define echoPin 11
#define buzzerPin = 8;
#define potPin = A0;
long duration, distance;
float distanceThreshold = 10.0; 
void setup() {
  Serial.begin (9600); 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  pinMode(buzzerPin, OUTPUT);
  pinMode(potPin, INPUT);
}
void loop() {
  int potValue = analogRead(potPin);

  distanceThreshold = map(potValue, 0, 1023, 1, 50);

  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) * 0.0343; 
  
  Serial.println(distance);
  Serial.println(distanceThreshold);
  
  if(distance > 0 && distance <= distanceThreshold) {
    digitalWrite(buzzerPin, HIGH);
  } else {
    digitalWrite(buzzerPin, LOW);
  }
  
  
  delay(50); 
  

}