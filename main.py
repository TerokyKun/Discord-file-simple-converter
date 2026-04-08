import subprocess
import math
import os
import argparse

# 👉 если ffmpeg в PATH — оставь так
FFMPEG = "ffmpeg"
FFPROBE = "ffprobe"


def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd).decode().strip()
    except FileNotFoundError:
        print("❌ ffmpeg/ffprobe не найден. Добавь в PATH.")
        exit()


def get_duration(filename):
    cmd = [
        FFPROBE,
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        filename
    ]
    return float(run_cmd(cmd))


def get_filesize(filename):
    return os.path.getsize(filename)


def split_video(input_file, chunk_mb):
    size_bytes = get_filesize(input_file)
    parts = math.ceil(size_bytes / (chunk_mb * 1024 * 1024))

    duration = get_duration(input_file)
    chunk_duration = duration / parts

    os.makedirs("output", exist_ok=True)

    for i in range(parts):
        start = i * chunk_duration
        output_file = f"output/part_{i+1}.mp4"

        cmd = [
            FFMPEG,
            "-y",
            "-ss", str(start),
            "-i", input_file,
            "-t", str(chunk_duration),
            "-c", "copy",
            output_file
        ]

        subprocess.run(cmd)

    print(f"✅ Разбито на {parts} частей")


def optimize_video(input_file, target_mb):
    duration = get_duration(input_file)

    # переводим размер в битрейт
    target_bits = target_mb * 1024 * 1024 * 8
    bitrate = target_bits / duration  # бит/сек

    # чуть уменьшаем (чтобы точно влезло)
    bitrate = int(bitrate * 0.95)

    output_file = "optimized.mp4"

    cmd = [
        FFMPEG,
        "-y",
        "-i", input_file,
        "-b:v", str(bitrate),
        "-bufsize", str(bitrate),
        "-maxrate", str(bitrate),
        "-preset", "fast",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "128k",
        output_file
    ]

    subprocess.run(cmd)

    print(f"✅ Оптимизировано: {output_file}")


# ---------------- CLI ----------------

parser = argparse.ArgumentParser(description="Video tool")

parser.add_argument("input", help="Входной файл")

parser.add_argument("--split", action="store_true", help="Разбить видео")
parser.add_argument("--optimize", action="store_true", help="Сжать до размера")

parser.add_argument("--size", type=int, default=8, help="Размер в МБ (по умолчанию 8)")

args = parser.parse_args()

if not os.path.exists(args.input):
    print("❌ Файл не найден")
    exit()

if not args.split and not args.optimize:
    print("❗ Укажи хотя бы --split или --optimize")
    exit()

if args.optimize:
    optimize_video(args.input, args.size)

if args.split:
    split_video(args.input, args.size)

print("🚀 Готово")