import argparse
import sys

from web3 import HTTPProvider, Web3

from pymaker import Address
from pymaker.token import ERC20Token
from pymaker.numeric import Ray,Wad
from pymaker.sai import Tub

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--warnratio", help="minimum ratio in percent that gives a warning",
                    type=int, default="180")
parser.add_argument("-q", "--quiet", help="only output warnings",
                    action='store_true')
parser.add_argument('cdps', metavar='CDP', type=int, nargs='+',
                    help='CDP id(s) to check')
args = parser.parse_args()

web3 = Web3(HTTPProvider(endpoint_uri="https://mainnet.infura.io/metamask"))

tub = Tub(web3=web3, address=Address('0x448a5065aebb8e423f0896e6c5d525c040f59af3'))
minimum_ratio=Ray.from_number(args.warnratio / 100)
requirements_satisfied=True

for cup_id in args.cdps:
    cup = tub.cups(cup_id)
    pro = tub.ink(cup_id)*tub.tag()
    tab = tub.tab(cup_id)
    if not args.quiet:
        print(f'CDP #{cup_id}')
        print(f'  Owner {cup.lad}')
        print(f'  Deposited {float(cup.ink):.8} PETH')
        print(f'  Debt {float(tab):.8} DAI')
    if tab > Wad(0):
        current_ratio = Ray(pro / tab)
        if not args.quiet:
            print(f'  Current Ratio {float(current_ratio):.2%}')
        is_undercollateralized = (current_ratio < minimum_ratio)
        if is_undercollateralized:
            print(f'CDP #{cup_id} is {float(current_ratio):.2%} which is less than {float(minimum_ratio):.2%}')
            requirements_satisfied=False

if not requirements_satisfied:
    sys.exit(1)
