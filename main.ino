#include "motor.h"

//volatile int speed = 0;

void setup(){
  pinMode(motor1_in1, OUTPUT);
  pinMode(motor1_in2, OUTPUT);
  pinMode(motor2_in1, OUTPUT);
  pinMode(motor2_in2, OUTPUT);

  analogWrite(motor1_in1, 0);
  analogWrite(motor1_in2, 0);

    speed = 255;
}

void loop (){
    set_direction();
}
