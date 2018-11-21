# Description

This script will check CDP(s) of [DAI stablecoin](https://makerdao.com/dai) for collateral requirements.

# Installation

Clone and setup [pymaker](https://github.com/makerdao/pymaker) according to official instructions and copy the script to pymaker directory (if you don't want to install the module).

# Usage

```bash
usage: check-cdp.py [-h] [-w WARNRATIO] [-q] CDP [CDP ...]

positional arguments:
  CDP                   CDP id(s) to check

optional arguments:
  -h, --help            show this help message and exit
  -w WARNRATIO, --warnratio WARNRATIO
                        minimum ratio in percent that gives a warning
  -q, --quiet           only output warnings
```

The script returns 0 if all the CDPs meet the requirements, 1 (error) otherwise

# Example outputs

```
# python3 check-cdp.py -w 150 3200 3500
  Deposited 26.087552656982794963 PETH
  Debt 1000.000000000000000000 DAI
  Current Ratio 3.475557176022628644000000000
CDP #3500
  Owner 0x571E524149ffC22615f49F0F785BB605dc50472b
  Deposited 0.077705745309196834 PETH
  Debt 0.000000000000000000 DAI
# python3 check-cdp.py -w 350 3200
  Owner 0xF230213506F2e4eB53B902D613B98a0dBE7fB1Bc
  Deposited 26.087552656982794963 PETH
  Debt 1000.000000000000000000 DAI
  Current Ratio 3.475557176022628644000000000
CDP #3200 is 3.475557176022628644000000000 which is below 3.500000000000000000000000000
# python3 check-cdp.py -w 350 -q 3200
CDP #3200 is 3.475557176022628644000000000 which is below 3.500000000000000000000000000
# python3 check-cdp.py -w 350 -q 3500 && echo Everything is fine
Everything is fine
```


































































