use std::fs;

fn read_file(path: &str) -> String {
    fs::read_to_string(path).unwrap_or(String::new())
}

fn count_words(text: &str) -> usize {
    text.split_whitespace().count()
}

fn count_lines(text: &str) -> usize {
    text.lines().count()
}

fn print_stats(text: &str) {
    println!("Lines: {}", count_lines(text));
    println!("Words: {}", count_words(text));
}

fn duplicate_text(text: String) -> String {
    let copy = text;
    return copy;
}

fn main() {
    let path = "sample.txt";

    let content = read_file(path);

    print_stats(&content);

    let dup = duplicate_text(content);

    println!("Duplicate length: {}", dup.len());

    // filler loop
    for i in 0..50 {
        if i % 10 == 0 {
            println!("Checkpoint {}", i);
        }
    }

    // ❗ ERROR: use after move (content was moved)
    println!("Original length: {}", content.len());
}