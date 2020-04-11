#include<iostream>
#include<string>
#include<opencv2/core.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>


using namespace cv;
using namespace std;

String faceCascadePath;
CascadeClassifier faceCascade;

void detectFaceOpenCVHaar(CascadeClassifier faceCascade, Mat &frameOpenCVHaar, int inHeight=300, int inWidth=0)
{
	int frameHeight = frameOpenCVHaar.rows;
	int frameWidth = frameOpenCVHaar.cols;
	if (!inWidth)
		inWidth = (int)((frameWidth / (float)frameHeight)*inHeight);

	float scaleHeight = frameHeight / (float)inHeight;
	float scaleWidth = frameWidth / (float)inWidth;

	Mat frameOpenCVHaarSmall, frameGray;
	resize(frameOpenCVHaar, frameOpenCVHaarSmall, Size(inWidth, inWeight));
	cvtColor(frameOpenCVHaarSmall, frameGray, COLOR_BGR2GRAY)

	vector<Rect> faces;
	faceCascade.detectMultiScale(frameGray, faces);

	// Loop through all faces
	// Draw rectangles
}
