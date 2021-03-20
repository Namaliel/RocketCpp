
tests: windows.o main.o
	g++  windows.o main.o -o app.exe

main.o: main.cpp
	g++ -c main.cpp

windows.o: windows.cpp
	g++ -c windows.cpp 

LDLIBS += -lglfw3 -lopengl32 -ldi32

clean:
	rm *.o tests
