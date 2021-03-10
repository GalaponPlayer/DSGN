MODEL=$1
LEFT=$2
RIGHT=$3

for i in $(seq 1 2 60)
do
    python tools/test_net.py --loadmodel $MODEL/finetune_${i}.tar -d 0 -btest 8 --left_path $LEFT --right_path $RIGHT
done
