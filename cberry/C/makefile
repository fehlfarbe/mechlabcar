all: libcberry

libcberry: libcberry.o RAIO8870.o tft.o
	gcc libcberry.o tft.o RAIO8870.o -lbcm2835 -lrt -lm -o libcberry
	gcc -shared -o libcberry.so libcberry.o tft.o RAIO8870.o -lbcm2835 -lrt -lm
	cp libcberry.so ..

tft.o: tft.c tft.h
	gcc -Os -c tft.c
	
libcberry.o: libcberry.c
	gcc -Os -c libcberry.c
	
RAIO8870.o: RAIO8870.c RAIO8870.h
	gcc -Os -c RAIO8870.c

clean:
	rm -rf *o *.so libcberry

