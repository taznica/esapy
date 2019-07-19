#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from esa.client import Client

token = os.environ['ESA_ACCESS_TOKEN']
team_name = 'taznica'


def main():
    client = Client(access_token=token, current_team=team_name)

    print(client.post(team_name, 20))


if __name__ == '__main__':
    main()
