int IN1 = 2;
int IN2 = 8;
int IN3 = 12;
int IN4 = 13;
int EnPin1 = 9 ;
int EnPin2 = 10 ;


int laserPin = 9;

void setup() {
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
    pinMode(laserPin, OUTPUT);
    pinMode(EnPin1, OUTPUT);
    pinMode(EnPin2, OUTPUT);
    analogWrite(EnPin1 ,60);
    analogWrite(EnPin2 ,30);
    Serial.begin(9600); 
}

void loop() {
 
    if (Serial.available()) {
        char command = Serial.read();

        switch (command) {
            case 'w':  // Move forward
                digitalWrite(IN1, HIGH);
                digitalWrite(IN2, LOW);
                digitalWrite(IN3, HIGH);
                digitalWrite(IN4, LOW);
                analogWrite(EnPin1 ,60);
                analogWrite(EnPin2 ,60);
                
                break;
            
            case 's':  // Move backward
                digitalWrite(IN1, LOW);
                digitalWrite(IN2, HIGH);
                digitalWrite(IN3, LOW);
                digitalWrite(IN4, HIGH);
                analogWrite(EnPin1 ,60);
                analogWrite(EnPin2 ,60);
                break;

            case 'd':  // Turn left
                digitalWrite(IN1, LOW);
                digitalWrite(IN2, HIGH);
                digitalWrite(IN3, HIGH);
                digitalWrite(IN4, LOW);
                analogWrite(EnPin1 ,60);
                analogWrite(EnPin2 ,60);
                break;

            case 'a':  // Turn right
                digitalWrite(IN1, HIGH);
                digitalWrite(IN2, LOW);
                digitalWrite(IN3, LOW);
                digitalWrite(IN4, HIGH);
                analogWrite(EnPin1 ,60);
                analogWrite(EnPin2 ,60);
                break;

            case 'm':  // Stop
                digitalWrite(IN1, LOW);
                digitalWrite(IN2, LOW);
                digitalWrite(IN3, LOW);
                digitalWrite(IN4, LOW);
                
                break;

            case 'u':  // Turn laser on
                digitalWrite(laserPin, HIGH);
                break;

            case 'p':  // Turn laser off
                digitalWrite(laserPin, LOW);
                break;
            
            default:
                // Do nothing                      
                break;
        }
    }
}