// Copyright (C) 2025  CoolCat467
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

import java.util.Scanner;

public class Lab13 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        // Step 1 = Create an integer called peopleNum and set it to 3
        int peopleNum = 3;
        // Step 2 = Create a Person array called people and set it to a size of
        Person[] people = createPeople(peopleNum);
        // Step 3 = Create a for loop that counts from 0 to peopleNum
        for (int i=0;i<people.length;i++){
            addPerson(people, i, scanner);
        }
        // Step 4 = In the loop, call addPerson with the Person array and the value of i
        // --> Go to studentHandler
        // Step 7 = Call printPeople with the people array
        printPeople(people);
    }

    public static String input(String prompt, Scanner scanner){
        System.out.print(prompt+": ");
        return scanner.nextLine();
    }

    public static int input_int(String prompt, Scanner scanner){
        System.out.print(prompt+": ");
        int value = scanner.nextInt();
        scanner.nextLine();
        return value;
    }

    public static double input_double(String prompt, Scanner scanner){
        System.out.print(prompt+": ");
        double value = scanner.nextDouble();
        scanner.nextLine();
        return value;
    }

    public static void addPerson(Person[] people, int position, Scanner scanner) {
        String choice = getChoice(scanner);
        if(choice.equals("s")) {
            studentHandler(people, position, scanner);
        } else if (choice.equals("e")) {
            employeeHandler(people, position, scanner);
        } else {
            System.out.println("Error!");
        }
    }

    public static void printPeople(Person[] people) {
        int length = people.length;
        for(int i = 0; i < length; i++) {
            System.out.print("\n********** NEW PERSON ***********\n");
            System.out.println(people[i]);
            System.out.println("\n********** END PERSON ***********\n");
        }
    }

    public static void studentHandler(Person[] people, int position, Scanner scanner) {
        String first = input("\n\tEnter first name", scanner);
        String last = input("\tEnter Last name", scanner);
        String degree = input("\tEnter Degree", scanner);
        int num = input_int("\tEnter Student number", scanner);
        // Step 5 = Create a new Student object with first, last, degree and num
        people[position] = new Student(first, last, degree, num);
        //and set into the people array at position
        // --> Go to employeeHandler
    }

    public static void employeeHandler(Person[] people, int position, Scanner scanner) {
        String first = input("\n\tEnter first name", scanner);
        String last = input("\tEnter Last name", scanner);
        String title = input("\tEnter Title", scanner);
        double sal = input_double("\tEnter Employee salary", scanner);
        // Step 6 = Create a new Employee object with first, last, title and
        // sal and set into the people array at position
        people[position] = new Employee(first, last, title, sal);
    }

    public static String getChoice(Scanner scanner) {
        while(true) {
            String choice = input("\nEnter a Student or Employee(s for student, e for employee)? ", scanner);

            if (checkInput(choice)){
                if (choice.equalsIgnoreCase("s")) {
                    return "s";
                } else if (choice.equalsIgnoreCase("e")) {
                    return "e";
                }
            }
            System.out.println("Please enter either e or s!");
        }
    }

    public static boolean checkInput(String user_input) {
        return user_input.equalsIgnoreCase("s") || user_input.equalsIgnoreCase("e");
    }

    public static Person[] createPeople(int size) {
        return new Person[size];
    }

    public static void print(int[] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            System.out.printf("%d", sequence[i]);
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    public static void print(double[] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            System.out.printf("%f", sequence[i]);
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    public static void print(String[] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            System.out.printf("\"%s\"", sequence[i]);
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
