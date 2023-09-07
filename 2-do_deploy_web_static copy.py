#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the function do_pack.
Prototype: def do_pack():
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions (your function
should create this folder if it doesn’t exist)
The name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the
archive has been correctly generated. Otherwise, it should return None
"""
import os
from datetime import datetime
from fabric.api import local
from os.path import isdir
from os import exitsts


def do_pack():
    """Archives the static files."""
    if not isdir("versions"):
        local("mkdir -p versions")
    cur_time = datetime.now()
    archive_time = cur_time.strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{archive_time}.tgz"

    try:
        local("tar -cvzf {} web_static".format(archive_name))
    except Exception:
        archive_name = None
    return archive_name


env.hosts = ['34.229.69.114', '100.26.122.201']
""" list of host ip address """


def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    success = False
    try:
        # archive_path = versions/filename.tgz
        f_name_all = archive_path.split('/')[-1]
        f_name_only = f_name_all.split('.')[0]
        path = "/data/web_static/releases/"
        # Upload the archive to the /tmp/ directory of the web server
        # syntax put(local_path, remote_path)
        put(archive_path, f"/temp/{f_name_only}")
        # Uncompress the archive to the folder
        # # create folder with name the same as the archive name
        run(f"mkdir -p {path}{f_name_only}")
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        run(f"tar -xzvf /temp/{f_name_all} -C {path}{f_name_only}")
        # Delete the archive from the web server
        run("rm -rf /temp/{f_name_all}")

        run("mv {}{}web_static/* {}".format(path, f_name_only, path))
        # Delete the symbolic link /data/web_static/current from
        # the web server
        run("rm -rf {}web_static".format(path))

        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on
        # the web server, linked to the new version of your code
        run(f"ln -sf /data/web_static/current  path{f_name_only}")

        # (/data/web_static/releases/<archive
        # filename without extension>)

    except Exception:
        success = False
    return success
