#define trig_left 2
#define echo_left 3

long duration_left;
int distance_left;

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