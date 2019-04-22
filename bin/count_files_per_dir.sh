#!/bin/bash
find . -type d -print0 | while read -d '' -r dir; do
    files=("$dir"/*)
    printf "%d %s\n" "${#files[@]}" "$dir"
done


