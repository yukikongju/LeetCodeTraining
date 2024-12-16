EXECUTABLE = program

all: exec clean

exec: $(INPUT)
	gcc -Wextra -o $(EXECUTABLE) $(INPUT)
	./$(EXECUTABLE)

clean: 
	rm -f $(EXECUTABLE)
