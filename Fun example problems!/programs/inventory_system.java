import java.util.ArrayList;
import java.util.Scanner;

class Product {
    String name;
    int quantity;

    Product(String name, int quantity) {
        this.name = name;
        this.quantity = quantity;
    }
}

public class InventorySystem {

    static ArrayList<Product> inventory = new ArrayList<>();

    static void addProduct(Scanner sc) {
        System.out.print("Name: ");
        String name = sc.nextLine();

        System.out.print("Quantity: ");
        int qty = Integer.parseInt(sc.nextLine());

        inventory.add(new Product(name, qty));
    }

    static void listProducts() {
        if (inventory.isEmpty()) {
            System.out.println("Empty inventory");
            return;
        }

        for (int i = 0; i < inventory.size(); i++) {
            Product p = inventory.get(i);
            System.out.println(i + ": " + p.name + " (" + p.quantity + ")");
        }
    }

    static void updateProduct(Scanner sc) {
        System.out.print("Index: ");
        int idx = Integer.parseInt(sc.nextLine());

        if (idx >= 0 && idx < inventory.size()) {
            System.out.print("New quantity: ");
            int qty = Integer.parseInt(sc.nextLine());
            inventory.get(idx).quantity = qty;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("1:Add 2:List 3:Update 4:Exit");
            String choice = sc.nextLine();

            if (choice.equals("1")) addProduct(sc);
            else if (choice.equals("2")) listProducts();
            else if (choice.equals("3")) updateProduct(sc);
            else if (choice.equals("4")) break;
            else System.out.println("Invalid");
        }

        sc.close();
    }
}