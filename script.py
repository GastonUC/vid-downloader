import ffmpeg
import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox

def download_video(url, output_path='video'):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path + '.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_ext = info_dict.get('ext', 'mkv')
        video_title = info_dict.get('title', 'video').replace(' ', '_')
        downloaded_video = f"{output_path}.{video_ext}"

    converted_video = f"{video_title}.mp4"
    ffmpeg.input(downloaded_video).output(converted_video).run()
    os.remove(downloaded_video)
    
    print(f"Video downloaded and converted successfully at {converted_video}")
    return converted_video

def download_videos():
    urls = url_entry.get("1.0", tk.END).strip().split('\n')
    for url in urls:
        if url:
            try:
                download_video(url)
                messagebox.showinfo("Success", f"Video downloaded and converted successfully for URL: {url}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download video for URL: {url}\n{e}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place the URL entry widget
tk.Label(root, text="Enter YouTube URLs (one per line):").pack(pady=5)
url_entry = tk.Text(root, height=10, width=50)
url_entry.pack(pady=5)

# Create and place the download button
download_button = tk.Button(root, text="Download", command=download_videos)
download_button.pack(pady=20)

# Run the application
root.mainloop()


# import yt_dlp
# import ffmpeg
# import os

# def download_video(url, output_path='video'):
#     ydl_opts = {
#         'format': 'bestvideo+bestaudio/best',
#         'outtmpl': output_path + '.%(ext)s'
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(url, download=True)
#         video_ext = info_dict.get('ext', 'mkv')
#         video_title = info_dict.get('title', 'video').replace(' ', '_')
#         downloaded_video = f"{output_path}.{video_ext}"

#     converted_video = f"{video_title}.mp4"
#     ffmpeg.input(downloaded_video).output(converted_video).run()
#     os.remove(downloaded_video)
#     # ydl.download([url])
#     print(f"Video downloaded and converted successfully at {converted_video}")
#     return converted_video

# youtube_url = "https://www.youtube.com/watch?v=fOAIrUZbOwo"
# download_video(youtube_url)