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
import os
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Archives the static files."""
    if not isdir("versions"):
        local("mkdir -p versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        local("tar -cvzf {} web_static".format(output))
    except Exception:
        output = None
    return output
