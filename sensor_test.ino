#define TRIG_PIN 2  
#define ECHO_PIN 3  
#define Buzzer_PIN 4
#define pot_PIN A1

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(pot_PIN,INPUT);
  pinMode(Buzzer_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(TRIG_PIN, LOW); 
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // calc duration
  long duration = pulseIn(ECHO_PIN, HIGH); 

  // Calc the distance (cm)
  int distance = (duration * 0.0343) / 2;
  Serial.print("distance");
  Serial.println(distance);
  
  float read=analogRead(pot_PIN);
  float critical = read*(100.0/1023.0);
  Serial.print(pot_PIN);  
  Serial.print("critical");
  Serial.println(critical);

  if (distance <=critical)
  {
    digitalWrite(Buzzer_PIN,HIGH);
  }else {
  {
    digitalWrite(Buzzer_PIN, LOW);
  }
  }delay(500);
}
