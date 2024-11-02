#!/bin/bash

for filename in ./*.stm; do
  receipt=$(cat $filename | egrep "Total Price")
  if [[ -n "$receipt" ]]; then
    mv $filename receipts/
  fi
done
