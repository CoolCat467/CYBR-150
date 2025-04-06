import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Lab10 {
    public static void main(String[] args){
        welcome();

        Scanner scanner = new Scanner(System.in);

        String filename = getFilename(scanner);
        File file = getFile(filename);

        printFile(file);
        addToFile(file, scanner);
        printFile(file);
    }

    public static void welcome(){
        System.out.println("Welcome to Lab 10!\n");
    }

    public static String input(String prompt, Scanner scanner){
        System.out.print(prompt+": ");
        return scanner.nextLine();
    }

    public static String getFilename(Scanner scanner){
        String result = input("Please enter a filename", scanner);
        System.out.println();
        return result;
    }

    public static File getFile(String filename){
        return new File(filename);
    }

    public static void printFile(File file){
        System.out.println("Printing\n");
        try {
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()){
                System.out.println(reader.nextLine());
            }
            reader.close();
        } catch (FileNotFoundException exc) {
            System.out.println("File not found.");
            System.out.println(exc);
        }
        System.out.println();
    }

    public static void addToFile(File file, Scanner scanner){
        String shouldAdd = input("Would you like to add to the file? 1 for yes 0 for no", scanner);
        if (!shouldAdd.equals("1")){
            return;
        }
        String value = input("What would you like to add", scanner);
        try {
            FileWriter writer = new FileWriter(file, true);
            writer.append("\n");
            writer.append(value);
            writer.close();
        } catch (FileNotFoundException exc) {
            System.out.println("File not found.");
            System.out.println(exc);
        } catch (IOException exc) {
            System.out.println("IO error.");
            System.out.println(exc);
        }
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
