
void setup() {
  Serial.begin(9600);
}

void loop() {
  int ch1 = analogRead(A0);  // EMG Channel 1
  int ch2 = analogRead(A1);  // EMG Channel 2
  Serial.print(ch1);
  Serial.print(",");
  Serial.print(ch2);
  Serial.print(",");
  Serial.println(millis());  // Time in ms
  delay(10);  // 100 Hz sampling rate
}
