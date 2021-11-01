# Sign Language-to-Speech with DeepStack's Custom API

![](https://github.com/SteveKola/Sign-Language-to-Speech-with-DeepStack-Custom-API/blob/main/scripts/gifs/proof.gif)

This project is an end-to-end working prototype that uses Artificial intelligence to detect sign language meanings 
in images/videos and generate equivalent, realistic voice of words communicated by the sign language.


## Steps to run the project
### 1. Install DeepStack using Docker. (Skip this if you already have DeepStack installed)
- Docker needs to be installed first. For Mac OS and Windows users can install Docker from 
[Docker's website](https://www.docker.com/products/docker-desktop).
- To install on a Linux OS,run the code below;

```
  sudo apt-get update && sudo apt-get install docker.io
  ```
- Install DeepStack. *You might want to grab a coffee while waiting for this to finish its execution :smirk:*
```
  docker pull deepquestai/deepstack
 ```
- Test DeepQuest.
```
  docker run -e VISION-SCENE=True -v localstorage:/datastore -p 80:5000 deepquestai/deepstack
 ```
**NOTE:** This works for the CPU variant only. To explore the other ways to install, check the 
[official tutorial](https://docs.deepstack.cc/#installation-guide-for-cpu-version).

> **Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use.**
    
If you come across this error, change `-p 80:5000` to another port, e.g., `-p 88:5000`. 
(I'm using **88**, too :blush:).


### 2. Clone the Project Repository and Install Dependencies
- To clone this repo, copy and run the command below in your bash and change into the new 
directory with the next line of code.
```
  git clone https://github.com/SteveKola/Sign-Language-to-Speech-with-DeepStack-Custom-API.git
  cd Sign-Language-to-Speech-with-DeepStack-Custom-API
  ```
- To avoid potential *dependency hell*, create a virtual enviroment and 
activate the created virtual environment afterwards.
``` 
  python3 -m venv env   
  source env/bin/activate
```
- Install the dependencies using `pip install -r requirements`.
- If you are on a Linux OS, TTS engines might not be pre-installed on your platform. Use the code below to install them.
```
  sudo apt-get update && sudo apt-get install espeak ffmpeg libespeak1
```


### 3. Spin up the DeepStack custom model's Server.
- While still in the project directory's root, spin up the deepstack custom model's server by running the command below;
```
  sudo docker run -v ~/path/to/folder/deployed_model:/modelstore/detection -p 88:5000 deepquestai/deepstack
```

### 4. Detect sign language meanings in image files and generate realistic voice of words.
- run the image_detection script on the image;
```
  python image_detection.py image_filename.file_extension
 ```
My default port number is 88. To specify the port on which DeepStack server is running, run this instead;
```
python image_detection.py image_filename.file_extension --deepstack-port port_number
```
Running the above command would return two new files in your project root directory - 
     
1. a copy of the image with bbox around the detected sign with the meaning on the top of the box,
2. an audiofile of the detected sign language.

![image](https://user-images.githubusercontent.com/45284829/123965899-cfde8080-d9ac-11eb-874e-14d69b2e0c0c.png)
![image](https://user-images.githubusercontent.com/45284829/123966073-f4d2f380-d9ac-11eb-8053-80a92130dedc.png)

### 5. Detect sign language meanings on a live video (via webcam).
- run the livefeed detection script;
```
  python livefeed_detection.py
```
My default port number is 88. To specify the port on which DeepStack server is running, run this instead;
```
  python livefeed_detection.py --deepstack-port port_number
```
This will spin up the webcam and would automatically detect any sign language words in view of the camera,
while also displaying the sign meaning and returning its speech equivalent immediately through the PC's audio system. 

![](https://github.com/SteveKola/Sign-Language-to-Speech-with-DeepStack-Custom-API/blob/main/scripts/gifs/proof.gif)


## Additional Notes
- **This project has built and tested successfully on a Linux machine. Other errors might arise on other Operating Systems,
which might not have been accounted for in this documentation)**.
- The dataset used in training the model was created via my webcam using an automation scipt. 
[scripts/creating_data.py](https://github.com/SteveKola/Sign-Language-to-Speech-with-DeepStack-Custom-API/blob/main/scripts/creating_data.py)
is the script used.
- My dataset could be found in [this repository](https://github.com/SteveKola/Sign-Language-to-Speech-with-DeepStack-Custom-API/tree/main/scripts). 
The repo contains both the DeepStack model's data and the TensorFlow Object Detection API's data (I did that about a month before this).
- Dataset was annotated in YOLOv format using [LabelImg](https://github.com/tzutalin/labelImg).
- Model was trained using Colab GPU. 
[scripts/model_training_deepstack.ipynb](https://github.com/SteveKola/Sign-Language-to-Speech-with-DeepStack-Custom-API/blob/main/scripts/model_training_deepstack.ipynb)
is the notebook used for that purpose. 

## Attributions
- The [DeepStack custom models' official docs](https://docs.deepstack.cc/custom-models/) contains everything that'd be
needed to replicate the whole building process. It is lean and concise.
- A big **thank you** to [Patrick Ryan](https://github.com/youngsoul) for making it seem like 
the project is not too herculean in his [article](https://docs.deepstack.cc/custom-models/).
- I got my first introduction to DeepStack's custom models with this 
[article](https://medium.com/deepquestai/detect-any-custom-object-with-deepstack-dd0a824a761e).
Having built few with TensorFlow, I can't appreciate this enough.
