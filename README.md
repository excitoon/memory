# `memory`

[![Black](https://github.com/excitoon/memory/actions/workflows/black.yml/badge.svg)](https://github.com/excitoon/memory/actions/workflows/black.yml)
[![Linux](https://github.com/excitoon/memory/actions/workflows/ubuntu.yml/badge.svg)](https://github.com/excitoon/memory/actions/workflows/ubuntu.yml)
[![OS X](https://github.com/excitoon/memory/actions/workflows/macos.yml/badge.svg)](https://github.com/excitoon/memory/actions/workflows/macos.yml)
[![Windows](https://github.com/excitoon/memory/actions/workflows/windows.yml/badge.svg)](https://github.com/excitoon/memory/actions/workflows/windows.yml)
[![PyPI](https://badge.fury.io/py/memory-py.svg)](https://badge.fury.io/py/memory-py)

Approximate memory usage profiler.

## Usage

```
memory 3 ~/ClickHouse
```

Output:

```
...

15037 directories, 199616 files

rss          7M     10M     10M     10M     10M     11M     12M     12M     12M     13M     16M
vms         25M     27M     27M     27M     27M     28M     29M     29M     29M     30M     32M
shared       5M      5M      5M      5M      5M      5M      5M      5M      5M      5M      5M
text         2M      2M      2M      2M      2M      2M      2M      2M      2M      2M      2M
lib          0M      0M      0M      0M      0M      0M      0M      0M      0M      0M      0M
data         3M      5M      5M      5M      5M      6M      6M      7M      7M      7M     10M
dirty        0M      0M      0M      0M      0M      0M      0M      0M      0M      0M      0M
```

## Install

```
pip3 install memory-py
```
