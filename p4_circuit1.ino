#include <Servo.h>
Servo myServo;

void setup()
{
  //myServo.attach(13);
}

void loop()
{
  //myServo.write(135);//changes based how to swing shovel
  //delay(1000);
  //myServo.write(-135);//changes based how to swing shovel
  //delay(1000);
}

//second circuit turns both servo motors 270 and -270 deg on repeat
	//but only when pushbutton is pressed
//first circuit turns dc cw or ccw
	//if both switches left = ccw w/ +rpm
	//if both switches right = cw w/ -rpm
	//if one left one right = off