MODEL=$1
LEFT=$2
RIGHT=$3

for i in $(seq 45 1 47)
do
    python tools/test_net.py --loadmodel ./outputs/model24g_blurred_wgan-res50p-1024_scratch_batch1/finetune_${i}.tar -d 1 -btest 8 --left_path $LEFT --right_path $RIGHT
done

for i in $(seq 45 1 50)
do
    python tools/test_net.py --loadmodel ./outputs/model24g_blurred_wgan-res50p-1024_scratch/finetune_${i}.tar -d 1 -btest 8 --left_path $LEFT --right_path $RIGHT
done
