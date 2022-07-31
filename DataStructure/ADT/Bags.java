#!/usr/bin/java

public class Bag implements Iterable{
  private Object[] elements;
  private int size; // size saw by user
  private static final int DEFAULT_CAPACITY = 1; // capacity stored in memory

  // initialize Bag
  private Bag(){this(DEFAULT_CAPACITY);}
  private Bag(int capacity){elements = new Object[capacity]; size = 0;}

  // add element in Bag
  private void add(Object object){
	if(size == element.length) reallocation(2*size); // double size if capacity reached
	elements[size++] = object; // add object to bag
  }

  private void reallocation(int newSize){
	// transfer old elements in bigger array when capacity has been reached
	Object[] temp = new Object[newSize];
	for(int i=0; i<elements.length; i++) temp[i] = elements[i];
	elements = temp;
  }
}
