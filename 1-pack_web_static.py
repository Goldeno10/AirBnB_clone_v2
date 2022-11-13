#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""


import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Compresses a folder and contents to a tgz archive """

    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date)
        local('tar -cvzf {} web_static/'.format(archive_path))
        return archive_path
    except Exception:
        return None
