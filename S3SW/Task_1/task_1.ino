// Motor Control Pins
int IN1 = 2;
int IN2 = 8;
int IN3 = 12;
int IN4 = 13;
int EnPin1 = 9;  // PWM pin for right motor speed control
int EnPin2 = 10; // PWM pin for left motor speed control

// Buzzer Pin
int buzzerPin = 7;  // Define a pin for the buzzer

// Speed values for motors
int speedValue = 255;  // Maximum speed (can be adjusted)

// Setup function to initialize pins and serial communication
void setup() {
    // Set motor control pins as outputs
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
    
    // Set enable (PWM) pins as outputs
    pinMode(EnPin1, OUTPUT);
    pinMode(EnPin2, OUTPUT);

    // Set buzzer pin as output
    pinMode(buzzerPin, OUTPUT);

    // Set initial motor speed (PWM values)
    analogWrite(EnPin1, 100);  // Right motor initial speed
    analogWrite(EnPin2, 100);  // Left motor initial speed

    // Start serial communication
    Serial.begin(9600); 
}

// Main loop to read serial commands and control motors and buzzer accordingly
void loop() {
    // Check if there is any data available on the serial port
    if (Serial.available()) {
        // Read the incoming command
        char command = Serial.read();
        
        // Perform action based on the received command
        switch (command) {
            case 'f':  // Move forward
                digitalWrite(IN1, HIGH);  // Right motor forward
                digitalWrite(IN2, LOW);
                digitalWrite(IN3, HIGH);  // Left motor forward
                digitalWrite(IN4, LOW);
                analogWrite(EnPin1, speedValue);  // Set right motor speed
                analogWrite(EnPin2, speedValue);  // Set left motor speed
                break;
            
            case 'b':  // Move backward
                digitalWrite(IN1, LOW);   // Right motor backward
                digitalWrite(IN2, HIGH);
                digitalWrite(IN3, LOW);   // Left motor backward
                digitalWrite(IN4, HIGH);
                analogWrite(EnPin1, speedValue);  // Set right motor speed
                analogWrite(EnPin2, speedValue);  // Set left motor speed
                break;

            case 'l':  // Turn left
                digitalWrite(IN1, LOW);   // Stop right motor or move backward
                digitalWrite(IN2, HIGH);
                digitalWrite(IN3, HIGH);  // Left motor forward
                digitalWrite(IN4, LOW);
                analogWrite(EnPin1, speedValue);  // Set right motor speed
                analogWrite(EnPin2, speedValue);  // Set left motor speed
                break;

            case 'r':  // Turn right
                digitalWrite(IN1, HIGH);  // Right motor forward
                digitalWrite(IN2, LOW);
                digitalWrite(IN3, LOW);   // Stop left motor or move backward
                digitalWrite(IN4, HIGH);
                analogWrite(EnPin1, speedValue);  // Set right motor speed
                analogWrite(EnPin2, speedValue);  // Set left motor speed
                break;

            case 's':  // Stop motors
                digitalWrite(IN1, LOW);
                digitalWrite(IN2, LOW);
                digitalWrite(IN3, LOW);
                digitalWrite(IN4, LOW);
                analogWrite(EnPin1, 0);  // Stop right motor
                analogWrite(EnPin2, 0);  // Stop left motor
                break;

            case 'u':  // Turn buzzer on
                digitalWrite(buzzerPin, HIGH);  // Buzzer on
                break;

            case 'p':  // Turn buzzer off
                digitalWrite(buzzerPin, LOW);  // Buzzer off
                break;
            
            default:
                // Do nothing if an unknown command is received                      
                break;
        }
    }
}
