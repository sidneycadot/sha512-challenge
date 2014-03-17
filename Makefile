
# Architecture can be
#
# sm_20
# sm_21   560 Ti card
# sm_30   GTX Titan card
# sm_35   GTX Titan card

GPU_ARCH=sm_21

sha512-challenge : sha512-challenge.cu
	nvcc -O3 -arch=$(GPU_ARCH) sha512-challenge.cu -o sha512-challenge

clean :
	$(RM) sha512-challenge
