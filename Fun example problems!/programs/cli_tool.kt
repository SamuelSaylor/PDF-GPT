fun sum(nums: List<Int>): Int {
    var total = 0
    for (n in nums) {
        total += n
    }
    return total
}

fun printMenu() {
    println("1. Sum")
    println("2. Exit")
}

fun main() {
    val nums = listOf(1, 2, 3, 4, 5)

    while (true) {
        printMenu()
        val choice = readLine()

        if (choice == "1") {
            println("Sum: ${sum(nums)}")
        } else if (choice == "2") {
            break
        } else {
            println("Invalid")
        }

        // filler
        for (i in 0..40) {
            if (i % 8 == 0) {
                println("Tick $i")
            }
        }
    }
}