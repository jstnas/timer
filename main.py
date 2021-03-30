import argparse
from timer import Timer

def main():
    parser = argparse.ArgumentParser(description='Wait for a specified amount of time')
    parser.add_argument('duration', help='The amount of time to wait')
    parser.add_argument('-i', '--interval', default=1, type=float, help='The pause between updates')
    parser.add_argument('-s', '--suffix', default='m', type=str, choices=['M', 's', 'm', 'h', 'd', 'w'], help='The default suffix')
    parser.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()
    duration = args.duration
    interval = args.interval if args.interval is not None else 1
    suffix = args.suffix if args.suffix else 'm'
    quiet = args.quiet
    t = Timer(duration, interval, suffix, quiet)
    return t.wait()

if __name__ == '__main__':
    main()
