#define trig_left 2
#define echo_left 3
#define trig_middle 4
#define echo_middle 5
#define trig_right 6
#define echo_right 7

volatile long duration_left;
volatile int distance_left;
volatile long duration_middle;
volatile int distance_middle;
volatile long duration_right;
volatile int distance_right;

inline void uasc_measure_left(){
    digitalWrite(trig_left, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_left, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_left, LOW);
    duration_left = pulseIn(echo_left, HIGH);
    distance_left = duration_left * 0.017;
    Serial.print("Distance: ");
    Serial.print(distance_left);
    Serial.println(" cm");
}
inline void uasc_measure_middle(){
    digitalWrite(trig_middle, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_middle, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_middle, LOW);
    duration_middle = pulseIn(echo_middle, HIGH);
    distance_middle = duration_middle * 0.017;
    Serial.print("Distance: ");
    Serial.print(distance_middle);
    Serial.println(" cm");
}
inline void uasc_measure_right(){
    digitalWrite(trig_right, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_right, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_right, LOW);
    duration_right = pulseIn(echo_right, HIGH);
    distance_right = duration_right * 0.017;
    Serial.print("Distance: ");
    Serial.print(distance_right);
    Serial.println(" cm");
}