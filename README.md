# SmartEdge Object Tracker    
This is our term project for course `COMP6733 IoT Design Studio (22T3)` @ UNSW.

## Introduction   
SmartEdge Tracker is a realtime GUI-based(touch monitor friendly) object tracking application developed for NVIDIA Jetson Nano. 
This application should also work on other NVIDIA Jetson devices, but we haven't tested yet as we don't have other Jetson devices.
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

## Compare with Google's solution
CSIRO cooperated with Google developed a real life application in a larger scale: [Using Machine Learning to Help Protect the Great Barrier Reef in Partnership with Australia’s CSIRO](https://blog.tensorflow.org/2022/05/Kaggle-Great-Barrier-Reef-ML.html). Here's a rough comparison between our system and Google's solution(one slide extracted from our project presentation):
<img width="1371" alt="screenRecording 2023-01-14 at 17 00 35@2x" src="https://user-images.githubusercontent.com/9710644/212458314-10bb36df-e399-475d-a334-9cb72e31fa55.png">

### Professor's comment
> I am impressed very much by the the quality of the projects. I would like to particularly highlight the following project and team. "AI On Edge: Help Protect the Great Barrier Reef" by Team SmartEdge (Members' names are omitted due to privacy concerns). The guest lecturer from CSRIO that works on the project is also very impressed by the results achieved.


## Reference   
* YOLOv5: https://github.com/ultralytics/yolov5 
* tensorrtx: https://github.com/wang-xinyu/tensorrtx/tree/master/yolov5 
* SORT: https://github.com/abewley/sort 
