# Oral Cancer Detection: A Comparative Study of Computer Vision Models

Code for the paper **"A comparative study of computer vision models for oral cancer detection from oral photographs"** (de Chauveron et al., *Computer Methods and Programs in Biomedicine*, 109198).

This repo benchmarks several object detection models on detecting oral cancer lesions in oral photographs, using [MMDetection](https://github.com/open-mmlab/mmdetection).

! Before running the script update the values in the configurations files such as <path_to_checkpoint> ! 
The training script for the yolo model works for all the yolo models tested in this thesis 

## Setup

Follow the [MMDetection installation guide](https://mmdetection.readthedocs.io/en/latest/get_started.html), then clone this repo:

    git clone <repo-url>
    cd <repo-name>

## Usage

Train a model:

    python tools/train.py configs/<model_config>.py

Evaluate a model:

    python tools/test.py configs/<model_config>.py <checkpoint>.pth

## Citation

    @article{dechauveron2025oral,
      title   = {A comparative study of computer vision models for oral cancer detection from oral photographs},
      author  = {de Chauveron, J{\'e}r{\^o}me and Zha, Chenyu and Lescaille, G{\'e}raldine and Shaar-Chneker, Caroline and Brocheriou, Isabelle and Wendling, Laurent and Kurtz, Camille and Rochefort, Juliette},
      journal = {Computer Methods and Programs in Biomedicine},
      pages   = {109198},
      year    = {2025}
    }
