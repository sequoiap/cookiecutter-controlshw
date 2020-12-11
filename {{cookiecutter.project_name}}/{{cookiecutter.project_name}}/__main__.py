#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Run a simulation.")
parser.add_argument('-hw', '--homework', action='store', required=True, \
    help="The homework problem to run the simulation for.", dest='hw')
parser.add_argument('-p', '--liveplot', action='store_true', help="Real-time \
    plots and simulation will be generated if flag is included.", dest='liveplot')

args = parser.parse_args()
print(args.hw, args.liveplot)
