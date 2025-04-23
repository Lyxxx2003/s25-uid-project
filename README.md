# CaféCraft - Interactive Coffee Learning Game

CaféCraft is an interactive web application that teaches users about different types of coffee drinks in a fun, game-like environment. Users can learn about various coffee types, take quizzes, and track their progress through an energy meter system.

## Features

- Interactive learning experience with pixel art graphics
- Progressive lesson system about coffee types
- Quiz system to test knowledge
- Energy meter to track progress
- Responsive design that works on all devices
- User progress tracking

## Requirements

- Python 3.8+
- Flask
- Modern web browser

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd cafecraft
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python app.py
```
3. Open your web browser and navigate to `http://localhost:5000`

## Project Structure

```
cafecraft/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── js/
│   │   └── main.js       # Custom JavaScript
│   ├── images/           # Game images
│   └── data/
│       └── game_data.json # Game content
│       └── lessons.json # Lessons content
│       └── quiz.json # Quiz content
└── templates/
    ├── base.html         # Base template
    ├── home.html         # Home page
    ├── learn.html        # Learning page
    ├── quiz.html         # Quiz page
    └── results.html      # Results page
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE)
