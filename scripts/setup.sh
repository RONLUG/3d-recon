# Load human-pose estimation's checkpoint 
mkdir -p checkpoints
cd checkpoints
if [ -f checkpoint_iter_370000.pth ]; then
    echo "Checkpoint already exists"
    rm checkpoint_iter_370000.pth
fi
wget https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth


# Load PIFuHD checkpoint
if [ -f pifuhd.pt ]; then
    echo "Checkpoint already exists"
    rm pifuhd.pt
fi
cd ..

sh ./pifuhd/scripts/download_trained_model.sh
