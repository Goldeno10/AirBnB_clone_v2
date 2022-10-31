#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""


import os
from datetime import datetime
from fabric.api import env, local, put, run


env.hosts = ['34.204.198.163', '54.85.106.26']
# env.user = 'ubuntu'
# env.key_filename = '/path/to/rsa/key/file'


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


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return False
    try:
        # Archive fullname with extension
        arch_f_n = archive_path.split("/")[-1]
        # Archive name without Extension
        arch_n_x = arch_f_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/temp/')
        run("mkdir -p {}{}/".format(path, arch_n_x))
        run("tar -xzf /temp/{} -C {}{}".format(arch_path, path, arch_n_x))
        run("rm  /temp/{}".format(archive_f_n))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, arch_n_x))
        run("rm -rf {0}{1}/web_static".format(path, arch_n_x))
        run("rm -rf /data/web_static/current")
        run("sudo ln -s {}{} /data/web_static/current".format(path, arch_n_x))
        return True
    except Exception:
        return False

def deploy():
    """ creates and distributes an archive to your web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
