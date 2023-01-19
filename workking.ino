#define BLYNK_TEMPLATE_ID           "TMPL7mL9rYa-"
#define BLYNK_DEVICE_NAME           "Quickstart Device"
#define BLYNK_AUTH_TOKEN            "i_4zHgN5P5oLEED5f1uMoCnDNWSszxGw"

#define trig D0 //Setting UltraSonic's trig pin to D0
#define echo D1 //Setting UltraSonic's echo pin to D1
#define motor D2 //Setting motor's output pin to D2
#define BLYNK_PRINT Serial

long tankDepth=100; // change value according to the tank depth in cm

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <Servo.h> // servo library  
Servo s1; 

//wifi crenditials
char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "RK_X3";
char pass[] = "ruchan10";

BlynkTimer timer;

long readUltrasonicDistance(int trig, int echo){
  pinMode(trig,OUTPUT);
  digitalWrite(trig,LOW);
  delay(100);
  digitalWrite(trig,HIGH);
  delay(100);
  digitalWrite(trig,LOW);
  pinMode(echo,INPUT);
  return pulseIn(echo, HIGH); //return the value extracted through the sensor
}

// This function is called every time the Virtual Pin 0 state changes
BLYNK_WRITE(V0)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();
  // Update state
  Blynk.virtualWrite(V1, value);
  Blynk.virtualWrite(V0, value);
}

// This function is called every time the device is connected to the Blynk.Cloud
BLYNK_CONNECTED()
{
  Blynk.syncVirtual(V0);
}

// main function
void waterLevel(){
  long cm=0.01723*readUltrasonicDistance(trig,echo); //converting the data to cm
  Serial.print(cm);
  Serial.println(" cm");
  delay(100);
  pinMode(trig, OUTPUT);
  digitalWrite(D6,HIGH); //REMOVE

  if(cm>.9*tankDepth){ // turn on the motor if water level is too low
    digitalWrite(motor,HIGH); 
    Serial.println("Motor ON");
    s1.write(0);  
    delay(100);  
    s1.write(180);  
    delay(100);  
    Blynk.virtualWrite(V1,1);
  }
  else if(cm<.1*tankDepth){ //turn off the water motor when tank is almost full
    digitalWrite(motor,LOW); 
    Serial.println("Motor OFF");
    Blynk.virtualWrite(V1,0);
  }
  else{ // do nothing if water is in medium level
    Serial.println("MOTOR IDEAL");
  }

  double level= tankDepth-cm; //actual water level
  if(level>0){ //send the water level to app
    long percentage=((level/tankDepth))*100;
    Blynk.virtualWrite(V0,percentage);
  }
  else{
    Blynk.virtualWrite(V0,0);
  }
}
// control the motor through the app
BLYNK_WRITE(V1)
{  
  if(param.asInt()==0)
  {
     digitalWrite(motor,LOW);
        Serial.println(" Motor Turned OFF");
  }
  else{
   Serial.println(" Motor Turned ON");
   Blynk.virtualWrite(V1,1);
   digitalWrite(motor,HIGH);
   s1.write(0);  
   delay(100);  
   s1.write(180);  
   delay(100);     
  }
}

void setup()
{
  // Debug console
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  pinMode(trig, OUTPUT);
  pinMode(motor, OUTPUT);
  pinMode(echo, INPUT);
  delay(1000);
  timer.setInterval(10L, waterLevel);
  s1.attach(4);  // attach servo to D2
}

void loop()
{
  Blynk.run();
  timer.run();
}
