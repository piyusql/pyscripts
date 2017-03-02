sudo mkdir -p /data/local /data/bitb /data/backup /data/personal
sudo chown -R `whoami`: /data
ls -l /data
sudo apt-get update
sudo apt-get install vim byobu git python-dev tree htop -y
sudo apt-get install postgresql-9.4 postgresql-server-dev-9.4 --fix-missing
git clone https://github.com/piyusgupta/pyscripts.git /data/personal/pyscripts
cat ~/.vimrc << EOF
set nu
set expandtab
set shiftwidth=4
set softtabstop=4

filetype plugin on
EOF
