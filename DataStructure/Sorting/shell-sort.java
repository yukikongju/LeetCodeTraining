public class ShellSort{
    public static void main(Comparable[] array){
	int h =1;
	int length = array.length;
	while(h< N/3) h=3*h +1;
	while(h>=1){
	    for(int i=h; i<length; i++){
		for(int j=i; j>= h && less(array[j], array[j-h]; j-=h))
		    exch(array, j, j-h);
	    }
	    h = h/3;
	}
    }

    private static void less(Comparable item1, Comparable item2){
	return item1.compareTo(item2) < 0;
    }

    private static void exch(Comparable[] array, int i, int j){
	int temp = array[i];
	array[i] = array[min];
	array[min] = temp;
    }
}
