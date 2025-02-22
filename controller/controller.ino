// #include <stdio.h>
// #include <../nanopb/pb_decode.h>
// #include <../nanopb/pb_encode.h>
// #include "protobufs/move.pb.h"

byte sizeBuff[4];
int buffSize = 0;


int recieveMessage(){

    // moveTo message = moveTo_init_zero;

    // pb_istream_t stream = pb_istream_from_buffer(buffer,message_length);

    return 0;
}


void setup() {
  Serial.begin(9600);
  while(!Serial){
  Serial.println("Hello World");
  }
}

void loop() {
  // first 4 bytes = number of bytes to expect
  if (Serial.available() >= 4 && buffSize == 0){
    // write first 4 bytes to  
    Serial.readBytes(sizeBuff, 4);
    buffSize = (sizeBuff[0] << 24) + (sizeBuff[1] << 16) + (sizeBuff[2] << 8) + sizeBuff[3];
    Serial.write(buffSize);
    buffSize = 0;
  }
}
