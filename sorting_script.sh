#!/bin/bash
for filename in SMA_Hackathon/*.stm; do
  pid=${filename: -8:-4}
  echo $pid
  mkdir -p sorted_data/$pid && cp $filename sorted_data/$pid
done
