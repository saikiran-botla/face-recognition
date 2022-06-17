import cv2
import os 

def Register(path,name):
	vid=cv2.VideoCapture(0)

	count=0
	picount=0

	while(True):

		ret,frame=vid.read()

		cv2.imshow("Register Your face",frame)
		count+=1
		if count%23==12:
			cv2.imwrite(os.path.join(path,name+str(picount)+'.jpg'),frame)
			picount+=1
			if(picount==30):
				vid.release()
				cv2.destroyAllWindows()
				return True


		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	vid.release()
	cv2.destroyAllWindows()