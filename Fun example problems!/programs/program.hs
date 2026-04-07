square x = x * x

sumList [] = 0
sumList (x:xs) = x + sumList xs

printList [] = return ()
printList (x:xs) = do
    print x
    printList xs

loop n = do
    if n > 50
        then return ()
        else do
            if mod n 10 == 0
                then print n
                else return ()
            loop (n + 1)

main = do
    let nums = [1,2,3,4,5]

    printList nums

    print (sumList nums)

    mapM_ (print . square) nums

    loop 0