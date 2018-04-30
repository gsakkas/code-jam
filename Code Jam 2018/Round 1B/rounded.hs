{-# OPTIONS_GHC -O2 -optc-O2 #-}
 
module Main where

import Data.Char (isSpace, isLetter)
import Data.List (sortOn)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Char8 as BSC


rnd :: Int -> Int -> Int
rnd x y | x * 100 `mod` y * 2 >= y = x * 100 `div` y + 1
        | otherwise                = x * 100 `div` y


extras :: Int -> Int -> Int -> [Int] -> [Int]
extras cnt n r acc
  | cnt < 1 = acc
  | rnd cnt n > cnt * 100 `div` n = extras (cnt - 1) n r ((mx):acc)
  | otherwise = extras (cnt - 1) n r acc
    where mx = (rnd cnt n) * (r `div` cnt) + (rnd 1 n) * (r `mod` cnt)


need :: [Int] -> Int -> Int -> [(Int, Int)] -> [(Int, Int)]
need [] _ _ acc = acc
need (l:ls) n r acc 
  | rnd l n < l * 100 `div` n + 1 = need ls n r ((find_next 1):acc)
  | otherwise = need ls n r acc
    where find_next cnt
            | cnt > r = (n + 1, 0)
            | rnd (l + cnt) n > (l + cnt) * 100 `div` n = (cnt, (rnd (l + cnt) n) - (rnd l n))
            | otherwise = find_next (cnt + 1)


find_max :: [(Int, Int)] -> Int -> Int -> Int -> [Int] -> [Int]
find_max [] _ _ _ acc = acc
find_max (n:ns) n' r sm acc
  | r - need >= 0 = find_max ns n' (r-need) (sm + pc) (least:acc)
  | otherwise     = acc
    where need = fst n
          pc = snd n
          more = maximum $ extras (r - need) n' (r - need) [0]
          least = (max more ((rnd 1 n') * (r - need))) + sm + pc


solve :: Int -> [Int] -> Int
solve n ls = sofar + max least (maximum $ find_max needed n remaining 0 [0])
  where sofar = sum $ map (\x -> rnd x n) ls
        remaining = n - sum ls
        all_new = maximum $ extras remaining n remaining [0]
        least = max all_new ((rnd 1 n) * remaining)
        needed = sortOn fst $ need ls n remaining []


main =
  do all <- BS.getContents
     let Just (t, r1) = readInt all
     putStr $ enum 1 "" $ solveAll t r1
  where enum _ acc [] = acc
        enum n acc (p:ps) =
          enum (n+1) (acc ++ "Case #" ++ (show n) ++ ": " ++ (show p) ++ "\n") ps
        readInt s = BSC.readInt (BSC.dropWhile isSpace s)
        readMany 0 s = ([], (BSC.dropWhile isSpace s))
        readMany l s = case readInt s of
            Just (x, r) -> let (xs, rest) = readMany (l-1) r
                           in  (x:xs, rest)
            Nothing     -> ([], (BSC.dropWhile isSpace s))
        solveAll t s
          | t == 1    = [solve n ls]
          | otherwise = (solve n ls) : (solveAll (t-1) rest)
              where Just (n, r2) = readInt s
                    Just (l, r3) = readInt r2
                    (ls, rest) = readMany l r3
     