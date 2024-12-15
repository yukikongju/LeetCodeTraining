CC = gcc
WFLAGS = -Wextra
EXECUTABLE = program


all: exec clean

exec: $(INPUT)
	$(CC) $(WFLAGS) -o $(EXECUTABLE) $(INPUT)
	./$(EXECUTABLE)

clean: 
	rm -f $(EXECUTABLE)

