#include <dht11.h>
#define DHT11PIN 8

dht11 DHT11;

int IN1 = 2;
int IN2 = 3;
int IN3 = 4;
int Pin1 = A0;
int Pin2 = A1; 
int Pin3 = A2;
 
float value1 = 0;
float value2 = 0;
float value3 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(Pin1, INPUT);
  digitalWrite(IN1, HIGH);

  pinMode(IN2, OUTPUT);
  pinMode(Pin2, INPUT);
  digitalWrite(IN2, HIGH);

  pinMode(IN3, OUTPUT);
  pinMode(Pin3, INPUT);
  digitalWrite(IN3, HIGH);

  delay(500);
}
void loop() {
  value1 = analogRead(Pin1);
  value2 = analogRead(Pin2);
  value3 = analogRead(Pin3);

  Serial.println("sos");
  Serial.print("moisture_s1,");
  Serial.println(value1);
  if(value1>454)
  {
      digitalWrite(IN1, LOW);
  }
  else
  {
    digitalWrite(IN1, HIGH);
    }

  Serial.print("moisture_s2,");
  Serial.println(value2);
  if(value2>454)
  {
      digitalWrite(IN2, LOW);
  }
  else
  {
    digitalWrite(IN2, HIGH);
    }

  Serial.print("moisture_s3,");
  Serial.println(value3);
  if(value3>454)
  {
      digitalWrite(IN3, LOW);
  }
  else
  {
    digitalWrite(IN3, HIGH);
    }
    int chk = DHT11.read(DHT11PIN);

  Serial.print("Humidity,");
  Serial.println((float)DHT11.humidity, 2);

  Serial.print("Temperature,");
  Serial.println((float)DHT11.temperature, 2);
  Serial.println("eos");
  Serial.println();
  delay(10);
}
