#!/usr/bin/env python3

# twitter bot for @plaspoly Copyright 2019 Thomas Homer

# Based on blades-tweet.py Copyright 2018 Bryant Durrell
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse
import json
# import tweepy
import tracery
from tracery.modifiers import base_english
# from credentials import *

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

def generate():
    parser = argparse.ArgumentParser(description='PlasticPolyhedra tweetbot')
    parser.add_argument('--grammar', required=True, help='JSON grammar')
    parser.add_argument('--maxlen', default=260, type=int, help='Max tweet length')
    parser.add_argument('--print', help='Print score', action='store_true')
    parser.add_argument('--tweet', help='Tweet score', action='store_true')
    args = parser.parse_args()

    with open(args.grammar) as data_file:
        rules = json.load(data_file)

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    score = ''
    while len(score) == 0:
        score = grammar.flatten('#origin#')

    score = ' '.join(score.split())

    score = score.replace('|','#')

    if len(score) > args.maxlen:
       score = score[:args.maxlen]+'...'

    if args.print:
        print(score)
        print(len(score))
#    if args.tweet:
 #       api.update_status(score)

if __name__ == '__main__':
    generate()
