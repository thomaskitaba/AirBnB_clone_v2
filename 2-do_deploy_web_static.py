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
        put(archive_path, "/temp/")   # TODO: archive path or file
        # Uncompress the archive to the folder
        # # create folder with name the same as the archive name
        run(f"mkdir -p {path}{f_name_only}/")
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        run(f"tar -xzvf /temp/{f_name_all} {path}{f_name_only}")
        # Delete the archive from the web server
        run("rm -rf /temp/{f_name_all}")
        # Delete the symbolic link /data/web_static/current from
        # the web server
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current on
        # the web server, linked to the new version of your code
        run(f"ln -sf /data/web_static/current  path{f_name_only}")

        # (/data/web_static/releases/<archive
        # filename without extension>)

    except Exception:
        success = False
    return success
