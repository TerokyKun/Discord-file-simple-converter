# 🎬 Discord File Simple Converter

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FFmpeg](https://img.shields.io/badge/FFmpeg-required-green)

Простой Python CLI-инструмент для работы с видео через FFmpeg.

---

## ⚙️ Требования

- Python 3.8+
- FFmpeg (с ffprobe)

Проверка:

ffmpeg -version
ffprobe -version

---

## 🚀 Запуск

python main.py <файл> [опции]

---

## 🧑‍💻 Использование

# Разбить видео (~8 МБ)
python main.py video.mp4 --split --size 8

# Сжать видео (~8 МБ)
python main.py video.mp4 --optimize --size 8

# Сжать + разбить
python main.py video.mp4 --optimize --split --size 8

---

## 📁 Результат

optimized.mp4
output/part_1.mp4
output/part_2.mp4
...

---

## ⚠️ Ошибки

FFmpeg не найден → добавить в PATH
Файл не найден → проверить путь
Нет флагов → указать --split или --optimize

---

# 🇺🇸

# 🎬 Video Tool

Simple Python CLI tool for video processing with FFmpeg.

---

## ⚙️ Requirements

- Python 3.8+
- FFmpeg (with ffprobe)

Check:

ffmpeg -version
ffprobe -version

---

## 🚀 Usage

python main.py <file> [options]

---

## 🧑‍💻 Examples

# Split (~8 MB)
python main.py video.mp4 --split --size 8

# Compress (~8 MB)
python main.py video.mp4 --optimize --size 8

# Compress + split
python main.py video.mp4 --optimize --split --size 8

---

## 📁 Output

optimized.mp4
output/part_*.mp4

---

## ⚠️ Errors

FFmpeg not found → add to PATH
File not found → check path
No flags → use --split or --optimize
