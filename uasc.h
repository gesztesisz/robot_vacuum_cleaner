#define trig_left 2
#define echo_left 3
#define trig_middle 4
#define echo_middle 5
#define trig_right 6
#define echo_right 7

volatile long duration;
volatile int distance;


inline void uasc_measure_left(){
    digitalWrite(trig_left, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_left, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_left, LOW);
    duration = pulseIn(echo_left, HIGH);
    distance = duration * 0.017;
    Serial.println(distance);

}
inline void uasc_measure_middle(){
    digitalWrite(trig_middle, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_middle, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_middle, LOW);
    duration = pulseIn(echo_middle, HIGH);
    distance= duration * 0.017;
    Serial.println(distance);
}
inline void uasc_measure_right(){
    digitalWrite(trig_right, LOW);
    delayMicroseconds(2);
    digitalWrite(trig_right, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig_right, LOW);
    duration = pulseIn(echo_right, HIGH);
    distance = duration * 0.017;
    Serial.println(distance);
}