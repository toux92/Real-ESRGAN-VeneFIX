from google.colab import drive
import os

# Monta Google Drive
drive.mount('/content/drive')

# Definisci le cartelle
input_folder = '/content/drive/MyDrive/AI_Works/Real_Esrgan_Video/Real-Esrgan_UPLOAD'
output_folder = '/content/drive/MyDrive/AI_Works/Real_Esrgan_Video/Real-Esrgan_DOWNLOAD'

# Verifica se ci sono video da elaborare
video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]

# Esegui l'inferenza su ciascun video
for video in video_files:
    input_path = os.path.join(input_folder, video)
    output_name = os.path.splitext(video)[0] + '_outx2.mp4'
    output_path = os.path.join(output_folder, output_name)

    # Esegui il comando di inferenza con `outscale` 2
    os.system(f"python3 inference_realesrgan_video.py -i {input_path} -n realesr-animevideov3 -s 2 --suffix outx2")
    
    # Sposta il file di output nella cartella di destinazione
    os.rename(output_path, os.path.join(output_folder, output_name))
