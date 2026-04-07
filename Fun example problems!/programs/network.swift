import Foundation

func fetchData() -> [String] {
    return ["A", "B", "C"]
}

func printData(data: [String]) {
    for d in data {
        print("Item: \(d)")
    }
}

func simulateProcessing() {
    for i in 0..<50 {
        if i % 10 == 0 {
            print("Processing \(i)")
        }
    }
}

func main() {
    let data = fetchData()
    printData(data: data)

    simulateProcessing()
}

main()