#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from esa.client import Client

token = os.environ['ESA_ACCESS_TOKEN']


def main():
    client = Client(access_token=token, current_team='taznica')

    print(client.teams())


if __name__ == '__main__':
    main()
