#include "uasc.h"
#define trig_left 2
#define echo_left 3

void setup(){
  pinMode(trig_left, OUTPUT);
  pinMode(echo_left, INPUT);
  pinMode(trig_middle, OUTPUT);
  pinMode(echo_middle, INPUT);
  Serial.begin(9600);
}


void loop (){
  uasc_measure_left();
  uasc_measure_middle(){;
}
