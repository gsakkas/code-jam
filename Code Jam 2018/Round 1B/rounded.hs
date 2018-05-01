{-# OPTIONS_GHC -O2 -optc-O2 #-}
 
module Main where

import Data.Char (isSpace, isLetter)
import Data.List (sortOn)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Char8 as BSC


rnd :: Int -> Int -> Int
rnd x y | x * 100 `mod` y * 2 >= y = x * 100 `div` y + 1
        | otherwise                = x * 100 `div` y


extras :: Int -> Int -> Int -> Int
extras cnt n r = (rnd cnt n) * (r `div` cnt) + (rnd 1 n) * (r `mod` cnt)


maxq :: Int -> Int -> Int -> Int
maxq cnt n r
  | cnt > r = 1
  | rnd cnt n > cnt * 100 `div` n = cnt
  | otherwise = maxq (cnt + 1) n r


nextr :: Int -> Int -> Int -> [Int] -> [Int]
nextr cnt n ll acc
  | cnt < 0 = acc
  | rnd cnt n > cnt * 100 `div` n = nextr (cnt - 1) n cnt (cnt:acc)
  | otherwise = nextr (cnt - 1) n ll (ll:acc)


need :: [Int] -> [Int] -> Int -> Int -> [(Int, Int)] -> [(Int, Int)]
need [] _ _ _ acc = acc
need (l:ls) nxt n r acc
  | rnd l n < l * 100 `div` n + 1 = need ls nxt n r ((find_next l):acc)
  | otherwise = need ls nxt n r acc
    where find_next cnt
            | cnt > r = (n + 1, 0)
            | rnd (l + cnt) n > (l + cnt) * 100 `div` n = (cnt, (rnd (l + cnt) n) - (rnd l n))
            | otherwise = find_next (cnt + 1)


find_max :: [(Int, Int)] -> Int -> Int -> Int -> Int -> [Int] -> [Int]
find_max [] _ _ _ _ acc = acc
find_max (n:ns) max_quant n' r sm acc
  | r - need >= 0 = find_max ns max_quant n' (r-need) (sm + pc) (least:acc)
  | otherwise     = acc
    where need = fst n
          pc = snd n
          more = extras max_quant n' (r - need)
          least = (max more ((rnd 1 n') * (r - need))) + sm + pc


solve :: Int -> [Int] -> Int
solve n ls
  | rnd 1 n > 100 `div` n = sofar + least
  | otherwise = sofar + max least (maximum $ find_max needed max_quant n remaining 0 [0])
    where sofar = sum $ map (\x -> rnd x n) ls
          remaining = n - sum ls
          max_quant = maxq 1 n remaining
          nn = (maximum ls) + remaining + 1
          nxt = nextr (nn - 1) n nn []
          least = max (extras max_quant n remaining) ((rnd 1 n) * remaining)
          needed = sortOn fst $ need ls nxt n remaining []


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
     