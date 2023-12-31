void setup() {
 Serial.begin(9600); // Starts the serial communication at 9600 baud
}

void loop() {
 Serial.println("Hello World"); // Sends the string "Hello World" over serial
 delay(1000); // Waits for a second before sending the next string
}
