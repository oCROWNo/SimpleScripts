import cv2
import os
num_max = 395
num=1

 
# 输出视频的路径和名称
output_video_path = 'hand_demo.mp4'
 
# 图像文件夹路径
images_folder = '/home/admin01/Work/Temp'
 
# 获取所有图像文件的列表
# image_files = [os.path.join(images_folder, f) for f in os.listdir(images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
# aa = image_files[0].split('/')[-1].split(".")[0]
# image_files.sort()  # 确保图像按正确的顺序排序，例如 frame1, frame2, ...

image_files = [os.path.join(images_folder, f"{index+1}.png") for index in range(num_max)]
# 读取第一张图像以获取其尺寸和类型，用于视频编码器设置
first_image = cv2.imread(image_files[0])
height, width, layers = first_image.shape
 
# 视频编码器，帧率和尺寸
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用XVID编码器，你也可以尝试'DIVX', 'X264'等
fps = 30  # 帧率，可以根据需要调整
video = cv2.VideoWriter(output_video_path, fourcc, fps, (2048, 1080))
 
# 写入帧到视频文件
for image_file in image_files:
    image = cv2.imread(image_file)
    video.write(image)  # 将图像写入视频文件
 
# 释放VideoWriter对象
video.release()