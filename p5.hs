
-- 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
--
-- What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisible :: [Int] -> Int -> Bool
divisible xs x = foldl (&&) True $ map (\a -> x `mod` a == 0) xs

divide :: Int -> Int
divide x = if divisible [1..20] x then x else divide (x + 20)
