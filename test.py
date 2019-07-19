#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from esa.client import Client
from esa.post import Post

token = os.environ['ESA_ACCESS_TOKEN']
team_name = 'taznica'


def main():
    client = Client(access_token=token, current_team=team_name)

    post = Post(name='test4', category='dev/aaa', tags=['test', 'test2'])

    print(client.new_post(team_name, post))


if __name__ == '__main__':
    main()
