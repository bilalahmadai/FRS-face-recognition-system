import cv2 as cv
import face_recognition
import pickle
import os
# dataPath="data"
dataPath="data"

dataList=os.listdir(dataPath)

print(dataList)
imgList=[]
studentIDs=[]
for img in dataList:
    # print(os.path.join(dataPath,img))
    imgList.append(cv.imread(os.path.join(dataPath,img)))
    # print(os.path.splitext(img))
    # print(os.path.splitext(img)[0])
    studentIDs.append(os.path.splitext(img)[0])
print("studentIDs : ",studentIDs)

# making encode of images
def findEncodings(imgList):
    encodeList=[]
    for img in imgList:
        img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def myencoder():
    print("encoding started...")
    knownEncodeList=findEncodings(imgList)
    print("encoding completed")

    filename='encoder/EncodeFile.p'
    if os.path.exists(filename):
        # Delete the file
        os.remove(filename)

    model=[knownEncodeList,studentIDs]
    file=open(filename,"wb")
    pickle.dump(model,file)
    file.close()
    print("Model Saved")

if __name__ == "__main__":
    print("--------encoder.py-------")