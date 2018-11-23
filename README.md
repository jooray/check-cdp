# Description

This script will check CDP(s) of [DAI stablecoin](https://makerdao.com/dai) for collateral requirements.

The reason to use this instead of [cdp-keeper](https://github.com/makerdao/cdp-keeper) is for example when your CDPs are on a hardware wallet such as Trezor and you don't have access to private keys, but want to be notified if something happens. It would be wise to keep WARNRATIO at 200% or more.

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
CDP #3200
  Owner 0xF230213506F2e4eB53B902D613B98a0dBE7fB1Bc
  Deposited 50.24188 PETH
  Debt 1926.0 DAI
  Current Ratio 334.91%
CDP #3500
  Owner 0x571E524149ffC22615f49F0F785BB605dc50472b
  Deposited 0.077705745 PETH
  Debt 0.0 DAI
# python3 check-cdp.py -w 350 3200
CDP #3200
  Owner 0xF230213506F2e4eB53B902D613B98a0dBE7fB1Bc
  Deposited 50.24188 PETH
  Debt 1926.0 DAI
  Current Ratio 334.91%
CDP #3200 is 334.91% which is less than 350.00%
# python3 check-cdp.py -w 350 -q 3200
CDP #3200 is 334.91% which is less than 350.00%
# python3 check-cdp.py -w 350 -q 3500 && echo Everything is fine
Everything is fine
```

# dai checker script

There is an example script in *dai-checker.sh.example*
that sends notifications at most every two hours.

We use signal as an example, using
[signal-cli](https://github.com/AsamK/signal-cli), but you can use any
other messenger or app that has a command line interface (like plain old
e-mail).
