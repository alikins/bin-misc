#!/usr/bin/python

import os
import sys

HASCOLORAMA = True
try:
    import colorama
    from colorama import Fore
except ImportError:
    HASCOLORAMA = False


def format_env(env_keys, env_dict, color=False):
    outlines = []
    print('color=%s' % color)
    for env_key in env_keys:
        env_value = env_dict[env_key]
        if color:
            outlines.append('%s' % Fore.GREEN + '%s' % env_key + Fore.RESET +
                            Fore.YELLOW + '=' + Fore.RESET +
                            Fore.WHITE + '%s' % env_value + Fore.RESET)
        else:
            outlines.append('%s=%s' % (env_key, env_value))
    return '\n'.join(outlines)


def output(msg):
    print(msg)


def main(args):
    if HASCOLORAMA:
        colorama.init(autoreset=True)

    env_keys = os.environ.keys()
    sorted_env_keys = reversed(sorted(env_keys))

    env_output = format_env(sorted_env_keys, os.environ, HASCOLORAMA)
    output(env_output)


if __name__ == "__main__":
    sys.exit(main(sys.argv[:]))
