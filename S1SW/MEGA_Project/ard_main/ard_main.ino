#define speedL 3
#define IN1 5
#define IN2 6
#define IN3 9
#define IN4 10
#define speedR 11


void setup() {
  Serial.begin(9600);
  for(int i=5; i<=10; i++) {
    pinMode(i, OUTPUT);
  }
}

void forword() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 150);
  analogWrite(speedR, 150);
}

void backword() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(speedL, 150);
  analogWrite(speedR, 150);
}

void left() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 0);
  analogWrite(speedR, 150);
}

void right() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 150);
  analogWrite(speedR, 0);
}

void stopp() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 0);
  analogWrite(speedR, 0);
}

void loop() {
  if(Serial.available() > 0){
    String msg = Serial.readString();
    if(msg == "forward"){
      forword();
      } else if(msg == "backward"){
        backword();
       }else if(msg == "left"){
        left();
      } else if(msg == "right"){
        right();
      } else if(msg == "laser"){
      // forword();
      } else if(msg == "laser"){
        stop();
      }
    }
}
