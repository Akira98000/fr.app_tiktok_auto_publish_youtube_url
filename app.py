from flask import Flask, render_template, request, jsonify
from pytube import YouTube
import moviepy.editor as mp
import os
import math 
import time
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url'] 
    try:
        download_video(url)
        return jsonify({"success": True, "message": "Vidéo téléchargée et dossier créé."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/split', methods=['POST'])
def split():
    try:
        split_video()
        return jsonify({"success": True, "message": "Vidéo découpée si nécessaire."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

def download_video(url, base_folder="download"):
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4").first()
    n = len(os.listdir(base_folder)) + 1
    folder_name = os.path.join(base_folder, f"tiktok-vdo-aki-{n}")
    os.makedirs(folder_name, exist_ok=True)
    
    print(f"Downloading video to: {folder_name}")
    video.download(folder_name)

def split_video(base_folder="download"):
    latest_folder = sorted([d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))])[-1]
    latest_folder_path = os.path.join(base_folder, latest_folder)
    video_path = os.path.join(latest_folder_path, os.listdir(latest_folder_path)[0])
    video = mp.VideoFileClip(video_path)
    clip_duration = 60 
    num_clips = math.ceil(video.duration / clip_duration)
    for i in range(num_clips):
        start_time = i * clip_duration
        end_time = (i + 1) * clip_duration
        end_time = min(end_time, video.duration)
        subclip = video.subclip(start_time, end_time)
        subclip.write_videofile(os.path.join(latest_folder_path, f"part{i+1}.mp4"))

def upload_to_tiktok(video_path):
    pass

def schedule_upload(base_folder="download"):
    latest_folder = sorted([d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))])[-1]
    latest_folder_path = os.path.join(base_folder, latest_folder)

    video_parts = sorted([v for v in os.listdir(latest_folder_path) if v.startswith("part")])
    start_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)

    for i, video_part in enumerate(video_parts):
        upload_time = start_time + timedelta(hours=i)
        while datetime.now() < upload_time:
            time.sleep(30)  
        video_path = os.path.join(latest_folder_path, video_part)
        upload_to_tiktok(video_path)

if __name__ == '__main__':
    app.run(debug=True)
