#include "uasc.h"
#include "error_code.h"

volatile unsigned int counter = 0;
unsigned long time_in  = 0;
unsigned long time_off = 0;
inline void real_delay();

unsigned int delay_time = 1000;

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
    time_in = millis();
    counter++;
    if(uasc_left_enabled){
      uasc_measure_left();
    }
    if(uasc_middle_enabled){
      uasc_measure_middle();
    }
    if(uasc_right_enabled){
      uasc_measure_right();
    }


    time_off = millis();
    real_delay();
}

void real_delay(){
  if( (time_off-time_in) < delay_time)
    delay(delay_time - (time_off-time_in));
  else 
    error_code(1);
}
