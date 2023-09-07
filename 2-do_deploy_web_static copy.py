#!/usr/bin/env bash
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
from fabric.api import put, run
from os.path import exists


env.hosts = ['34.229.69.114', '100.26.122.201']
""" list of host ip address """


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
