#!/bin/bash

for filename in ./*.stm; do
  eod_report=$(cat $filename | egrep "END OF DAY REPORT")
  if [[ -n "$eod_report" ]]; then
    cp $filename eod_reports/
  fi
done
