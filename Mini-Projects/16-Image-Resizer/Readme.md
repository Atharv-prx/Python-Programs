# Multithreaded Image Resizer & Converter

Built as a part of my learning journey
A multithreaded image processing tool that resizes and converts images in bulk using worker threads and queue-based task management

# Supported Formats

- PNG
- JPG
- JPEG
- WEBP

# How To Run

## Step 1

Make 2 folders named input and output, use version-4-main.py for best results.
Place images inside:

```text
input/
```

## Step 2

Run the program:

```bash
python main.py
```

## Step 3

Choose:
- output format
- width
- height

## Step 4

Processed images appear inside:

```text
output/
```

# Future Improvements

## Performance & Threading
- Dynamic worker count
- Better queue shutdown system
- Compression quality settings
- Custom aspect ratio modes
- Crop mode

Possible GUI features:
- file explorer
- live preview
- progress tracking
- drag & drop
- image comparison