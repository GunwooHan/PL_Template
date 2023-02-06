python train.py --gpus=3 \
 --train_data_dir ~/codes/datasets/TianChiBuilding/train \
 --name resnest14dupp \
 --name ResNeSt50dMeanGSoPSCA_2UnetPP \
 --model ResNeSt50dMeanGSoPSCA_2UnetPP \
 --precision 32 \
 --buildingSegTransform True \
 --batch_size 32 \
 --epochs 32 \
 --learning_rate 0.0005 \
 --optimizer adamp \
 --kfold 2 \
