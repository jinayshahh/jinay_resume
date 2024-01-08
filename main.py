from flask import Flask, request, redirect, session, render_template, jsonify, url_for
import mysql.connector
from datetime import datetime, time
import time
import random
import re
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management
jinay_password = "Bulletproof28"

conn = mysql.connector.connect(
    user="root",
    password="abcd1234",
    host="localhost",
    database="jinay_shah_resume",
    port="3306"
)
mycur = conn.cursor(buffered=True)

@app.route('/')
def index():
    return render_template("welcome.html")


@app.route('/sign_in')
def sign_in():
    return render_template("sign-in.html")


@app.route('/jinay_resume', methods=['POST', 'GET'])
def jinay_resume():
    mycur.execute("select * from project_details where soft_delete != 'yes'")
    project_details_main = mycur.fetchall()
    conn.commit()
    print(project_details_main)
    return render_template("light-header.html", project_details=project_details_main)


@app.route('/soft_delete_project_list')
def soft_delete_project_list():
    mycur.execute("SELECT * from project_details where soft_delete = 'yes'")
    deleted_projects = mycur.fetchall()
    conn.commit()
    return render_template("soft_delete_project_list.html", deleted_sports=deleted_projects)


@app.route('/revive_project/<revive_project_name>', methods=['POST', 'GET'])
def revive_match(revive_project_name):
    mycur.execute(f"UPDATE project_details SET soft_delete = 'no' WHERE project_name = '{revive_project_name}'")
    conn.commit()
    return redirect(url_for("main_page"))


@app.route('/main_page', methods=['POST', 'GET'])
def main_page():
    mycur.execute("select * from project_details where soft_delete != 'yes'")
    project_details_main = mycur.fetchall()
    conn.commit()
    print(project_details_main)
    return render_template("light-header_admin.html", project_details=project_details_main)

@app.route("/project_details_full/<project_name>")
def project_details_full(project_name):
    session['project_name'] = project_name
    mycur.execute(f"select * from project_details where project_name = '{project_name}'")
    project_details_main = mycur.fetchall()
    conn.commit()
    return render_template("dark-header.html", project_details=project_details_main)


@app.route("/project_details_full_general/<project_name>")
def project_details_full_general(project_name):
    session['project_name'] = project_name
    mycur.execute(f"select * from project_details where project_name = '{project_name}'")
    project_details_main = mycur.fetchall()
    conn.commit()
    return render_template("dark-header-general.html", project_details=project_details_main)


@app.route('/delete_project', methods=['POST'])
def soft_delete_project():
    project_name = session.get("project_name")
    mycur.execute(f"UPDATE project_details SET soft_delete = 'yes' WHERE project_name = '{project_name}'")
    conn.commit()
    return redirect(url_for("main_page"))


@app.route('/update_project', methods=['POST', 'GET'])
def update_open_sport():
    project_name = session.get("project_name")
    mycur.execute(f"select * from project_details where project_name = '{project_name}'")
    project_details_main = mycur.fetchall()
    conn.commit()
    return render_template('project_update_details.html', project_details=project_details_main, project_name=project_name)


@app.route('/project_update_form/<project_id>', methods=['POST'])
def project_update_form(project_id):
    if request.method == 'POST':
        project_name = request.form.get('project_name')
        project_brief_short = request.form.get('project_brief_short')
        project_brief_big = request.form.get('project_brief_big')
        days_details = request.form.get('days_details')
        amount_project = request.form.get('amount')
        tasks_project = request.form.get('tasks')
        progress_project = request.form.get('progress')
        category_project = request.form.get('category')
        framework_project = request.form.get('framework')
        mycur.execute(f"UPDATE project_details SET project_name = '{project_name}', category_project = "
                      f"'{category_project}', project_framework = '{framework_project}', day_details = "
                      f"'{days_details}', project_progress = '{progress_project}', project_brief_short = "
                      f"'{project_brief_short}', project_brief_big = '{project_brief_big}', project_cash = "
                      f"'{amount_project}', number_of_tasks = '{tasks_project}' where idproject_details = '{project_id}'")
        conn.commit()
        return redirect(url_for("main_page"))

    return redirect(url_for("main_page"))


@app.route('/log_in_password_admin', methods=['POST'])
def log_in_password_admin():
    if request.method == 'POST':
        if 'password_admin' in request.form:
            password_admin = request.form['password_admin']
            print(password_admin)
            if password_admin == jinay_password:
                print('Login successful')
                return redirect("main_page")
            else:
                return render_template("incorrect_password.html")
    print('Error: Invalid request')
    return 'Error: Invalid request'  # Modify this according to your error handling



@app.route('/project_details', methods=['POST'])
def project_details():
    if request.method == 'POST':
        print("hii")
        mycur.execute("SELECT idproject_details FROM project_details ORDER BY idproject_details DESC LIMIT 1")
        project_ids = mycur.fetchall()
        conn.commit()
        if project_ids:
            project_id = int(project_ids[0][0]) + 1
        else:
            project_id = 1
        name_project = request.form['project_name']
        category = request.form['category']
        framework = request.form['framework']
        days_details = request.form['days_details']
        project_brief_short = request.form['project_brief_short']
        project_brief_big = request.form['project_brief_big']
        project_progress = request.form['progress']
        project_amount = request.form['amount']
        project_task = request.form['tasks']
        mycur.execute("INSERT INTO project_details(idproject_details, project_name, category_project, project_framework"
                      ", day_details, project_progress, project_brief_short, project_brief_big, project_cash,"
                      f" number_of_tasks, soft_delete) VALUES('{project_id}', '{name_project}', '{category}', "
                      f"'{framework}', '{days_details}', '{project_progress}', '{project_brief_short}', "
                      f"'{project_brief_big}', '{project_amount}', '{project_task}', 'no')")
        conn.commit()

        return redirect("main_page")  # Modify this according to your error handling

if __name__ == '__main__':
    app.run(debug=True)
