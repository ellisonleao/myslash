#!/usr/bin/env python
# encoding: utf-8
import os

from bottle import run, post


@post('/hello')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    run(host='0.0.0.0', port=port)
