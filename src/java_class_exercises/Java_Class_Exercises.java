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


public class Java_Class_Exercises {
    public static void main(String[] args){
        Triangle triangle = new Triangle(3, 4);
        // Triangle triangle = new Triangle();
        System.out.println(triangle);

        Rectangle rectangle = new Rectangle(3, 4);
        System.out.println(rectangle);

        User user = new User("Jerald", "Perchance", "Jason", 1744901965);
        System.out.println(user);

        Employee employee = new Employee("Business", "Michael", "Mister", 1744902514, 27, "email_address@example.com");
        System.out.println(employee);

        Animal animal = new Animal("Cat", 4, 17, "Pounce De Leon");
        System.out.println(animal);

        House house = new House(7, 4, 125010, 32518.32);
        System.out.println(house);
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
