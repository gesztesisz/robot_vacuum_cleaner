#include "uasc.h"
#define trig_left 2
#define echo_left 3

long duration_left;
int distance_left;

void setup(){
  pinMode(trig_left, OUTPUT);
  pinMode(echo_left, INPUT);
  Serial.begin(9600);
}


void loop (){
  uasc_measure_left();
}
