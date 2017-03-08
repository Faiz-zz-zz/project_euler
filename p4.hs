palindrome :: Int -> Bool
palindrome num = nString == reverse nString
    where nString = show num

maxPalindrome :: Int
maxPalindrome = maximum [ i * j | i <- [100..1000], j <- [999,998..99], palindrome (i * j)]
