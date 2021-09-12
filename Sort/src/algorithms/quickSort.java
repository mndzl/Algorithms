package algorithms;

import java.util.ArrayList;

public class quickSort {
    public static ArrayList<Integer>array;

    public static ArrayList<Integer> sort(ArrayList<Integer>array, int begin, int end){
        if (begin<end) {
            int pivot = partition(begin, end, array);

            array = sort(array, begin, pivot - 1);
            array = sort(array, pivot + 1, end);
        }

        return array;
    }

    private static int partition(int begin, int end, ArrayList<Integer>arr){
        int pivot = arr.get(end);
        int i = begin-1;

        for(int j=begin; j<end-1; j++){
            if (arr.get(j)<=pivot){
                i++;
                if(i!=j)arr = swap(arr,i,j);
            }
        }

        arr = swap(arr, i+1, end);

        array = arr;

        pivot = i+1;

        return pivot;
    }


    private static ArrayList<Integer> swap(ArrayList<Integer>array, int i, int j){
        int aux = array.get(i);
        array.set(i, array.get(j));
        array.set(j, aux);
        return array;
    }
}
