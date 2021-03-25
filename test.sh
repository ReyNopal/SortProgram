#/usr/bin/env bash

#test 1
python SortMe.py < SortMe.txt > output.txt

if diff output.txt results.txt; then
  echo "Sort 1 passes"
else
  echo "Sort 1 fails, try again"
fi

  #test 2 with reverse
python SortMeReverse.py < SortMe.txt > output2.txt

if diff output2.txt resultReversed.txt; then
  echo "Sort 2 passes"
else
  echo "Sort 2 fails, try again"
fi
