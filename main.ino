#include "motor.h"

volatile unsigned int counter = 0;
unsigned long time_in  = 0;
unsigned long time_off = 0;
inline void real_delay();

int delay_time = 50;

void setup(){
  pinMode(trig_left, OUTPUT);
  pinMode(echo_left, INPUT);
  pinMode(trig_middle, OUTPUT);
  pinMode(echo_middle, INPUT);
  pinMode(trig_right, OUTPUT);
  pinMode(echo_right, INPUT);
  Serial.begin(9600);
}


void loop (){
    counter++;
    if(!uasc_blocked){       //false -> blocked, true -> not blocked
      uasc_measure_left();
      uasc_measure_middle();
      uasc_measure_right();
    }
}
