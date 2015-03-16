#!/usr/bin/python
# encoding: utf-8
#
# Copyright © 2015 Jonathan McAuliffe
#
# Created on 15/03/2015
#

"""
"""

from __future__ import unicode_literals, print_function

import sys
import os
import subprocess
from workflow import Workflow, ICON_NETWORK

VERSION = '1.0'


def search_key_for_venv(venv):
    """Generate a string search key for a venv"""
    elements = []
    elements.append(venv)  # title of post
    return u' '.join(elements)


def main(wf):

    # Get query from Alfred
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    # -- this way works in the terminal but not with alfred... --
    # p = subprocess.Popen("source $(which virtualenvwrapper.sh)
    # && lsvirtualenv -b | sort -df | grep -v '^$'", shell=True,
    # stdout=subprocess.PIPE)

    workon_home = os.getenv('WORKON_HOME')
    workon_home = b"{}".format(workon_home)

    p = subprocess.check_output([b'ls',
                                 os.path.join(os.getenv('HOME'),
                                              '.virtualenvs')])

    p = wf.decode(p)
    # lst = (p.stdout.read()).split('\n')
    lst = p.split('\n')
    # venvs = [x for x in lst if x != '']
    venvs = [x for x in lst if
             os.path.exists(os.path.join(os.getenv('HOME'),
                                         '.virtualenvs', x,
                                         'bin/activate'))]

    # If script was passed a query, use it to filter posts
    if query:
        venvs = wf.filter(query, venvs, key=search_key_for_venv)

    # Loop through the returned venvs and add an item for each to
    # the list of results for Alfred
    for venv in venvs:
        wf.add_item(title=venv,
                    arg=venv,
                    valid=True,
                    icon=ICON_NETWORK)

    # Send the results to Alfred as XML
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
