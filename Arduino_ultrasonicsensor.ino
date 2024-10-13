const int trigPin = 9;          
const int echoPin = 10;         
const int buzzerPin = 11;       
const int potentiometerPin = A0; 

long duration;
float distance;                


int potValue;
float thresholdDistance;        

void setup() {
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2; 
  
 
  potValue = analogRead(potentiometerPin);
  thresholdDistance = map(potValue, 0, 1023, 5, 100); // Map potentiometer value to distance range 

 
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm, Threshold: ");
  Serial.print(thresholdDistance);
  Serial.println(" cm");

 
  if (distance <= thresholdDistance) {
    digitalWrite(buzzerPin, HIGH);  
  } else {
    digitalWrite(buzzerPin, LOW);   
  }

delay(1000);
}