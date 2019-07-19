#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from esa.client import Client

token = os.environ['ESA_ACCESS_TOKEN']


def main():
    client = Client(team_name='taznica', access_token=token)

    print(client.teams())


if __name__ == '__main__':
    main()
