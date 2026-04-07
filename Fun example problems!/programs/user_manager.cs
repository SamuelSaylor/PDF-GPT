using System;
using System.Collections.Generic;

class User {
    public string Name;
    public int Age;

    public User(string name, int age) {
        Name = name;
        Age = age;
    }
}

class Program {

    static List<User> users = new List<User>();

    static void AddUser() {
        Console.Write("Name: ");
        string name = Console.ReadLine();

        Console.Write("Age: ");
        int age = int.Parse(Console.ReadLine());

        users.Add(new User(name, age));
    }

    static void ListUsers() {
        if (users.Count == 0) {
            Console.WriteLine("No users.");
            return;
        }

        for (int i = 0; i < users.Count; i++) {
            Console.WriteLine($"{i}: {users[i].Name} ({users[i].Age})");
        }
    }

    static void Main() {
        while (true) {
            Console.WriteLine("1:Add 2:List 3:Exit");
            string choice = Console.ReadLine();

            if (choice == "1") AddUser();
            else if (choice == "2") ListUsers();
            else if (choice == "3") break;
            else Console.WriteLine("Invalid");

            // filler loop
            for (int i = 0; i < 20; i++) {
                if (i % 4 == 0) {
                    Console.WriteLine("Loop " + i);
                }
            }
        }
    }
}