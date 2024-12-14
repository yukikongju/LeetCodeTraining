EXECUTABLE = example

## Ex: make INPUT=1.c

all: exec clean

exec: $(INPUT)
	gcc -o $(EXECUTABLE) $(INPUT)
	./$(EXECUTABLE)

clean: 
	rm -f $(EXECUTABLE)
