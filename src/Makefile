
tests: windows.o main.o
	g++ -lglfw3 -lopengl32 -lgdi32 windows.o main.o -o app.exe

main.o: main.cpp main.h
	g++ -c main.cpp

windows.o: windows.cpp
	g++ -c windows.cpp

libraries: 

clean:
	rm *.o tests
