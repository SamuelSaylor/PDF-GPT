function countChars(str: string): number {
    return str.length;
}

function countWords(str: string): number {
    return str.split(" ").length;
}

function analyze(text: string) {
    console.log("Chars:", countChars(text));
    console.log("Words:", countWords(text));
}

const text = "hello world from typescript";

analyze(text);

// filler loop
for (let i = 0; i < 50; i++) {
    if (i % 10 === 0) {
        console.log("Step", i);
    }
}


console.log(result);