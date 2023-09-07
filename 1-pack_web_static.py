#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz
archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
Prototype: def do_pack():
All files in the folder web_static must be added to
the final archive All archives must be stored in the
folder versions (your function should create this folder
if it doesn’t exist) The name of the archive created
must be web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the
archive has been correctly generated. Otherwise, it should return None
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    try:
        if not isdir("versions"):
            local("mkdir -p versions")

        archive_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_" + archive_time + ".tgz"

        local(f"tar -czvf {archive_name} web_static")

        return archive_name
    except Exception as e:
        return None
