{-# OPTIONS_GHC -O2 -optc-O2 #-}
 
module Main where

import Data.Char (isSpace, isLetter)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Char8 as BSC
import Data.List (dropWhileEnd, span)

damage :: [Char] -> Int
damage "" = 0
damage (p:ps)
  | p == 'C'  = 2 * damage ps
  | otherwise = 1 + damage ps

changeOne :: [Char] -> [Char]
changeOne p = hd' ++ [tlhd] ++ hdtl ++ tl'
  where p' = dropWhile (=='C') p
        (hd, tl) = span (=='S') p'
        (hd', hdtl) = splitAt ((length hd) - 1) hd
        (tlhd:tl') = tl

impossible :: [Char] -> Int
impossible p = length $ filter (=='S') p

solve :: Int -> [Char] -> Int -> Int
solve d "" res = res
solve d p res 
  | (impossible p) > d = -1
  | damage (reverse p) <= d = res
  | otherwise = solve d (changeOne p) (res+1)

main =
  do all <- BS.getContents
     let Just (t, r1) = readInt all
     putStrLn $ enum 1 "" $ solveAll t r1
  where enum _ acc [] = acc
        enum n acc (p:ps) =
          enum (n+1) (acc ++ "Case #" ++ (show n) ++ ": " ++ (f p) ++ "\n") ps
        f n = if n < 0 then "IMPOSSIBLE" else show n
        readInt s = BSC.readInt (BSC.dropWhile isSpace s)
        readMany s = BSC.span isLetter (BSC.dropWhile isSpace s)
        solveAll t s
          | t == 1    = [solve d p' 0]
          | otherwise = (solve d p' 0) : (solveAll (t-1) rest)
              where Just (d, r2) = readInt s
                    (p, rest) = readMany r2
                    p' = reverse $ dropWhileEnd (=='C') $ BSC.unpack p
     