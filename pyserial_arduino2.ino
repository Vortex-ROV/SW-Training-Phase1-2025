#define BUTTON_PIN 12 // Pin where the LED is connected
int Current_State=LOW;
int Last_State =LOW;
unsigned long lastDebouncedTime = 0;
unsigned long DebouncedDelay = 50;
void setup() {
  pinMode(BUTTON_PIN, INPUT);
  Serial.begin(9600); 
}

void loop() {
  int reading =digitalRead(BUTTON_PIN);

  if (reading !=Last_State)    //button has been pressed not equal the previous state?
  { 
    lastDebouncedTime=millis();    //if yes reset the last debounced time
  
  }if (millis()-lastDebouncedTime>DebouncedDelay)     //check the stability
   {if (reading !=Current_State)                             //check change in button
   { 
    Current_State=reading;
   }

   }
  Serial.println(Current_State);
  Last_State=Current_State;
  }

