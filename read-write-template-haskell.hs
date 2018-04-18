{-# OPTIONS_GHC -O2 -optc-O2 #-}
 
module Main where

import Data.Char (isSpace, isLetter)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Char8 as BSC

solve :: Int -> [Char] -> Int
solve 0 _ = -1
solve d _ = 10


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
        readFloat s = reads s
        solveAll t s
          | t == 1    = [solve d p']
          | otherwise = (solve d p') : (solveAll (t-1) rest)
              where Just (d, r2) = readInt s
                    (p, rest) = readMany r2
                    p' = BSC.unpack p
     