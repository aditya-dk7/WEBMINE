#!/usr/bin/python3

import argparse


try:
    from bin import banner
    from bin import trim_url


    banner.print_banner()

    class CapitalisedHelpFormatter(argparse.HelpFormatter):
        def add_usage(self, usage, actions, groups, prefix=None):
            if prefix is None:
                prefix = 'Usage: '
            return super(CapitalisedHelpFormatter, self).add_usage(
                usage, actions, groups, prefix)


    parser = argparse.ArgumentParser(prog='webvulsca.py', usage='%(prog)s [options]', add_help=False,
                                     formatter_class=CapitalisedHelpFormatter)
    parser._positionals.title = 'Positional arguments'
    parser._optionals.title = 'Options'
    parser.add_argument('-u', '--url', help='Target URL (e.g. "http://www.site.com/")', required=True, metavar='')
    parser.add_argument('-o', '--outfile', help='Output Directory Path (e.g. "/root/example_dir/")', metavar='',
                        required=True)
    parser.add_argument('-c','--crawl',help='This option crawls the complete website',action='store_true',default=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Show this help message and exit.')

    args = parser.parse_args()

    trim_url.url_splitter(args.url,args.crawl)


except ImportError:
    print("[-] Unsupported for Python 2")


