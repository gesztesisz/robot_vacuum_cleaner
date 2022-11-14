#define trig_left 2
#define echo_left 3
#define trig_middle 4
#define echo_middle 5

long duration_left;
int distance_left;
long duration_middle;
int distance_middle;

void uasc_measure_left(){
    digitalWrite(trig_left, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_left, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_left, LOW);
    duration_left = pulseIn(echo_left, HIGH);
    distance_left = duration_left * 0.034 / 2;
    Serial.print("Distance: ");
    Serial.print(distance_left);
    Serial.println(" cm");
}
void uasc_measure_middle(){
    digitalWrite(trig_middle, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_middle, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_middle, LOW);
    duration_middle = pulseIn(echo_middle, HIGH);
    distance_middle = duration_middle * 0.034 / 2;
    Serial.print("Distance: ");
    Serial.print(distance_middle);
    Serial.println(" cm");
}