# CaféCraft - Interactive Coffee Learning Game

CaféCraft is an interactive web application that teaches users about different types of coffee drinks in a fun, game-like environment. Users can learn about various coffee types, take quizzes, and track their progress through an energy meter system.

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/Lyxxx2003/s25-uid-project.git
cd s25-uid-project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python server.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Features

- Interactive learning experience with pixel art graphics
- Progressive lesson system about coffee types
- Quiz system to test knowledge
- Energy meter to track progress
- Responsive design that works on all devices
- User progress tracking
- Crafting table for creating coffee drinks

## Project Structure

```
s25-uid-project/
├── server.py              # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── main.css      # Main stylesheet
│   ├── js/
│   │   └── main.js       # Main JavaScript file
│   ├── images/           # Game images and assets
│   └── data/
│       ├── game_data.json # Game content and recipes
│       └── quiz.json     # Quiz questions and answers
├── templates/
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   ├── enter_name.html   # Name entry page
│   ├── loading.html      # Loading screen
│   ├── introduction.html # Introduction page
│   ├── recipes.html      # Recipes page
│   ├── learn.html        # Learning page
│   ├── craft.html        # Crafting page
│   ├── feedback.html     # Feedback page
│   ├── quiz.html         # Quiz page
│   └── certificate.html  # Certificate page
└── venv/                 # Virtual environment (not tracked in git)
```

## Game Flow

1. **Introduction**: Players enter their name and learn about the game
2. **Learning**: Players learn about different coffee types and their ingredients
3. **Crafting**: Players practice making coffee drinks using the crafting table
4. **Quiz**: Players test their knowledge through interactive quizzes
5. **Certificate**: Players receive a certificate upon completing the game

## Development

- Built with Flask 3.0.0
- Uses Bootstrap 5.3.0 for responsive design
- jQuery 3.6.0 for DOM manipulation
- Custom CSS for game styling
- JSON files for game data management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
