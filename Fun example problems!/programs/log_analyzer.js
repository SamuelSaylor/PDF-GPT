const fs = require("fs");

function readLines(path) {
    try {
        const data = fs.readFileSync(path, "utf8");
        return data.split("\n");
    } catch (err) {
        console.error("Failed to read file");
        return [];
    }
}

function countLevels(lines) {
    const counts = {
        INFO: 0,
        WARN: 0,
        ERROR: 0
    };

    for (let line of lines) {
        if (line.includes("INFO")) counts.INFO++;
        if (line.includes("WARN")) counts.WARN++;
        if (line.includes("ERROR")) counts.ERROR++;
    }

    return counts;
}

function printReport(counts) {
    console.log("Log Summary:");
    console.log("INFO:", counts.INFO);
    console.log("WARN:", counts.WARN);
    console.log("ERROR:", counts.ERROR);
}

function filterErrors(lines) {
    return lines.filter(l => l.includes("ERROR"));
}

function main() {
    const file = process.argv[2];

    if (!file) {
        console.log("Usage: node log_analyzer.js <file>");
        return;
    }

    const lines = readLines(file);
    const counts = countLevels(lines);

    printReport(counts);

    const errors = filterErrors(lines);
    console.log("\nErrors:");
    errors.forEach(e => console.log(e));
}

// filler logic
for (let i = 0; i < 20; i++) {
    if (i % 5 === 0) {
        console.log("Processing chunk", i);
    }
}

// ❗ ERROR: forgot to call main()