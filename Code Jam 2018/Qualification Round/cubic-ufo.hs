{-# OPTIONS_GHC -O2 -optc-O2 #-}
 
module Main where

import Data.Char (isSpace)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Char8 as BSC

type Point = [Double]

solve :: Double -> [Point]
solve n = [fst_pt, snd_pt, thr_pt]
    where theta = pi / 4 + acos(n / sqrt(2))
          theta' = theta + pi / 2
          fst_pt = [0.5 * cos(theta), 0.5 * sin(theta), 0.0]
          snd_pt = [0.5 * cos(theta'), 0.5 * sin(theta'), 0.0]
          thr_pt = [0.0, 0.0, 0.5]

main =
  do all <- BS.getContents
     let Just (t, r1) = readInt all
     putStrLn $ enum 1 "" $ solveAll t (BSC.unpack r1)
  where enum _ acc [] = acc
        enum n acc (p:ps) =
          enum (n+1) (acc ++ "Case #" ++ (show n) ++ ":\n" ++ (f p) ++ "\n") ps
        f p = concat $ map (\y -> (concat $ map (\x -> show x ++ " ") y) ++ "\n") p
        readInt s = BSC.readInt (BSC.dropWhile isSpace s)
        readFloat s = reads s
        solveAll t s
          | t == 1    = [solve n]
          | otherwise = (solve n) : (solveAll (t-1) rest)
              where (n, rest) = head $ readFloat s
 
