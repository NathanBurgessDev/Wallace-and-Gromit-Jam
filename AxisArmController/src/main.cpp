// #include <stdio.h>
#include <pb_decode.h>
#include <pb_encode.h>
#include "move.pb.h"
#include <Arduino.h>

byte sizeBuff[4];
byte bingos[4] = {1,2,3,4};
int buffSize = 0;

int recieveMessage(){

    // moveTo message = moveTo_init_zero;

    // pb_istream_t stream = pb_istream_from_buffer(buffer,message_length);

    return 0;
}

void setup() {
  Serial.begin(9600);
  Serial.write("Hello World");
}

void loop() {
  // first 4 bytes = number of bytes to expect
  if (Serial.available() >= 4 && buffSize == 0){
    // write first 4 bytes to  
    Serial.readBytes(sizeBuff, 4);
    Serial.write(sizeBuff,4);
  }
}
