#define motor1_in1 10
#define motor1_in2 11
#define motor2_in1 6
#define motor2_in2 9

// 1  = forward
// 0  = stop
// -1 = backward
int direction = 0;  

void set_direction(){
    if(speed > 0 ){ 
        analogWrite(motor1_in1, 0);
        analogWrite(motor1_in2, speed);

        analogWrite(motor2_in1, 0);
        analogWrite(motor2_in2, speed);
    }
    else if(speed < 0 ){
        analogWrite(motor1_in1, speed);
        analogWrite(motor1_in2, 0);

        analogWrite(motor2_in1, speed);
        analogWrite(motor2_in2, 0);
    }
    else {
        analogWrite(motor1_in1, 0);
        analogWrite(motor1_in2, 0);

        analogWrite(motor2_in1, 0);
        analogWrite(motor2_in2, 0);
    }
}