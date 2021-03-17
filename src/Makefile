
tests: windows.o main.o
	g++ windows.o main.o -o tests

main.o: main.cpp main.h
	g++ -c main.cpp

windows.o: windows.cpp windows.h
	g++ -c windows.cpp

clean:
	rm *.o tests
