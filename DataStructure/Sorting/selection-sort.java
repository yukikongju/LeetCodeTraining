public class Selection {
    public static void selectionSort(Comparable[] array){
	for(int i=0; i< array.length - 1; i++){
	    int min = i;
	    for(int j = i+1; j< array.length; j++){
		if(less(array[j], array[min])){
		    min = j;
		}
		exch(array, i, min);
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
