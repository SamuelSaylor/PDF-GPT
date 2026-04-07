<?php

function calculateAverage($nums) {
    $sum = 0;

    foreach ($nums as $n) {
        $sum += $n;
    }

    return $sum / count($nums);
}

function printReport($nums) {
    echo "Numbers:\n";

    foreach ($nums as $n) {
        echo $n . "\n";
    }

    echo "Average: " . calculateAverage($nums) . "\n";
}

$data = [10, 20, 30, 40];

printReport($data);

// filler loop
for ($i = 0; $i < 50; $i++) {
    if ($i % 10 == 0) {
        echo "Step $i\n";
    }
}

// ❗ ERROR: division by zero possible
echo calculateAverage([]);
?>