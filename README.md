# COMP6733 Project Repo

## How to run inference demo   
Run with camera: `python3 inference_demo.py`     
Run with video file: `python3 inference_demo.py <video file path>`     

## How to run pyqt demo
Run with camera: `python3 pyqt_demo.py`     
Run with video file: `python3 pyqt_demo.py <video file path>`     

If the camera failed to load frames, close the app, execute
`sudo systemctl restart nvargus-daemon`
, and re-launch the demo script.
