#!/usr/bin/python3
"""
    Write a Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy:
    Prototype: def deploy():
    The script should take the following steps:
    Call the do_pack() function and store the path of the created
    archive
    Return False if no archive has been created
    Call the do_deploy(archive_path) function, using the new path of
    the new archive
    Return the return value of do_deploy
    All remote commands must be executed on both of web your servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your
    script)
    You must use this script to deploy it on your servers: xx-web-01
    and xx-web-02
"""
from fabric.api import run
from "2-do_deploy_web_static" import do_pack


def do_deploy(archive_path):
    pass

def deploy():
    archive_path = do_pack()
    if do_pack() is None:
        return false
    do_deploy(archive_path)
