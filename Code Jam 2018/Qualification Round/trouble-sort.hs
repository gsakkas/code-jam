{-# OPTIONS_GHC -O2 -optc-O2 #-}
 
module Main where

import Data.Char (isSpace)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Char8 as BSC
import Data.List (sort, findIndex)

solve :: Int -> [(Int, Int)] -> Int
solve d [] = -1
solve d p = case findIndex (==True) $ zipWith (/=) orig trouble of
    Just a  -> a
    Nothing -> -1
  where os = sort $ map snd $ odds p
        es = sort $ map snd $ evens p
        orig = sort $ map snd $ p
        trouble = merge es os

enumerate :: [Int] -> [(Int, Int)]
enumerate = zip [0..]

evens :: [(Int, Int)] -> [(Int, Int)]
evens = filter (even.fst)

odds :: [(Int, Int)] -> [(Int, Int)]
odds = filter (odd.fst)

merge :: [Int] -> [Int] -> [Int]
merge xs     []     = xs
merge []     ys     = ys
merge (x:xs) (y:ys) = x : y : merge xs ys

main =
  do all <- BS.getContents
     let Just (t, r1) = readInt all
     putStrLn $ enum 1 "" $ solveAll t r1
  where enum _ acc [] = acc
        enum n acc (p:ps) =
          enum (n+1) (acc ++ "Case #" ++ (show n) ++ ": " ++ (f p) ++ "\n") ps
        f n = if n < 0 then "OK" else show n
        readInt s = BSC.readInt (BSC.dropWhile isSpace s)
        readMany 0 readf s = ([], (BSC.dropWhile isSpace s))
        readMany n readf s = case readf s of
            Just (x, r) -> let (xs, rest) = readMany (n-1) readf r
                           in  (x:xs, rest)
            Nothing     -> ([], (BSC.dropWhile isSpace s))
        solveAll t s
          | t == 1    = [solve n p']
          | otherwise = (solve n p') : (solveAll (t-1) rest)
              where Just (n, r2) = readInt s
                    (p, rest) = readMany n readInt r2 
                    p' = enumerate p
