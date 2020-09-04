"""
q1_init.py

TODO: Describe what this script does

The script takes in images for query blob and set of blobs from the folder and extracts the features of these images.
The features are stored in a dictionary data type along with the blob names.
The blobs are then classified based on their similarity w.r.t the query blob and returned as a tuple of two lists
"""

import argparse
import os
import math
import cv2
import numpy as np

def main():
    """
    Extracts various features from a cv2 image and returns them in a list.
    :param None
    :return: A tuple containing two lists: containing the most similar and the least similar blobs wrt the query blob.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--blob_set", required=True, help="The path to the blob_set directory")
    parser.add_argument("--query_blob", required=True, help="The file path to the query blob")
    args = parser.parse_args()

    # Define input arguments
    blob_set_dir = args.blob_set
    query_blob_path = args.query_blob


    query_blob = cv2.imread(query_blob_path)
    query_features = blob_feature_extractor(img=query_blob)
    blob_img_paths = [blob_path for blob_path in os.listdir(blob_set_dir) if blob_path.endswith(".png")]
    blob_set_feature_vectors = {}

    #Assemble dictionary of feature vectors
    for blob_path in blob_img_paths:
        # Open the blob and extract its features (ask nicely)
        blob = cv2.imread('blob_set/'+blob_path)
        feature_vector = blob_feature_extractor(img=blob)
        

        blob_set_feature_vectors[os.path.basename(blob_path)] = feature_vector
    
# TODO: Compare feature vectors and determine which blob is most and least similar to the query blob
    print('The extracted features of the query blob are: Area, Perimeter, Circularity, Aspect Ratio respectively \n',query_features)
    most_similar=[]
    least_similar=[]
    for blob, feature_vector in blob_set_feature_vectors.items():
        if ((query_features[0][0]-100<=feature_vector[0][0]) and (query_features[0][0]+100>=feature_vector[0][0])):
            if ((query_features[0][2]-0.15<=feature_vector[0][2]) and (query_features[0][2]+0.15>=feature_vector[0][2])):
                if ((query_features[0][3]-0.3<=feature_vector[0][3]) and (query_features[0][3]+0.3>=feature_vector[0][3])):
                    most_similar.append(blob)
        else:
            least_similar.append(blob)
    return most_similar,least_similar


def blob_feature_extractor(img):
    """
    Extracts various features from a cv2 image and returns them in a list.
    :param img: A cv2 image of a blob.
    :return: A list where each element represents a unique feature in the image.
    """

    # TODO: extract the features
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    

    ret,thresh = cv2.threshold(imgray,127,255,0)
    _,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    
    cnt = contours[0]
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt,True)
    circularity=4*math.pi*area/perimeter**2
    
    
    Convexity = cv2.isContourConvex(cnt)

    
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    aspectR = math.sqrt( ((box[0][0]-box[1][0])**2)+((box[0][1]-box[1][1])**2) )/(math.sqrt( ((box[2][0]-box[1][0])**2)+((box[2][1]-box[1][1])**2) ))
    values=[area,perimeter,circularity,aspectR]
    feature_vector = []
    feature_vector.append(values)

    return feature_vector


if __name__ == '__main__':
    most_similar,least_similar=main()
    print('\n The',len(most_similar),'Most similar blobs w.r.t the query blob are: \n',most_similar,'\n')
    print('The',len(least_similar),'Least similar blobs w.r.t the query blob are: \n',least_similar)