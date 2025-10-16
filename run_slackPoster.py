#!/usr/bin/env python3

# Main code to search the arXiv for new articles

import os
cwd = '~/Research/slackPoster'

main_dict = {
             'lemma': 'astro,physics,hep',
}

for name, channels in main_dict.items():

     print(name)

     # For production
     os.system('{2}/slack_env/bin/python {2}/lazy_astroph.py -w {2}/{0}/webhook --channel {1} {2}/{0}/inputs'.format(name, channels, cwd))

     # For running without updating param files or posting to Slack
     #os.system('{2}/slack_env/bin/python {2}/lazy_astroph.py --dry_run --channel {1} {2}/{0}/inputs'.format(name, channels, cwd))
