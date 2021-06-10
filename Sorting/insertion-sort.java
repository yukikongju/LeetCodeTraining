public class Insertion{
    public static void main(Comparable[] array){
	for(int i=0; i<array.length; i++){
	    for(int j=i; j>0; j--){
		if(less(array[j], array[j-1]))
		    exch(array, j, j-1);
		else break;
	    }
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

