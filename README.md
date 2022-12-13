# SmartEdge Object Tracker    

## Introduction   
SmartEdge Tracker is a realtime GUI-based(touch monitor friendly) object tracking application developed for NVIDIA Jetson Nano. 
This application should also work on other NVDIA Jetson devices but we haven't tested yet as we don't have other Jetson devices.
For this particular project, we used the dataset from [Kaggle](https://www.kaggle.com/competitions/tensorflow-great-barrier-reef) and trained a `yolov5n`(YOLOv5 v6.0) model detecting Crown-of-Throns Starfish(COTS). 
We also added a SORT object tracker to track and count the number of COTS.

If you want to track other objects, you can also train your own model (yolov5n), convert the weights to `.wts` and replace the model file in the `weights` directory. 
The application will then automatically create a `.engine` file (TensorRT optimized model) for inference. 

Below is a screenshot of the application. You can also find our demo video [HERE](https://youtu.be/37IsbjCkvEU) on YouTube. 

[![GUI](https://github.com/FreemanX/SmartEdgeTracker/blob/main/res/gui.png)](https://youtu.be/37IsbjCkvEU)

## Setup running environment   
Follow the instructions in this repo [jetson-setup](https://github.com/FreemanX/jetson-setup). 

## How to run the application
Run with camera: `python3 main.py`     
Run with video file: `python3 main.py <video file path>`. 
The demo video can be downloaded from [GoogleDrive](https://drive.google.com/file/d/1t2q_rHtbBLUDrqLC2tBmAobv4_FxuDhF/view?usp=share_link)

If the camera failed to load frames, close the app, execute
`sudo systemctl restart nvargus-daemon`
, and re-launch the demo script.

## Reference   
* YOLOv5: https://github.com/ultralytics/yolov5 
* tensorrtx: https://github.com/wang-xinyu/tensorrtx/tree/master/yolov5 
* SORT: https://github.com/abewley/sort 
