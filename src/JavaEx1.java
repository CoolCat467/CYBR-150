import java.util.Scanner;

public class JavaEx1 {
    public static void main(String[] args){
        System.out.println("Hello wurld");

        char val1 = 'a';
        char val2 = 'b';
        char val3 = 'c';

        System.out.println(val1);
        System.out.println(val2);
        System.out.println(val3);

        int age1, age2, age3;
        age1 = -3;
        age2 = 6;
        age3 = 9;

        System.out.println(age1);
        System.out.println(age2);
        System.out.println(age3);

        double pct1, pct2, pct3;
        pct1 = 3.14;
        pct2 = 2.85;
        pct3 = 0.01;

        System.out.println(pct1);
        System.out.println(pct2);
        System.out.println(pct3);

        boolean check1, check2, check3;
        check1 = true;
        check2 = false;
        check3 = true;

        System.out.println(check1);
        System.out.println(check2);
        System.out.println(check3);

        String input1, input2, input3;
        input1 = "this is text";
        input2 = "you understand, mechanical hands, are the ruler of everything";
        input3 = "Добрый вечер";

        System.out.println(input1);
        System.out.println(input2);
        System.out.println(input3);

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first name: ");
        String firstName = scanner.nextLine();

        System.out.print("Enter last name: ");
        String lastName = scanner.nextLine();

        String fullName = firstName + ' ' + lastName;

        System.out.print("Enter age: ");
        int age = scanner.nextInt();

        System.out.println(fullName);

        // System.out.printf("Full name: %s\n", full_name);


        double height, depth, length;
        System.out.print("Enter height: ");
        height = scanner.nextDouble();
        System.out.print("Enter depth: ");
        depth = scanner.nextDouble();
        System.out.print("Enter length: ");
        length = scanner.nextDouble();
        double area = height * depth * length;
        if (area > 50.0f){
            System.out.printf("Area: %f\n", area);
        } else {
            System.out.println("Error.");
        }


        int value1, value2, value3;
        System.out.print("Enter value 1: ");
        value1 = scanner.nextInt();
        System.out.print("Enter value 2: ");
        value2 = scanner.nextInt();
        System.out.print("Enter value 3: ");
        value3 = scanner.nextInt();

        if (value1 > 10 && value2 > 10 && value3 > 10){
            System.out.println("Big numbers.");  //big boi kekw
        }
        if (value1 > 7 && value2 > 7){
            System.out.println("Two medium numbers.");
        }
        if (value1 > 10 || value2 > 10 || value3 > 10){
            System.out.println("One big number.");
        }
        if (value1 > 10 || value2 > 10){
            System.out.println("Two big numbers.");
        }



        System.out.print("Enter income: ");
        double income = scanner.nextDouble();
        double tax = 0.50;
        if (income < 5_000.00){
            tax = 0.02;
        } else if (income < 15_000.00){
            tax = 0.05;
        } else if (income < 50_000.00){
            tax = 0.10;
        } else if (income < 95_000.00){
            tax = 0.20;
        }
        System.out.printf("Tax payment: %f\n", income * tax);


        boolean exit = false;
        while (!exit){
            System.out.print("Enter `True` or `False`: ");
            exit = scanner.nextLine().equals("True");
        }
        System.out.println("Exit!");


        boolean valid = false;
        while (!valid){
            System.out.print("Enter `yes` or `no`: ");
            input1 = scanner.nextLine();
            valid = input1.equals("yes") || input1.equals("no");
        }


        int factorial = 1, numLoops;
        System.out.print("Enter number for factorial: ");
        numLoops = scanner.nextInt();
        for (int i = numLoops; i>1; i--){
            factorial *= i;
        }
        System.out.printf("Factorial: %d\n", factorial);


        System.out.println(addNums(27, 94));


        int[] ints = new int[10];
        int[] nums = new int[75];
        for (int i=0; i<nums.length; nums[i] = i++);
        print(ints);
        print(nums);
        String[] names = new String[4];
        System.out.println("Press enter to continue");
        scanner.nextLine();
        for (int i=0; i<names.length; i++){
            System.out.printf("Enter name %d: ", i);
            names[i] = scanner.nextLine();
        }
        print(names);
        int[] smallNums = new int[50];
        for (int i=0; i<smallNums.length; smallNums[i++] = i / 10);
        print(smallNums);


        printWelcome();
        System.out.println(printGoodbye("this is text"));
        System.out.println(getUsername(scanner));
        System.out.println(sumNums(3.14, 0.06, 0.8));
        System.out.println(fact(5));
        System.out.println(avgNums(nums));
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

    public static int addNums(int first, int second){
        return (first + second) * second;
    }

    public static void printWelcome(){
        System.out.println("Welcome!");
    }
    public static String printGoodbye(String prompt){
        System.out.println(prompt);
        System.out.println("Welcome!");
        return "Done";
    }
    public static String getUsername(Scanner scanner){
        System.out.print("Enter username: ");
        return scanner.nextLine();
    }
    public static double sumNums(double a, double b, double c){
        return a+b+c;
    }
    public static int fact(int n){
        int value = 0;
        for (int i=n; i>1; i--){
            value *= i;
        }
        return value;
    }
    public static double avgNums(int[] sequence){
        int sum = 0;
        for (int i=0; i<sequence.length; i++){
            sum += sequence[i];
        }
        return sum / ((double) sequence.length);
    }
}
