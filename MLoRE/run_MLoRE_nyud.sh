export DATA_PATH="/home/khlee01/dataset/"
RANDOM=$$
CUDA_VISIBLE_DEVICES=0,1 torchrun -m torch.distributed.launch --nproc_per_node=2  --master_port=$((RANDOM%1000+12000))  main.py --config_exp './configs/nyud/nyud_vitLp16_MLoRE.yml' --run_mode train
