#define IN_leftA 2
#define IN_leftB 8
#define IN_rightA 12
#define IN_rightB 13

#define RightMotor 9
#define LeftMotor 10

#define LeftSensor A2
#define RightSensor A0
#define MiddleSensor A1

int left_sensor_read, right_sensor_read, middle_sensor_read;
int prev_left_sensor_read, prev_right_sensor_read, prev_middle_sensor_read;

void setup() {
  pinMode(IN_leftA, OUTPUT);
  pinMode(IN_leftB, OUTPUT);
  pinMode(IN_rightA, OUTPUT);
  pinMode(IN_rightB, OUTPUT);

  pinMode(RightMotor, OUTPUT);
  pinMode(LeftMotor, OUTPUT);

  pinMode(LeftSensor, INPUT);
  pinMode(RightSensor, INPUT);
  pinMode(MiddleSensor, INPUT);

  Serial.begin(9600);
}

void loop() {
  // Store previous sensor readings for recovery purposes
  prev_left_sensor_read = left_sensor_read;
  prev_right_sensor_read = right_sensor_read;
  prev_middle_sensor_read = middle_sensor_read;

  // Read current sensor values
  left_sensor_read = digitalRead(LeftSensor);
  right_sensor_read = digitalRead(RightSensor);
  middle_sensor_read = digitalRead(MiddleSensor);

  int speed = 50;      // Default motor speed
  int turn_speed = 30; // Slower speed when turning

  // Forward movement when the middle sensor detects the line
  if (middle_sensor_read == HIGH && left_sensor_read == LOW && right_sensor_read == LOW) {
    digitalWrite(IN_leftA, HIGH);
    digitalWrite(IN_leftB, LOW);
    analogWrite(LeftMotor, speed);

    digitalWrite(IN_rightA, HIGH);
    digitalWrite(IN_rightB, LOW);
    analogWrite(RightMotor, speed);

  } 
  // Veering slightly right when the left sensor detects the line
  else if (middle_sensor_read == LOW && left_sensor_read == HIGH && right_sensor_read == LOW) {
    digitalWrite(IN_leftA, HIGH);
    digitalWrite(IN_leftB, LOW);
    analogWrite(LeftMotor, speed);
    
    digitalWrite(IN_rightA, HIGH);
    digitalWrite(IN_rightB, LOW);
    analogWrite(RightMotor, turn_speed);

  } 
  // Veering slightly left when the right sensor detects the line
  else if (middle_sensor_read == LOW && left_sensor_read == LOW && right_sensor_read == HIGH) {
    digitalWrite(IN_leftA, HIGH);
    digitalWrite(IN_leftB, LOW);
    analogWrite(LeftMotor, turn_speed);
    
    digitalWrite(IN_rightA, HIGH);
    digitalWrite(IN_rightB, LOW);
    analogWrite(RightMotor, speed);

  } 
  // 90-degree left turn when both middle and left sensors detect the line
  else if (middle_sensor_read == HIGH && left_sensor_read == HIGH && right_sensor_read == LOW) {
    digitalWrite(IN_leftA, LOW);  // Left motor backward