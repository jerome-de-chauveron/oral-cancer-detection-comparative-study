from ultralytics import YOLO
import os 
os.environ['WANDB_DISABLED'] = 'true'

data_root = '<path_to_data>'
# Load the model.
model = YOLO("<path_to_yolo_model_weight>")
lr = 0.00001
epochs = 60

for fold in [0, 1, 2, 3, 4]:
    # Training.
    path_fold = data_root+str(fold)
    results = model.train(
        data=os.path.join(path_fold, "Descriptor.yaml"),
        imgsz=840,
        epochs=epochs,
        batch=8,
        name='yolov<version>_60epochs_fold_'+str(fold)+"", 
        lr0=lr, 
        optimizer ="Adam", 
        flipud=0.5, 
        shear=5, 
        degrees=90, 
        single_cls=False
    )
