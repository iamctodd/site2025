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
    books = [
        {"title": "Design Sprint", "description": "A comprehensive guide on leveraging a sprint to inform product decisions and strategies.", "link": "https://www.amazon.com/Design-Sprint-Practical-Guidebook-Building/dp/1491923172/ref=sr_1_3?crid=IBQCGHZ699KR&dib=eyJ2IjoiMSJ9.legNGhUOGubiz5M78njsKs1M741mnnqjBOyA-apE2w57mtaL8spdpvA8zlJV5FB1ZamvDKnaM-D6EmEOiYcwl_Zrkayo_uJySfaYhOmZ5IiuzInmla5WPWXopRZL9OXj6IRJdUgKVOvTHEBEk_mJ2Rz-D7NzzNtScJ2eX3SwuUJ_s5JwkbVKmflXAInutnwKffATMK38_PLkgIdGYt0sxmOjiEomBHbpBRbS-si-ebc.PFo4rAsQHbY3dGSJmAutlrEJmt85P0Rvwv7t65f1CEQ&dib_tag=se&keywords=design+sprint&qid=1761679583&s=books&sprefix=design+sprint%2Cstripbooks%2C90&sr=1-3"},
        {"title": "Product Roadmaps Relaunched", "description": "Explores how a great product roadmap can drive growth and innovation.", "link": "https://www.amazon.com/Product-Roadmaps-Relaunched-Direction-Uncertainty/dp/149197172X/ref=pd_lpo_d_sccl_1/140-5098991-6972659?pd_rd_w=eR0YD&content-id=amzn1.sym.4c8c52db-06f8-4e42-8e56-912796f2ea6c&pf_rd_p=4c8c52db-06f8-4e42-8e56-912796f2ea6c&pf_rd_r=AJXCBNHXDM0P0KB76JAP&pd_rd_wg=wms0J&pd_rd_r=9784a906-9331-4482-8114-7d0fbf5bc5a8&pd_rd_i=149197172X&psc=1"},
        {"title": "Product Research Rules", "description": "Insights into the world of researching products effectively.", "link": "https://www.amazon.com/Product-Research-Rules-Foundational-Accelerated/dp/1492049476"}
        ]
    return render_template('writing.html', books=books)

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
    app.run(debug=True, host='0.0.0.0', port=10000)