from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'replace-with-a-secret-key'

projects = [
        {"title": "Appcues — VP of Product", "description": "Scaled product and design teams, launched analytics features driving 2x engagement.", "link": "#"},
        {"title": "Vempathy — CEO & Co-founder", "description": "Built AI-driven user research platform acquired by a major UX firm.", "link": "#"},
        {"title": "Tyche Tools — Founder", "description": "Creating tools for data-driven operations in tech and product management.", "link": "#"},
        {"title": "Product Roadmaps Relaunched — Co-author", "description": "Authored a book on modern product roadmap techniques and frameworks.", "link": "#"}
        ]
    
# Configure Flask-Mail
app.config.update(
    MAIL_SERVER='smtp.example.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='your_email@example.com',
    MAIL_PASSWORD='your_email_password',
    MAIL_DEFAULT_SENDER=('C Todd', 'email@example.com')
    )
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/work')
def work():
    return render_template('work.html', projects=projects)

@app.route('/writing')
def writing():
    return render_template('writing.html')

@app.route('/teaching')
def teaching():
    return render_template('teaching.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # TODO: send email or store message
        flash('Thank you for your message!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)