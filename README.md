<<<<<<< HEAD
# Viswakarma — PPE Safety Detection

A webcam-based Personal Protective Equipment (PPE) detection project using Python, OpenCV, and Ultralytics YOLO.

## Features

- Live webcam detection
- Trained PPE detection model
- Bounding-box visualization and confidence filtering
- Keyboard shortcut `Q` to close the camera window

## Detected classes

The model is configured for 11 classes, including helmets, goggles, gloves, vests, boots, people, and labels for missing protective equipment.

## Project structure

```text
HCI-2.O/
├── datasets/
│   └── construction-ppe/
├── models/
│   └── best.pt
├── ppe_live.py
├── requirements.txt
└── README.md
```

## Setup on Ubuntu

```bash
sudo apt install python3-venv python3-pip
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run the detector

```bash
python ppe_live.py
```

Ensure your webcam is connected and available. Press `Q` to exit the detection window.

## Notes

- The trained model is stored at `models/best.pt`.
- Detection accuracy depends on training data, lighting, camera angle, and confidence threshold.
- This project is a prototype and should not be treated as the sole means of enforcing workplace safety.

## License

Review the applicable licenses for the dataset, model, and dependencies before redistribution.
=======
# HCI-2.O
Zenvia is a multimodal AI system that understands human intent through voice, gestures, vision, and sensors. It uses contextual reasoning and safety verification to convert intentions into safe physical or digital actions with real-time feedback, enabling natural, accessible, and intelligent human-machine interaction.
>>>>>>> origin/main
