package Test_Java.toy_shop.user_interface;

import java.util.Scanner;

public interface UserInterface {
    default String getUserInput() {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        scanner.close();
        return input;
    }
    void displayMessage(String message);
}
