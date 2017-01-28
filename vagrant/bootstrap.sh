#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive
export MYSQL_ROOT_PASS=poitot

echo "source /home/ubuntu/vagrant/bin/activate" >> .bashrc
echo "cd /vagrant" >> .bashrc

sudo apt-get update

sudo apt-get clean

sudo apt-get -y install git
sudo apt-get -y install python-dev python-pip
sudo apt-get -y install mysql-client libmysqlclient-dev

sudo pip install --upgrade pip

# Pip moved location after upgrade from 1.0
sudo ln -s /usr/local/bin/pip /usr/bin/pip 2>/dev/null

sudo pip install virtualenv
sudo pip install mysql-connector-python mysql-connector-python

virtualenv -p /usr/bin/python3 vagrant

sudo debconf-set-selections <<< "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASS"
sudo debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASS"
sudo apt-get -y install mysql-server

#check it's up
sudo mysqladmin status -p$MYSQL_ROOT_PASS

sudo mysql -u root -p$MYSQL_ROOT_PASS -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'password'"
sudo mysql -u root -p$MYSQL_ROOT_PASS -e "GRANT ALL PRIVILEGES ON * . * TO 'django'@'localhost'";

sudo mysqladmin -p$MYSQL_ROOT_PASS flush-privileges

source /home/ubuntu/vagrant/bin/activate
pip install -r /vagrant/requirements.txt
