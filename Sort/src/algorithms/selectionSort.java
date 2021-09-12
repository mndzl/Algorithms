package algorithms;
import java.util.ArrayList;

public class selectionSort {

    public static ArrayList<Integer> sort(ArrayList<Integer>array){

        // Through every element in array
        for(int i=0; i<array.size()-1; i++){
            // set next element as min
            int min = i;
            // find min element starting from i
            for(int j=i+1; j<array.size(); j++)
                // When found...
                if (array.get(j) < array.get(min))
                    // set that index as new min
                    min = j;

            // if a min is found, swap with i element which is current being analyzed
            if(min>=0)
                array = swap(min,i, array);
        }

        return array;
    }

    // Swaps elements i and j in array given
    public static ArrayList<Integer> swap(int i, int j, ArrayList<Integer>a){
        int aux = a.get(i);
        a.set(i, a.get(j));
        a.set(j, aux);

        return a;

    }

}
