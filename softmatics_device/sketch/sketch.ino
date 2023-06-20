void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);  // initialization
}

void loop() {
  byte var;
  var = Serial.read();
  switch(var){
    case '0':
      digitalWrite(13, LOW);
      Serial.println("13 to LOW for releasing");
      break;
    case '1':
      digitalWrite(13, HIGH);
      Serial.println("13 to HIGH for grasping");
      break;
    default:
      break;
  }
}