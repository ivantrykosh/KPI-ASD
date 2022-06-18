import java.util.Scanner;
public class LabaOP {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Введіть а: ");
        double a = in.nextDouble();
        double d = a * Math.sqrt(2);
        double P = a * 4;
        double S = a * a;
        System.out.printf("Діагональ = %.6f, периметр = %.6f, площа = %.6f.", d, P, S);
    }
}
