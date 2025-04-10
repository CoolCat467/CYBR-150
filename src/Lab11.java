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

import java.util.Random;

public class Lab11 {
    public static void main(String[] args){
        double[] double_1d_array = make1DDoubleArray(10);
        print1DDoubleArray(double_1d_array);

        // double[][] double_2d_array = make2DDoubleArray(10, 10);
        // print2DDoubleArray(double_2d_array);

        int[][] int_2d_array = make2DIntegerArray(10, 10);
        print2DIntArray(int_2d_array);
    }

    public static double[] make1DDoubleArray(int length){
        Random rand = new Random();
        double[] array = new double[length];
        for (int i=0; i<length; i++){
            array[i] = rand.nextDouble();
        }
        return array;
    }

    public static double[][] make2DDoubleArray(int row, int col){
        Random rand = new Random();
        double[][] array = new double[row][col];
        for (int r=0; r<row; r++){
            for (int c=0; c<col; c++){
                array[r][c] = rand.nextDouble();
            }
        }
        return array;
    }

    public static int[][] make2DIntegerArray(int row, int col){
        Random rand = new Random();
        int[][] array = new int[row][col];
        for (int r=0; r<row; r++){
            for (int c=0; c<col; c++){
                array[r][c] = rand.nextInt(99);
            }
        }
        return array;
    }


    public static void print1DDoubleArrayNoHeader(double[] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            System.out.printf("%.2f", sequence[i]);
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    public static void print1DDoubleArray(double[] sequence){
        System.out.println("***** Printing 1d double array *****\n");
        print1DDoubleArrayNoHeader(sequence);
    }

    public static void print2DDoubleArrayNoHeader(double[][] sequence){
        System.out.print("[\n");
        for (int i=0; i<sequence.length; i++){
            System.out.print("  ");
            print1DDoubleArrayNoHeader(sequence[i]);
        }
        System.out.println("]");
    }

    public static void print2DDoubleArray(double[][] sequence){
        System.out.println("***** Printing 2d double array *****\n");
        print2DDoubleArrayNoHeader(sequence);
    }

    public static void print1DIntArrayNoHeader(int[] sequence){
        print(sequence);
    }

    public static void print1DIntArray(int[] sequence){
        System.out.println("***** Printing 1d int array *****\n");
        print1DIntArrayNoHeader(sequence);
    }

    public static void print2DIntArrayNoHeader(int[][] sequence){
        System.out.print("[\n");
        for (int i=0; i<sequence.length; i++){
            System.out.print("  ");
            print1DIntArrayNoHeader(sequence[i]);
        }
        System.out.println("]");
    }

    public static void print2DIntArray(int[][] sequence){
        System.out.println("***** Printing 2d int array *****\n");
        print2DIntArrayNoHeader(sequence);
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
