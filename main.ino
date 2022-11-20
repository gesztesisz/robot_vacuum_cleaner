//volatile int speed = 0;
volatile unsigned int counter = 0;
unsigned long time_in  = 0;
unsigned long time_off = 0;
inline void real_delay();

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
inline void real_delay(){
  time_off = millis();
  Serial.println(delay_time - (time_off-time_in));
  if( (delay_time-(time_off - time_in)) >= 0)
    delay(delay_time - (time_off-time_in));
  //else 
    //error_code()
}