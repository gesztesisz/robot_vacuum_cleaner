#include "motor.h"

//volatile int speed = 0;
volatile unsigned int counter = 0;
unsigned long time_in  = 0;
unsigned long time_off = 0;
void real_delay();

int delay_time = 50;

void setup(){
  counter++; //Simple counter check the SW is not in infinite loop
  if(counter == 65530)
    counter = 0;
  
}

void loop (){
  time_in = millis();


  real_delay();
}
void real_delay(){
  time_off = millis();
  delay(delay_time - (time_off-time_in));
}