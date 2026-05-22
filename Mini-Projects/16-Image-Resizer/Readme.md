# Multithreaded Image Resizer & Converter

Built as a part of my learning journey
A Python project that resizes and converts multiple images simultaneously using multithreading and worker queues.

# Features Implemented

## Current Features

- Batch image processing
- Multithreaded resizing
- Queue-based worker system
- Thread-safe printing using locks
- Automatic processing of all images inside input folder
- Output images saved into output folder
- Image resizing using Pillow
- Worker pool architecture

# Project Structure

```text
16-Image-Resizer/
│
├── input/
├── output/
├── main.py (Try latest version for best results)
└── README.md
```

# How To Run

## Prerequisite - Install Pillow

```bash
pip install pillow
```

## Step 1

Place images inside:

```text
input/
```

---

## Step 2

Run program:

```bash
python main.py
```

---

## Step 3

Processed images will appear inside:

```text
output/
```


# Planned Improvements

- Better exception handling
- Progress tracking
- Execution timer
- Dynamic worker count
- Format conversion support
- Image compression options
- Preserve metadata
- GUI version using Tkinter
- Drag & drop support
- Recursive directory processing

# Example Output

```text
cat.png resized successfully.
dog.jpg resized successfully.
car.webp resized successfully.

All images processed.