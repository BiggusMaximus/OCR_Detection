import cv2
import argparse
import os

# Take a n number of picture, --position_taken the position the photo was taken, --reset deleting all the images in folder
parser = argparse.ArgumentParser()
parser.add_argument('--n_photo', type=int,
                    help='Take n number of photo')
parser.add_argument('--position_taken', type=str,
                    help='In what position camera is taken')
parser.add_argument('--reset', action='store_true',
                    help='Deleting all the photo')
arg = parser.parse_args()

cam             = cv2.VideoCapture(0)
result, img     = cam.read()

count = 0
pictureTake_dir = "takePicture" 
pictureTake_path = os.path.join(os.getcwd(), pictureTake_dir)

if os.path.exists(pictureTake_path):
    if arg.n_photo == None :
        print("Please inserting number of photo")
    else:
        for i in range(arg.n_photo):
            cv2.imwrite(f"{pictureTake_path}\picture_{str(count)}_{arg.position_taken}.jpg", img)
            print(f"picture taken {str(count)}")
            count = count + 1
else:
   os.mkdir(os.path.join(os.getcwd(), pictureTake_path))

if arg.reset == True :
    for file_name in os.listdir(pictureTake_path):
        file = os.path.join(pictureTake_path, file_name)
        if file.endswith('.jpg'):
            print('Deleting file:', file)
            os.remove(file)