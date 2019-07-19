#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from esa.client import Client

token = os.environ['ESA_ACCESS_TOKEN']
team_name = os.environ['TEAM_NAME']


def main():
    client = Client(access_token=token, current_team=team_name)

    print(client.team(team_name))


if __name__ == '__main__':
    main()
