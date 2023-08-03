from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

server_config = config['server']
database_config = config['database']
settings_config = config['settings']

# Mysql Connection
app.config['MYSQL_HOST'] = database_config['host']
app.config['MYSQL_USER'] = database_config['user']
app.config['MYSQL_PASSWORD'] = database_config['password']
app.config['MYSQL_DB'] = database_config['db']
mysql = MySQL(app)

# settings
app.secret_key = settings_config['secret_key']

@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact added succesfully')
        return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts WHERE id = {0}'.format(id))
    data = cursor.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<string:id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE contacts 
            SET fullname = %s, 
                phone = %s, 
                email = %s 
            WHERE id = %s""", (fullname, phone, email, id))
        mysql.connection.commit()
        flash('Contact updated succesfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact removed succesfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = server_config['port'], debug = True)
