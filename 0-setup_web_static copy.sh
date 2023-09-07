#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of
sudo get-apt -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello World! deploy" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
if ! grep -q 'location /hbnb_static/' /etc/nginx/sites-available/default; then
    sudo sed -i '/server {/a \ \ \ \ location /hbnb_static/ {\n \ \ \ \ \ \ alias /data/web_static/current/;\n \ \ \ \ }\n' /etc/nginx/sites-available/default
fi
sudo service nginx start
