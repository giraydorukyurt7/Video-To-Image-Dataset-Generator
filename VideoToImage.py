import cv2 as cv
import os

# Turn your video into images
# filename: example-> "xyz.mp4"
# frame_rate: -----> Photos_Saved_Per_Second ~= Video_FPS / Frame_Rate
# output_folder: Name of your folder. It generates an additional folder inside this folder named as same as your video.
def VideoToImage(filename, frame_rate=10, output_folder="Image_Dataset"):
    video_path = "Video_Dataset/"+filename

    #take video name
    video_name=os.path.splitext(os.path.basename(video_path))[0] #extension like ".mp4"
    video_output_folder = os.path.join(output_folder, video_name) #create Image_Dataset/{video_name}
    os.makedirs(video_output_folder, exist_ok=True)

    video_capture = cv.VideoCapture(video_path)

    frame_count = 0
    img_no = 1
    while True:
        succes, frame = video_capture.read()
        if not succes:
            break
        #save frames
        if frame_count % frame_rate == 0:
            frame_name = os.path.join(video_output_folder, f"{video_name}_{img_no}.jpg")
            cv.imwrite(frame_name, frame)
            img_no+=1
        frame_count+=1

    video_capture.release()
    print(f"All frames saved into {video_output_folder} folder.")

#Example use
#VideoToImage(filename="VID_20241206_200412.mp4", frame_rate=20, output_folder="Image_Dataset")