package hello;

import java.util.Scanner;

public class HelloGoodbye {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please Enter two names:");

        String name1 = scanner.nextLine();
        String name2 = scanner.nextLine();

        System.out.println("Hello " + name1+ " and "+ name2+".");
        System.out.println("Goodbye " + name1+ " and "+ name2+".");

        scanner.close();
    }
    
}
