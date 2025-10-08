from flask import Flask, render_template_string, request, url_for

app = Flask(__name__)

# ---------- BEAUTIFUL BASE PAGE ----------
def render_page(title, inner_html):
    base_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #89f7fe, #66a6ff);
                margin: 0;
                color: #222;
            }}
            nav {{
                background-color: rgba(0,0,0,0.8);
                padding: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.3);
                position: sticky;
                top: 0;
                z-index: 10;
            }}
            nav ul {{
                list-style-type: none;
                display: flex;
                justify-content: center;
                gap: 30px;
                margin: 0;
                padding: 0;
            }}
            nav a {{
                color: white;
                text-decoration: none;
                font-weight: 600;
                transition: 0.3s;
            }}
            nav a:hover {{
                color: #66a6ff;
            }}
            .content {{
                padding: 40px 20px;
                display: flex;
                justify-content: center;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 16px;
                max-width: 600px;
                width: 100%;
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                animation: fadeIn 0.6s ease-in;
            }}
            h1, h2 {{
                text-align: center;
                color: #333;
            }}
            input, button, textarea {{
                width: 100%;
                padding: 10px;
                margin-top: 8px;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 15px;
                font-family: 'Poppins', sans-serif;
            }}
            button {{
                background: linear-gradient(135deg, #66a6ff, #89f7fe);
                color: white;
                font-weight: 600;
                border: none;
                cursor: pointer;
                transition: 0.3s;
            }}
            button:hover {{
                transform: scale(1.05);
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
            a {{
                color: #007BFF;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(10px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><a href="{url_for('home')}">Home</a></li>
                <li><a href="{url_for('profile')}">Profile</a></li>
                <li><a href="{url_for('works')}">Works</a></li>
                <li><a href="{url_for('contact')}">Contact</a></li>
            </ul>
        </nav>
        <div class="content">
            <div class="card">
                {inner_html}
            </div>
        </div>
    </body>
    </html>
    """
    return base_html


# ---------- ROUTES ----------

@app.route('/')
def home():
    html = """
    <h1>Welcome to My Flask Portfolio</h1>
    <p>Hi everyone! My name is Stephen and this is my Lab 3 work as portfolio.</p>
    <p>Use the navigation bar above to explore my profile, works, and contact info.</p>
    """
    return render_page("Home", html)


@app.route('/profile')
def profile():
    html = """
    <h2>About Me</h2>
    <p><strong>Name:</strong> Stephen Mariñas</p>
    <p><strong>Course:</strong> BS Computer Engineering</p>
    <p><strong>Section:</strong> BSCPE 2-3</p>
    <p><strong>Subject:</strong> Data Structures and Algorithms</p>
    <p><strong>Motto:</strong> “Everything can be made with computer engineering, think about it yow..”</p>
    """
    return render_page("Profile", html)


@app.route('/contact')
def contact():
    html = """
    <h2>Contact Me</h2>
    <p>Email: stephenmarinas.property@gmail.com</p>
    <p>GitHub: <a href="https://github.com/stephenmarinas31" target="_blank">stephenmarinas31</a></p>
    """
    return render_page("Contact", html)


@app.route('/works')
def works():
    html = f"""
    <h2>Programming Works</h2>
    <p>Explore my simple Flask-based programming activities below:</p>
    <ul>
        <li><a href="{url_for('area_calculator')}">Area Calculator</a></li>
        <li><a href="{url_for('text_uppercase')}">toUpperCase Converter</a></li>
    </ul>
    """
    return render_page("Works", html)


@app.route('/area_calculator', methods=['GET', 'POST'])
def area_calculator():
    result = ""
    if request.method == 'POST':
        shape = request.form['shape']
        try:
            if shape == 'circle':
                r = float(request.form['radius'])
                result = f"Area of Circle: {3.1416 * r * r:.2f}"
            elif shape == 'triangle':
                b = float(request.form['base'])
                h = float(request.form['height'])
                result = f"Area of Triangle: {0.5 * b * h:.2f}"
        except ValueError:
            result = "Please enter valid numbers."

    html = f"""
    <h2>Area Calculator</h2>
    <form method="POST">
        <h3>Circle</h3>
        <label>Radius:</label>
        <input type="number" name="radius" step="any">
        <button type="submit" name="shape" value="circle">Compute Circle Area</button>

        <h3>Triangle</h3>
        <label>Base:</label>
        <input type="number" name="base" step="any">
        <label>Height:</label>
        <input type="number" name="height" step="any">
        <button type="submit" name="shape" value="triangle">Compute Triangle Area</button>
    </form>
    """

    if result:
        html += f"<h3>{result}</h3>"

    return render_page("Area Calculator", html)


@app.route('/text_uppercase', methods=['GET', 'POST'])
def text_uppercase():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        result = text.upper()

    html = f"""
    <h2>toUpperCase Converter</h2>
    <form method="POST">
        <label>Enter text:</label>
        <textarea name="text" rows="4" cols="40"></textarea>
        <button type="submit">Convert to UPPERCASE</button>
    </form>
    """

    if result:
        html += f"<h3>Result: {result}</h3>"

    return render_page("toUpperCase Converter", html)


# ---------- MAIN ----------
if __name__ == '__main__':
    app.run(debug=True)
