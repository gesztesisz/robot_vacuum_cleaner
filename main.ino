#include "uasc.h"


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
  uasc_measure_left();
  uasc_measure_middle();
  uasc_measure_right();
  Serial.println();
  delay(50);
}
