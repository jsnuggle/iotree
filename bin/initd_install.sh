# Install initd script to run buzzer bot server on start up

SERVER_DIR=`pwd`
USER=`whoami`
TMUX_SESSION="iotree"

VARS=$( cat <<EOF
SERVER_DIR=$SERVER_DIR
USER=$USER
TMUX_SESSION=$TMUX_SESSION
EOF
)

echo -e "#! /bin/bash\n$VARS" "$(cat bin/initd.tpl)" > iotree_init.sh
chmod +x iotree_init.sh
sudo mv iotree_init.sh /etc/init.d/
sudo update-rc.d iotree_init.sh defaults

ls -l /etc/init.d/iotree_init.sh
echo "Installed init.d"
