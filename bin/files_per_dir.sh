#!/bin/bash
du -a | cut -d/ -f2 | sort | uniq -c | sort -n
