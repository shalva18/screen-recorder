# Screen Recorder

A simple Python screen recorder that captures your main monitor and saves the recording as an MP4 video.

## Features

- Records the primary monitor at 20 FPS
- Saves the output as `recording.mp4`
- Stops cleanly with `Ctrl+C`, so the video file is always saved properly

## Built With

- [Python 3](https://www.python.org/)
- [mss](https://github.com/BoboTiG/python-mss) for fast screen capture
- [OpenCV](https://opencv.org/) for video encoding
- [NumPy](https://numpy.org/) for frame processing

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Git

### Installation

```bash
git clone https://github.com/shalva18/screen-recorder.git
cd screen-recorder
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

Recording starts immediately. Press `Ctrl+C` in the terminal to stop. The video is saved as `recording.mp4` in the project folder.

## Configuration

You can change these values at the top of `main.py`:

| Variable | Default         | Description                |
|----------|-----------------|----------------------------|
| `FPS`    | `20.0`          | Frames per second          |
| `OUTPUT` | `recording.mp4` | Name of the output file    |

## How It Works

1. `mss` grabs a screenshot of the primary monitor in a loop.
2. Each frame is converted from BGRA to BGR with OpenCV.
3. Frames are written to an MP4 file with `cv2.VideoWriter`.
4. A small sleep keeps the loop close to the target FPS.

## Roadmap

- [ ] Start/Stop buttons (GUI with `tkinter`)
- [ ] Audio recording
- [ ] Select which monitor or screen region to record
- [ ] Configurable settings from the command line

## Limitations

- Records video only (no audio yet)
- Records the primary monitor only

## Author

Created by [shalva18](https://github.com/shalva18).
