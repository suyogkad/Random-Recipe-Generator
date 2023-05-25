from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()

    if request.method == 'POST':
        c.execute('SELECT * FROM recipes ORDER BY RANDOM() LIMIT 1')
        recipe = c.fetchone()
        c.close()

        recipe_dict = {
            'title': recipe[1],
            'ingredients': recipe[2],
            'instructions': recipe[3],
            'image': '/static/images/' + recipe[4] + '.jpg'
        }

        return render_template('index.html', recipe=recipe_dict)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
