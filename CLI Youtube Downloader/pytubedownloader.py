import yt_dlp
import os

def download_video(url, resolution, save_path="."):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # yt-dlp format string: bestvideo with resolution + bestaudio, merged
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'merge_output_format': 'mp4',  # ensures video+audio is merged
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("\nDownload complete.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("🔗 Enter YouTube video URL: ").strip()
    resolution = input("Enter max resolution (e.g., 720, 480, 360): ").strip()
    save_path = input("Enter save directory (leave blank for current): ").strip() or "."

    download_video(url, resolution, save_path)
