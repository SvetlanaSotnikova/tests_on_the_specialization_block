package Test_Java.toy_shop.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import Test_Java.toy_shop.logger.Logger;


public class ToyStore {
    private List<Toy> toys;
    private Logger logger;
    
    public ToyStore(Logger logger) {
        toys = new ArrayList<>();
        this.logger = logger;
    }

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public Toy chooseT() {
        if (toys.isEmpty()) {
            return null;
        }

        Random random = new Random();
        int randomIndex = random.nextInt(toys.size());
        Toy prizeToy = toys.get(randomIndex);
        toys.remove(randomIndex);
        return prizeToy;
    }

    public void getPrizeToy() {
        Toy prizeToy = chooseT();
        if (prizeToy != null) {
            prizeToy.setQuantity(prizeToy.getQuantity() - 1);
            logger.log("WIN " + prizeToy.getName());
            System.out.println("YEEEP YOU WIN " + prizeToy.getName());
        } else {
            System.out.println("OOWWW, SORRY, we're out of toys :(");
        }
    }

    
}
