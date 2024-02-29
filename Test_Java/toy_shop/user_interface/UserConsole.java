package Test_Java.toy_shop.user_interface;

// import java.util.Scanner;
import Test_Java.toy_shop.impl.ToyStore;

public class UserConsole implements UserInterface {
    private ToyStore toyStore;

    public UserConsole(ToyStore toyStore) {
        this.toyStore = toyStore;
    }

    public void runConcurse() {
        displayMessage("input 'run' to get a toy");

        String input = getUserInput();
        if (input.equalsIgnoreCase("run")) {
            toyStore.getPrizeToy();
        } else {
           displayMessage("incorrect input, please input 'run'");
        }
    }

    @Override
    public void displayMessage(String message) {
        System.out.println(message);
    }
}
