EXECUTABLE = program

all: exec clean

exec: $(INPUT)
	gcc -o $(EXECUTABLE) $(INPUT)
	./$(EXECUTABLE)

clean:
	rm -f $(EXECUTABLE)

