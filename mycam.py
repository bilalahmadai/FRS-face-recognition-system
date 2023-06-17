import cv2 as cv
import pickle
import face_recognition
import numpy as np
import cvzone 
import os
cap=cv.VideoCapture(1)

# print(imgIDs)
bgImg=cv.imread("assets/bg.png")
bgInfo=cv.imread("assets/bgInfo.png")

dataPath="data"
dataList=os.listdir(dataPath)

imgProfile=[]
for pimg in dataList:
    imgProfile.append(cv.imread(os.path.join(dataPath,pimg)))

# print(imgProfile)
def webCam():
    print("Encoded File Loading...")
    file=open("encoder/EncodeFile.p","rb")
    model=pickle.load(file)
    file.close()
    print("Encoded File Loaded")
    knownEncodeList,imgIDs = model
    while True:
        success, img = cap.read()
        img = cv.resize(img, (720, 520)) #w,h
        
        imgS=cv.resize(img,(0,0),None,0.25,0.25) #scaling image to 1/4 th
        imgS=cv.cvtColor(imgS,cv.COLOR_BGR2RGB)

        faceCurLoc=face_recognition.face_locations(imgS)
        encodeCurFrame=face_recognition.face_encodings(imgS,faceCurLoc)

        bgImg[140:140+520,50:50+720]=img #y:h,x:w
        bgImg[42:42+635,855:855+380]=bgInfo #y:h,x:w
    
        for encodeFace, faceLoc in zip(encodeCurFrame,faceCurLoc):
            matches=face_recognition.compare_faces(knownEncodeList,encodeFace)
            faceDis=face_recognition.face_distance(knownEncodeList,encodeFace)
            
            matchIndex=np.argmin(faceDis)
            print("FacDisList",faceDis)
            # print("FacDis index ",faceDis[matchIndex])

            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            bbox= 50+x1,140+y1,x2-x1,y2-y1
            
            
            if (matches[matchIndex] and faceDis[matchIndex]<=0.50):

                pimg = cv.resize(imgProfile[matchIndex], (234, 234))
                bgImg[125:125+234,928:928+234]=pimg #y:h,x:w
                # print("imgPath: ",imgProfile[matchIndex])
                #getting Text and Center it to InfoBox
                (w,h),_=cv.getTextSize(imgIDs[matchIndex],cv.FONT_HERSHEY_COMPLEX,1,1)
                offset=(380-w)//2
                cv.putText(bgImg,imgIDs[matchIndex].upper(),(855+offset,400),cv.FONT_HERSHEY_COMPLEX,1,(94,4,3),1)

                #cvZone provide beautiful BoundingBox 
                cvzone.cornerRect(bgImg,bbox,rt=1,t=5,colorR=(220,218,168),colorC=(216,180,0))
            
            else:
                
                cvzone.cornerRect(bgImg,bbox,rt=0,t=5,colorC=(70,57,230))
                (w,h),_=cv.getTextSize("UnKnown",cv.FONT_HERSHEY_COMPLEX,1,1)
                offset=(380-w)//2
                cv.putText(bgImg,"UnKnown",(855+offset,400),cv.FONT_HERSHEY_COMPLEX,1,(70,57,230),1)



        cv.imshow("Face Recogniton",bgImg)
        if cv.waitKey(1) == ord('q'):
            break
        
    cv.destroyAllWindows()




if __name__ == "__main__":
    print("--------webcam.py-------")