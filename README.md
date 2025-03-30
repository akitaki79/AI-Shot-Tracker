# Basketball Shot Tracker

This project uses **YOLOv8** (You Only Look Once) and computer vision techniques to detect and track basketball shots in video footage. It identifies the basketball and hoop, tracks the movement of the ball, and counts shots made based on the ball's trajectory. 


## How it Works
I used a pretrained YOLOv8 model (best.pt). The model detects basketballs (class 0) and hoops (class 1) in each frame of the video. It tracks the position of the ball over time, maintaining the last 10 positions. When the ball moves from below the hoop to above the hoop, and certain conditions are met (e.g., proximity to hoop), a shot is counted. The app displays the total shots attempted and shots made on the screen in real-time.

## Setup

Follow these steps to set up the project on your local machine.

1) Clone the repository:
```bash
git clone https://github.com/yourusername/basketball-shot-tracker.git
cd basketball-shot-tracker
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the program!
```bash
python3 main.py 
```

NOTE: This program uses a model I pretrained. You can also train your own model and implement it if you'd like.

## Usage

After running the program, you will be prompted to upload a video. Once uploaded, a window will pop up where the model detects and tracks the shots. Its simple and easy to use!

## Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request with improvements or bug fixes.

## License
This project is licensed under the MIT License.
