#!/usr/bin/java

public Stack{
  private Object[] elements;
  private int top;
  private static final DEFAULT_CAPACITY = 1;

  // init
  private Bag(){this(DEFAULT_CAPACITY);}
  private Bag(int capacity){elements = new Object[capacity]; top = 0;}

  // push
  private void push(Object object){
	if(top == elements.length) realloc(2*elements.length);
	elements[top++] = object;
  }

  private void realloc(int newSize){
	Object[] temp = new Object[newSize];
	for(int i=0; i<elements.length; i++) temp[i] = elements[i];
	elements = temp;
  }

  // pop
  private void pop(){
	Object lastElement = elements[top];
	top--;
	elements[top] = null;
	if(top < elements.length / 4) realloc(elements.length /2);
	return lastElement;
  }
}
