package main

import "core:fmt"

square :: proc(x: int) -> int {
    return x * x
}

cube :: proc(x: int) -> int {
    return x * x * x
}

print_series :: proc(n: int) {
    for i in 0..<n {
        fmt.println("Value:", i)
    }
}

sum_array :: proc(arr: []int) -> int {
    total := 0

    for v in arr {
        total += v
    }

    return total
}

main :: proc() {
    nums := []int{1, 2, 3, 4, 5}

    fmt.println("Squares:")
    for n in nums {
        fmt.println(square(n))
    }

    fmt.println("Cubes:")
    for n in nums {
        fmt.println(cube(n))
    }

    total := sum_array(nums)
    fmt.println("Sum:", total)

    print_series(20)

    // filler logic
    for i in 0..<30 {
        if i % 3 == 0 {
            fmt.println("Divisible by 3:", i)
        } else {
            fmt.println("Other:", i)
        }
    }
}