#!/usr/bin/env python
import os,sys
path = os.path.dirname(sys.argv[0])
os.chdir(path)

try:
	from moviepy.editor import *
except:
	os.system(f'pip install moviepy')
	from moviepy.editor import *




result_dir = "result"
support_video_size = [(9,16),(3,5),(3,4)]
# 得到本文件所处文件夹下所有的视频文件
# 返回的是视频的相对路径
def GetAllVideoPaths():
	videoPaths = []
	for file in os.listdir('.'):
		if IsVideo(file):
			videoPaths.append(file)

	return videoPaths

# 判断文件是否是视频文件
def IsVideo(path):
	suffix = os.path.splitext(path)[1]
	supportVideoSuffix = [".mp4",".mov"]
	if suffix in supportVideoSuffix:
		return True
	else:
		return False


#从用户那里得到目标视频的尺寸
def GetTargetVideoSize():
	print("请选择你的目标尺寸，并输入它前面的编号")
	print("例如想要转换成9:16的，请输入1，并按回车键")
	print("退出请输入0")
	for index in range(len(support_video_size)):
		chooseStr = (str(index+1) + "." + str(support_video_size[index][0]) + ":" + str(support_video_size[index][1]))
		print(chooseStr)
	while(True):
		try:
			choose = int(input("请输入目标尺寸前的编号："))
			if(choose == 0):
				return ()
			return support_video_size[choose-1]
		except:
			print("请输入正确的序号!!!")


# 将视频文件转换成目标尺寸
def ConvertToTargetSize(path,targetSize):
	clip = VideoFileClip(path)
	originalRatio = clip.w / clip.h
	targetRatio = targetSize[0] / targetSize[1]
	newHeight = clip.h
	newWidth = clip.w
	# height 太小了，根据height来算
	if originalRatio > targetRatio:
		newWidth = clip.h * targetRatio
	else:
		newHeight = newWidth / targetRatio

	newClip = clip.crop(x_center = clip.w / 2,y_center = clip.h/2,width = newWidth,height = newHeight)
	if(not os.path.exists(result_dir)):
		os.mkdir(result_dir)
	out = os.path.join(result_dir,path)
	newClip.write_videofile(out)

# 处理主模块
def Main():

	targetSize = GetTargetVideoSize()
	if(len(targetSize) == 0):
		print("已退出...")
	else:
		videoPaths = GetAllVideoPaths();
		print("开始处理...")
		for path in videoPaths:
			print("正在处理 " + path)
			ConvertToTargetSize(path,targetSize)
			print(path + "处理完成")
		print("所有文件已经处理完成!")

Main()

