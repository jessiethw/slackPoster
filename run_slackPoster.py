#!/usr/bin/env python3

# Main code to search the arXiv for new articles

import os


main_dict = {
             'lemma': 'astro,physics,hep',
}

for name, channels in main_dict.items():

     print(name)

     # For production
     os.system('./lazy_astroph.py -w {0}/webhook --channel {1} {0}/inputs'.format(name, channels))

     # For running without updating param files or posting to Slack
     #os.system('./lazy_astroph.py --dry_run --channel {1} {0}/inputs'.format(name, channels))
