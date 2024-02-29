package Test_Java.toy_shop;

import Test_Java.toy_shop.impl.Toy;
import Test_Java.toy_shop.impl.ToyStore;
import Test_Java.toy_shop.logger.Logger;
import Test_Java.toy_shop.logger.LoggerFile;
import Test_Java.toy_shop.user_interface.UserConsole;
import Test_Java.toy_shop.user_interface.UserInterface;


public class Runner {
    public static void main(String[] args) throws Exception {
        Logger logger = new LoggerFile("prize_toy.txt");
        ToyStore toyStore = new ToyStore(logger);

        toyStore.addToy(new Toy(1, "doll", 10, 20));
        toyStore.addToy(new Toy(2, "Typewriter", 8, 15));
        toyStore.addToy(new Toy(3, "Ball", 15, 25));

         UserInterface uInterface = new UserConsole(toyStore);
        ((UserConsole)uInterface).runConcurse();
    }
    
}
