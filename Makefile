
sha512-challenge : sha512-challenge.cu
	nvcc -O3 -arch=sm_30 sha512-challenge.cu -o sha512-challenge

clean :
	$(RM) sha512-challenge
