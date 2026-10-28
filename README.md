This project is the implementation of a Damped Harmonic Oscillator Analyzer developed for the Physics course. The objective is to analyze frame-by-frame data to determine physical relationships and constants of the system, applying the equations of damped harmonic motion.

All analysis data—such as time, x-position, and y-position—are read from an external video. This allows users to process different experimental datasets without needing to modify the source code.

## Authorship

The core physics of the program and the data analysis logic were fully implemented by me. The data processing, mathematical fitting, and graphical rendering rely on the following external open-source Python libraries:
* **OpenCV**: For frame-by-frame video analysis and data extraction.
* **NumPy & Pandas**: For data structuring, matrix operations, and dataset manipulation.
* **SciPy (curve_fit)**: For fitting the experimental data to the damped harmonic oscillator equation.
* **Matplotlib**: For plotting and graphical visualization of the results.

## How to Use

1. Clone this repository to your local machine.
2. Open the project folder in Visual Studio Code.
3. Make sure you have the required compiler or interpreter installed on your machine.
4. Edit your video file (e.g., `video.mp4`) to the right name.
5. Open the VS Code terminal and compile/run the project:

    ```bash
    # Replace with your specific run command (e.g., for Python)
    python project.py
    ```
