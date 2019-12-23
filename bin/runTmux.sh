tmux new-session -d -s iotree -n 0
tmux send-keys -t iotree:0 "./bin/run.sh" Enter
