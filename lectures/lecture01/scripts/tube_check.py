import argparse
from urllib.request import urlopen
import json

parser = argparse.ArgumentParser()

parser.add_argument("mode", nargs='*',
                    help="transport modes to consider: eg. tube, bus or dlr.",
                    default=("tube", "overground"))
parser.add_argument("-l", "--lines", nargs='+',
                    help="specific lines/bus routes to list: eg. Circle, 73.")

args = parser.parse_args()

if args.lines:
    url = "https://api.tfl.gov.uk/line/%s/status"%','.join(args.lines)
else:
    url = "https://api.tfl.gov.uk/line/mode/%s/status"%','.join(args.mode)
    
# For python 3.6+ you can just use "status = json.load(url)"
status = json.loads(str(urlopen(url).read(),'ascii'))

short_status = {s['name']:s['lineStatuses'][0]['statusSeverityDescription']
	             for s in status}
	
for _ in short_status.items():
    print('%s: %s'%_)