import os
from deepface import DeepFace
import cv2
import register

models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
metrics = ["cosine", "euclidean", "euclidean_l2"]

#result=DeepFace.verify(img1_path='./Db/im1.jpeg', img2_path='./Db/im2.jpg',model_name=models[1])

val=input("Click R for registering new face:")


path="./Db/"
if val=='R':
	name=input("Enter the Employee id:")
	if name in os.listdir(path):
		print("Your Employee id is already registered")
	else:
		os.makedirs(f'./Db/{name}')
		path1=f"./Db/{name}/"
		val=register.Register(path1,name)
		if val:
			print("Your face is registered successfully")


DeepFace.stream(db_path='./Db')
#print(result)