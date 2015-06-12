#include <bcm2835.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include "tft.h"
#include "RAIO8870.h"
//#include "bmp.h"
//#include "examples.h"

int init();
void release();
void loadBuffer(uint8_t* buf);
