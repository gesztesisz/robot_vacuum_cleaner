#define motor1_in1 10
#define motor1_in2 11

#define motor2_in1 6
#define motor2_in2 9


// 1  = forward
// 0  = stop
// -1 = backward
int direction = 0;  

void direction();

void setup(){
  pinMode(motor1_in1, OUTPUT);
  pinMode(motor1_in2, OUTPUT);
  pinMode(motor2_in1, OUTPUT);
  pinMode(motor2_in2, OUTPUT);

  digitalWrite(motor1_in1, LOW);
  digitalWrite(motor1_in2, LOW);
}

void loop (){
    direction();
}

void direction(){
    if(direction == 1 ){
        digitalWrite(motor1_in1, LOW);
        digitalWrite(motor1_in2, HIGH);

        digitalWrite(motor2_in1, LOW);
        digitalWrite(motor2_in2, HIGH);
    }
    else if(direction == -1){
        digitalWrite(motor1_in1, HIGH);
        digitalWrite(motor1_in2, LOW);

        digitalWrite(motor2_in1, HIGH);
        digitalWrite(motor2_in2, LOW);
    }
    else {
        digitalWrite(motor1_in1, LOW);
        digitalWrite(motor1_in2, LOW);

        digitalWrite(motor2_in1, LOW);
        digitalWrite(motor2_in2, LOW);
    }
}