#!/usr/bin/python3
""" Contains a function that compress a folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ Compresses a folder """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = f"versions/web_static_{t.strftime(f)}.tgz"
        local(f'tar -cvzf {archive_path} web_static/')
        return archive_path
    except Exception:
        return None
