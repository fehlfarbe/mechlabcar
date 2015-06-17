#include "libcberry.h"


int init(){
	if (!bcm2835_init())
		return 1;

	TFT_init_board();
	TFT_hard_reset();
	RAIO_init();

	return 0;
}

void release(){
    bcm2835_close();
}

void loadBuffer(uint8_t* buf){
	int i;
	uint8_t r, g, b;
	uint16_t color;
	uint16_t picture[PICTURE_PIXELS];
	for(i=0; i<PICTURE_PIXELS*3; i+=3){
		r = buf[i];
		g = buf[i+1];
		b = buf[i+2];
		#ifdef CM_65K
			color = (r >> 3);
			color = color << 6;
			color = color | (g >> 2);
			color = color << 5;
			color = color | (b >> 3);
		#elif defined(CM_4K)
			color = ( r >> 4 );
			color = color << 4;
			color = color | ( g >> 4);
			color = color << 4;
			color = color | (b >> 4);
		#endif
		picture[i/3] = color;
	}

	RAIO_Write_Picture ( picture, PICTURE_PIXELS );
}

void drawString( int x, int y, unsigned char *str, uint8_t BG_color, uint8_t FG_color ){
	RAIO_print_text( (uint16_t)x, (uint16_t)y, str, BG_color, FG_color );
}

int main(int argc, char** args){
	int i;
	uint8_t buf[PICTURE_PIXELS*3];
	for(i=0; i<PICTURE_PIXELS*3; i++){
		buf[i] = 0;
	}

	init();
	loadBuffer(buf);
	delay(5000);
	drawString(0, 0, "Hallo", 0, 255);
	delay(5000);
	release();

	return 0;
}
