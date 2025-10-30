from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/admin')
def admin_dashboard():
    return render_template('admin.html')

@app.route('/admin/users')
def admin_users():
    return render_template('admin_users.html')

@app.route('/admin/courses')
def admin_courses():
    return render_template('admin_courses.html')

@app.route('/admin/analytics')
def admin_analytics():
    return render_template('admin_analytics.html')

@app.route('/admin/settings')
def admin_settings():
    return render_template('admin_settings.html')

if __name__ == '__main__':
    app.run(debug=True)

