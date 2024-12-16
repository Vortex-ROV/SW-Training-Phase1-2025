#define trigPin 12 
#define echoPin 11
#define buzzerPin = 8;
long duration, distance;
const float distanceThreshold = 10.0; 
void setup() {
  Serial.begin (9600); 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  pinMode(buzzerPin, OUTPUT);
}
void loop() {
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) * 0.0343; 
  
  Serial.println(distance);
  
  if(distance > 0 && distance <= distanceThreshold) {
    digitalWrite(buzzerPin, HIGH);
  } else {
    digitalWrite(buzzerPin, LOW);
  }
  
  
  delay(50); 
  

}