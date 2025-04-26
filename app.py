from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key in production

# Load game data
with open('static/data/game_data.json', 'r') as f:
    game_data = json.load(f)

# Game state
class GameState:
    def __init__(self):
        self.caffeine_level = 1
        self.recipes_unlocked = ["espresso"]  # Start with espresso unlocked
        self.inventory = {
            "coffee_beans": 5,
            "water": 5,
            "milk": 5,
            "chocolate_syrup": 3,
            "whipped_cream": 3
        }
        self.name = ''
        self.current_recipe = None
        self.has_seen_intro = False  # Track if user has seen introduction

# Initialize game state
game_state = GameState()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start', methods=['POST'])
def start():
    game_state.name = request.form.get('name', '')
    return redirect(url_for('enter_name'))

@app.route('/enter_name', methods=['GET', 'POST'])
def enter_name():
    if request.method == 'POST':
        game_state.name = request.form.get('name', '')
        return redirect(url_for('loading'))
    return render_template('enter_name.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/introduction')
def introduction(): 
    return render_template('introduction.html',
                         name=game_state.name,
                         caffeine_level=game_state.caffeine_level)

@app.route('/introduction_backpack')
def introduction_backpack():
    return render_template('introduction_backpack.html', 
                         name=game_state.name,
                         caffeine_level=game_state.caffeine_level,
                         dr_coffee=game_data["characters"]["dr_coffee"])

@app.route('/introduction_table')
def introduction_table():
    game_state.has_seen_intro = True  # Mark introduction as seen
    return render_template('introduction_table.html',
                         name=game_state.name,
                         caffeine_level=game_state.caffeine_level,
                         dr_coffee=game_data["characters"]["dr_coffee"])

@app.route('/recipes')
def recipes():
    recipe_sequence = ["espresso", "americano", "macchiato", "latte", "mocha"]
    all_unlocked = set(recipe_sequence).issubset(set(game_state.recipes_unlocked))  # Check if all recipes are unlocked
    return render_template('recipes.html',
                         name=game_state.name,
                         game_data=game_data,
                         unlocked_recipes=game_state.recipes_unlocked,
                         caffeine_level=game_state.caffeine_level,
                         all_unlocked=all_unlocked)

@app.route('/learn/<recipe_id>')
def learn(recipe_id):
    if recipe_id not in game_state.recipes_unlocked:
        return redirect(url_for('recipes'))
    
    game_state.current_recipe = recipe_id
    return render_template('learn.html',
                         name=game_state.name,
                         recipe=game_data["recipes"][recipe_id],
                         recipe_id=recipe_id,
                         items=game_data["items"],
                         caffeine_level=game_state.caffeine_level)

@app.route('/craft/<recipe_id>')
@app.route('/craft')
def craft(recipe_id=None):
    if recipe_id is None:
        recipe_id = request.args.get('recipe_id')
    
    if not recipe_id or recipe_id not in game_state.recipes_unlocked:
        return redirect(url_for('recipes'))
    
    return render_template('craft.html',
                         items=game_data["items"],
                         inventory=game_state.inventory,
                         recipe=game_data["recipes"][recipe_id],
                         recipe_id=recipe_id,
                         caffeine_level=game_state.caffeine_level)

@app.route('/craft_result', methods=['POST'])
def craft_result():
    recipe_id = request.json.get('recipe_id')
    ingredients = request.json.get('ingredients')
    
    if recipe_id not in game_state.recipes_unlocked:
        return jsonify({'success': False, 'message': 'Recipe not unlocked'})
    
    recipe = game_data["recipes"][recipe_id]
    correct_ingredients = sorted([ing for ing in recipe["ingredients"] if ing])  # Filter out None/empty values
    submitted_ingredients = sorted([ing for ing in ingredients if ing])  # Filter out None/empty values
    
    if submitted_ingredients == correct_ingredients:
        # Successful craft
        game_state.caffeine_level = min(game_state.caffeine_level + 1, 6)
        
        # Unlock next recipe if available
        recipe_sequence = ["espresso", "americano", "macchiato", "latte", "mocha"]
        current_index = recipe_sequence.index(recipe_id)
        if current_index < len(recipe_sequence) - 1:
            next_recipe = recipe_sequence[current_index + 1]
            if next_recipe not in game_state.recipes_unlocked:
                game_state.recipes_unlocked.append(next_recipe)
        
        return jsonify({
            'success': True,
            'caffeine_level': game_state.caffeine_level,
            'feedback_url': url_for('feedback', recipe_id=recipe_id)
        })
    
    return jsonify({'success': False, 'message': 'Wrong ingredients'})

@app.route('/feedback/<recipe_id>')
def feedback(recipe_id):
    if recipe_id not in game_state.recipes_unlocked:
        return redirect(url_for('recipes'))
    
    return render_template('feedback.html',
                         name=game_state.name,
                         recipe=game_data["recipes"][recipe_id],
                         recipe_id=recipe_id,
                         caffeine_level=game_state.caffeine_level,
                         unlocked_recipes=game_state.recipes_unlocked)

@app.route('/learn_more/<recipe_id>')
def learn_more(recipe_id):
    if recipe_id not in game_state.recipes_unlocked:
        return redirect(url_for('recipes'))
    
    # Unlock next recipe when transitioning to learn more
    if recipe_id == "espresso" and "americano" not in game_state.recipes_unlocked:
        game_state.recipes_unlocked.append("americano")
    elif recipe_id == "americano" and "macchiato" not in game_state.recipes_unlocked:
        game_state.recipes_unlocked.append("macchiato")
    elif recipe_id == "macchiato" and "latte" not in game_state.recipes_unlocked:
        game_state.recipes_unlocked.append("latte")
    elif recipe_id == "latte" and "mocha" not in game_state.recipes_unlocked:
        game_state.recipes_unlocked.append("mocha")
    
    return render_template('learn_more.html',
                         name=game_state.name,
                         caffeine_level=game_state.caffeine_level)



# QUIZ
# @app.route('/quiz')
# def quiz():
#     with open('static/data/quiz.json') as f:
#         quiz_data = json.load(f)
#     question = quiz_data['questions'][0]
#     return render_template(
#         'quiz.html',
#         question=question,
#         name=game_state.name,
#         caffeine_level=game_state.caffeine_level,
#         inventory=[
#             "coffee_beans",
#             "espresso",
#             "steamed_milk",
#             "milk_foam",
#             "whipped_cream",
#             "chocolate_syrup",
#             "water"
#         ]
#     )
@app.route('/quiz')
@app.route('/quiz/<int:qid>')
def quiz(qid=1):
    with open('static/data/quiz.json') as f:
        quiz_data = json.load(f)
    
    if qid == 1:
        session['quiz_score'] = 0  # Reset score at beginning

    question = next(q for q in quiz_data['questions'] if q['id'] == qid)
    total_questions = len(quiz_data['questions'])
    return render_template(
        'quiz.html',
        question=question,
        current_qid=qid,
        total_questions=total_questions,
        name=game_state.name,
        caffeine_level=game_state.caffeine_level,
        inventory=[
            "coffee_beans", "espresso", "steamed_milk", "milk_foam",
            "whipped_cream", "chocolate_syrup", "water"
        ]
    )
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.json
    qid = data.get('question_id')
    submitted_ingredients = sorted([ing for ing in data.get('ingredients', []) if ing])

    with open('static/data/quiz.json') as f:
        quiz_data = json.load(f)

    question = next(q for q in quiz_data['questions'] if q['id'] == qid)
    correct_option = next(opt for opt in question['options'] if opt['id'] == question['answer_id'])
    correct_ingredients = sorted(correct_option['ingredients'])

    is_correct = submitted_ingredients == correct_ingredients

    # Update score
    if is_correct:
        session['quiz_score'] = session.get('quiz_score', 0) + 1

    next_qid = qid + 1 if qid < len(quiz_data['questions']) else None

    return jsonify({
        'success': is_correct,
        'result': question['success_image'] if is_correct else question['failure_image'],
        'next_qid': next_qid,
        'score': session.get('quiz_score', 0),
        'finished': next_qid is None
    })

@app.route('/certificate')
def certificate():
    score = session.get('quiz_score', 0)
    today = datetime.now().strftime("%B %d, %Y")
    return render_template('certificate.html', name=game_state.name, score=score, date=today)



if __name__ == '__main__':
    app.run(debug=True) 