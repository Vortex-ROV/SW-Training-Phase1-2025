// C++ code

// Define pin constants
const int trigPin = 7;
const int echoPin = 6;
const int buzzerPin = 9;
const int potPin = A0;

// Speed of sound in cm/us (343 m/s)
const float speedOfSound = 0.0343; 


void setup()
{
 // Set up pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);

  // Start serial communication
  Serial.begin(9600);
}

void loop()
{
  // Read distance from ultrasonic sensor
  float distance = getDistance();

  // Read potentiometer to define the threshold distance
  int potValue = analogRead(potPin);
  int thresholdDistance = map(potValue, 0, 1023, 5, 100); // Adjustable threshold from 5 cm to 100 cm  
  
  //check if distance is too close
  if(distance <= thresholdDistance){
  	 digitalWrite(buzzerPin, HIGH);  // Buzz if distance is too close
  } else {
    digitalWrite(buzzerPin, LOW);   // Turn off the buzzer if safe
  }
  
  // measure the ping time in cm
  Serial.print(distance);
  Serial.println("cm");
  delay(100); // Wait for 100 millisecond(s)
}


float getDistance(){
	digitalWrite(trigPin,LOW);
  	delayMicroseconds(2);
  	digitalWrite(trigPin,HIGH);
  	delayMicroseconds(10);
  	digitalWrite(trigPin,LOW);
  
  	float duration = pulseIn(echoPin,HIGH);
  	float distance = (duration * speedOfSound)/2;

    return distance; 
}
