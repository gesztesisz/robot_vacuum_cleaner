#define uascLeft_Trig   2
#define uascLeft_Echo   3
#define uascMiddle_Trig 4
#define uascMiddle_Echo 5   
#define uascRight_Trig  6   
#define uascRight_Echo  7 

volatile long duration;
volatile int distance; 

const int warning_distance = 2; // SEND SIGNAL IF SOMETHING IS IN THIS RANGE

int measure_uascLeft   (){
    digitalWrite(uascLeft_Trig, LOW);
    delayMicroseconds(2);
    digitalWrite(uascLeft_Trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(uascLeft_Trig, LOW);

    duration = pulseIn(uascLeft_Echo, HIGH);
    distance = duration * 0.034 / 2; 

    if(distance <= warning_distance){
        return 1;
    }
    return 0;
};
int measure_uascMiddle (){
    digitalWrite(uascMiddle_Trig, LOW);
    delayMicroseconds(2);
    digitalWrite(uascMiddle_Trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(uascMiddle_Trig, LOW);

    duration = pulseIn(uascMiddle_Echo, HIGH);
    distance = duration * 0.034 / 2; 
    
    if(distance <= warning_distance){
        return 1;
    }
    return 0;
};
int measure_uascRight  (){
    digitalWrite(uascRight_Trig, LOW);
    delayMicroseconds(2);
    digitalWrite(uascRight_Trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(uascRight_Trig, LOW);

    duration = pulseIn(uascRight_Echo, HIGH);
    distance = duration * 0.034 / 2; 
    
    if(distance <= warning_distance){
        return 1;
    }
    return 0;
};