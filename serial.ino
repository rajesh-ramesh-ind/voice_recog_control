int data,led=8;
void setup()
{ 
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(led, OUTPUT); //make the LED pin (8) as output
  digitalWrite (led, LOW);  
  Serial.println("Hi!, I am Arduino");
}
 
void loop() 
{
  while (Serial.available())
  {
  data = Serial.read();
  }
  if (data == '1')
    digitalWrite (led, HIGH);
  else if (data == '0')
    digitalWrite (led, LOW);
}
