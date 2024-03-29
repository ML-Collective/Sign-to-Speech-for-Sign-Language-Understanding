# Sign-to-Speech for Sign Language Understanding: A case study of Nigerian Sign Language

![sign](https://user-images.githubusercontent.com/45284829/139852417-a2e1b40a-ee7c-41e9-9ef5-bbd4983ac320.gif)

This repository contains the code, model, and deployment configs for the paper [**Sign-to-Speech for Sign Language Understanding: A case study of Nigerian Sign Language**](https://www.ijcai.org/proceedings/2022/855) which appeared first at the NeurIPS workshop on Machine Learning for Developing World (ML4D) 2021, and subsequently as a demo paper at the Thirty-First International Joint Conference on Artificial Intelligence {IJCAI-22}.

## Dataset
Our dataset is a novel dataset for the Nigerian Sign Language comprising of 5000 images of 137 sign words/phrases including the alphabet letters. Data collectors of 20+ individuals comprising of a TV sign language broadcaster and students and teachers from 2 special education schools in Nigeria. The dataset is hosted on [Lanfrica Records](https://lanfrica.com/record/sign-to-speech-for-sign-language-understanding-a-case-study-of-nigerian-sign-language).

## Model configs and code
- [YOLO model](https://github.com/SteveKola/Sign-to-Speech-for-Sign-Language-Understanding/tree/master/savedmodels_configs/yolo_model)
- [SSD model](https://github.com/SteveKola/Sign-to-Speech-for-Sign-Language-Understanding/tree/master/savedmodels_configs/ssd_model)
- [Classification model](https://github.com/SteveKola/Sign-to-Speech-for-Sign-Language-Understanding/tree/master/savedmodels_configs/classification_model)

## To run deployed model
- Clone the repository and `pip install -r requirements`.
- If you are on a Linux OS, TTS engines might not be pre-installed on your platform. Use the code below to install them.
```
  sudo apt-get update && sudo apt-get install espeak ffmpeg libespeak1
```
- Install Python's dependencies.
```
  pip install -r requirements.txt
```
- While in the project directory's root, spin up the deepstack custom model's server by running the command below;
```
  sudo docker run -v ~/path/to/project_folder/savedmodels_configs/yolo_model/weights:/modelstore/detection -p 88:5000 deepquestai/deepstack
```

#### - Detect sign language meanings in image files and generate realistic voice of words.
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

#### - Detect sign language meanings on a live video (via webcam).
- run the livefeed detection script;
```
  python livefeed_detection.py
```
My default port number is 88. To specify the port on which DeepStack server is running, run this instead;
```
  python livefeed_detection.py --deepstack-port port_number
```
This will spin up the webcam and would automatically detect any sign language words in view of the camera,
while also displaying the sign meaning and returning its speech equivalent immediately through the PC's audio system. Press `**q**` to quit the live video.

https://user-images.githubusercontent.com/45284829/139852351-23bf2759-409c-49f5-8941-66ce88b5acf9.mp4


## Citation
```
@inproceedings{ijcai2022p855,
  title     = {Sign-to-Speech Model for Sign Language Understanding: A Case Study of Nigerian Sign Language},
  author    = {Kolawole, Steven and Osakuade, Opeyemi and Saxena, Nayan and Olorisade, Babatunde Kazeem},
  booktitle = {Proceedings of the Thirty-First International Joint Conference on
               Artificial Intelligence, {IJCAI-22}},
  publisher = {International Joint Conferences on Artificial Intelligence Organization},
  editor    = {Lud De Raedt},
  pages     = {5924--5927},
  year      = {2022},
  month     = {7},
  note      = {Demo Track},
  doi       = {10.24963/ijcai.2022/855},
  url       = {https://doi.org/10.24963/ijcai.2022/855},
  ```
