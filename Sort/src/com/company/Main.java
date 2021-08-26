package com.company;
import java.util.ArrayList;
import java.util.Scanner;

import algorithms.selectionSort;

public class Main {

// ArrayList<type>n = new ArrayList<type>();
// n.add(n);
// n.set(pos, newValue);
// n.get(pos)
// n.remove(pos)
// n.clear()
// n.size()

    public static void main(String[] args) {
        ArrayList<Integer>arr = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        int n;

        do{
            System.out.print("Enter a number: ");
            n = scanner.nextInt();
            arr.add(n);
        }while(n!=0);

        System.out.println(selectionSort.sort(arr));
    }

}
