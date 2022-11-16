#include "motor.h"

//volatile int speed = 0;
volatile unsigned int counter = 0;

void setup(){
  counter++; //Simple counter check the SW is not in infinite loop
  if(counter == 65530)
    counter = 0;
  
}

void loop (){

}
