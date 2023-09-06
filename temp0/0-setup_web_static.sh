#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart


# sudo apt-get -y update
# sudo apt-get -y upgrade
# sudo apt-get -y install nginx
# sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
# echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
# sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# sudo chown -hR ubuntu:ubuntu /data/
# sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
# sudo service nginx start