

case "$1" in

start)
    echo "starting server in: $SERVER_DIR in tmux session: $TMUX_SESSION"
    cd $SERVER_DIR
    sudo -u $USER ./bin/runTmux.sh 
    ;;

stop)
    echo "stopping server in: $SERVER_DIR / tmux session: $TMUX_SESSION"
    cd $SERVER_DIR
    sudo -u $USER ./bin/killTmux.sh
    ;;

restart)
    echo "restarting server in: $SERVER_DIR with tmux session: $TMUX_SESSION"
    cd $SERVER_DIR
    sudo -u $USER ./bin/killTmux.sh
    sudo -u $USER ./bin/runTmux.sh
    ;;
*)
    echo "usage: $0 (start|stop|restart)"
esac

exit 0
