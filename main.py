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
    return render_template("index.html")


@app.route('/landing')
def landing():
    return render_template("landing.html")


@app.route('/activity')
def activity():
    return render_template("activity.html")


@app.route('/api_keys')
def api_keys():
    return render_template("api_keys.html")


@app.route('/billing')
def billing():
    return render_template("billing.html")


@app.route('/logs')
def logs():
    return render_template("logs.html")


@app.route('/overview')
def overview():
    return render_template("overview.html")


@app.route('/referrals')
def referrals():
    return render_template("referrals.html")


@app.route('/security')
def security():
    return render_template("security.html")


@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.route('/statements')
def statements():
    return render_template("statements.html")


@app.route('/drawer')
def drawer():
    return render_template("drawer.html")


@app.route('/group')
def group():
    return render_template("group.html")


@app.route('/private')
def private():
    return render_template("private.html")


@app.route('/add_contact')
def add_contact():
    return render_template("add_contact.html")


@app.route('/edit_contact')
def edit_contact():
    return render_template("edit_contact.html")


@app.route('/edit_product')
def edit_product():
    return render_template("edit-product.html")


@app.route('/getting_started')
def getting_started():
    return render_template("getting_started.html")


@app.route('/view_contact')
def view_contact():
    return render_template("view_contact.html")


@app.route('/view')
def view():
    return render_template("view.html")


@app.route('/add_category')
def add_category():
    return render_template("add_category.html")


@app.route('/categories')
def categories():
    return render_template("index.html")


@app.route('/edit_category')
def edit_category():
    return render_template("edit_category.html")


@app.route('/products')
def products():
    return render_template("products.html")


@app.route('/customer_orders')
def customer_orders():
    return render_template("customer_orders.html")


@app.route('/returns')
def returns():
    return render_template("returns.html")


@app.route('/sales')
def sales():
    return render_template("sales.html")


@app.route('/shipping')
def shipping():
    return render_template("shipping.html")


@app.route('/add_order')
def add_order():
    return render_template("add_order.html")


@app.route('/details')
def details():
    return render_template("details.html")


@app.route('/edit_order')
def edit_order():
    return render_template("edit_order.html")


@app.route('/blank')
def blank():
    return render_template("blank.html")


@app.route('/folders')
def folders():
    return render_template("folders.html")


@app.route('/compose')
def compose():
    return render_template("compose.html")


@app.route('/listing')
def listing():
    return render_template("listing.html")


@app.route('/lists')
def lists():
    return render_template("lists.html")


@app.route('/reply')
def reply():
    return render_template("reply.html")


@app.route('/invoice_1')
def invoice_1():
    return render_template("invoice-1.html")


@app.route('/invoice_2')
def invoice_2():
    return render_template("invoice-2.html")


@app.route('/invoice_3')
def invoice_3():
    return render_template("invoice-3.html")


@app.route('/create')
def create():
    return render_template("create.html")


@app.route('/budget')
def budget():
    return render_template("budget.html")


@app.route('/files')
def files():
    return render_template("files.html")


@app.route('/list')
def list():
    return render_template("list.html")


@app.route('/project')
def project():
    return render_template("project.html")


@app.route('/targets')
def targets():
    return render_template("targets.html")


@app.route('/users')
def users():
    return render_template("users.html")


@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/add_product')
def add_product():
    return render_template("add-product.html")


@app.route('/post')
def post():
    return render_template("post.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/faq')
def faq():
    return render_template("faq.html")


@app.route('/licenses')
def licenses():
    return render_template("licenses.html")


@app.route('/permissions')
def permissions():
    return render_template("permissions.html")


@app.route('/calendar')
def calendar():
    return render_template("calendar.html")


@app.route('/card_declined')
def card_declined():
    return render_template("card-declined.html")


@app.route('/invitation')
def invitation():
    return render_template("invitation.html")


@app.route('/password_change')
def password_change():
    return render_template("password-change.html")


@app.route('/password_reset')
def password_reset():
    return render_template("password-reset.html")


@app.route('/promo_1')
def promo_1():
    return render_template("promo-1.html")


@app.route('/promo_2')
def promo_2():
    return render_template("promo-2.html")


@app.route('/promo_3')
def promo_3():
    return render_template("promo-3.html")


@app.route('/subscription_confirmed')
def subscription_confirmed():
    return render_template("subscription-confirmed.html")


@app.route('/verify_email')
def verify_email():
    return render_template("verify-email.html")


@app.route('/welcome_message')
def welcome_message():
    return render_template("welcome-message.html")


@app.route('/multi_steps_sign_up')
def multi_steps_sign_up():
    return render_template("multi-steps-sign-up.html")


@app.route('/two_factor_auth')
def two_factor_auth():
    return render_template("two-factor-auth.html")


@app.route('/account_deactivated')
def account_deactivated():
    return render_template("account-deactivated.html")


@app.route('/coming_soon')
def coming_soon():
    return render_template("coming-soon.html")


@app.route('/deactivation')
def deactivation():
    return render_template("deactivation.html")


@app.route('/error_404')
def error_404():
    return render_template("error-404.html")


@app.route('/error_500')
def error_500():
    return render_template("error-500.html")


@app.route('/password_confirmation')
def password_confirmation():
    return render_template("password-confirmation.html")


@app.route('/new_password')
def new_password():
    return render_template("new-password.html")


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/reset_password')
def reset_password():
    return render_template("reset-password.html")


@app.route('/sign_in')
def sign_in():
    return render_template("sign-in.html")


@app.route('/sign_up')
def sign_up():
    return render_template("sign-up.html")


@app.route('/two_steps')
def two_steps():
    return render_template("two-steps.html")


@app.route('/bidding')
def bidding():
    return render_template("bidding.html")


@app.route('/call_center')
def call_center():
    return render_template("call-center.html")


@app.route('/crypto')
def crypto():
    return render_template("crypto.html")


@app.route('/delivery')
def delivery():
    return render_template("delivery.html")


@app.route('/ecommerce')
def ecommerce():
    return render_template("ecommerce.html")


@app.route('/finance_performance')
def finance_performance():
    return render_template("finance-performance.html")


@app.route('/logistics')
def logistics():
    return render_template("logistics.html")


@app.route('/marketing')
def marketing():
    return render_template("marketing.html")


@app.route('/online_courses')
def online_courses():
    return render_template("online-courses.html")


@app.route('/podcast')
def podcast():
    return render_template("podcast.html")


@app.route('/pos')
def pos():
    return render_template("pos.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/school')
def school():
    return render_template("school.html")


@app.route('/social')
def social():
    return render_template("social.html")


@app.route('/store_analytics')
def store_analytics():
    return render_template("store-analytics.html")


@app.route('/website_analytics')
def website_analytics():
    return render_template("website-analytics.html")


@app.route('/dark_header')
def dark_header():
    return render_template("dark-header.html")


@app.route('/dark_sidebar')
def dark_sidebar():
    return render_template("dark-sidebar.html")


@app.route('/light_header')
def light_header():
    return render_template("light-header.html")


@app.route('/light_sidebar')
def light_sidebar():
    return render_template("light-sidebar.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/apply')
def apply():
    return render_template("apply.html")


@app.route('/classic')
def classic():
    return render_template("classic.html")


@app.route('/extended')
def extended():
    return render_template("extended.html")


@app.route('/column')
def column():
    return render_template("column.html")


@app.route('/table')
def table():
    return render_template("table.html")


@app.route('/feeds')
def feeds():
    return render_template("feeds.html")


@app.route('/followers')
def followers():
    return render_template("followers.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/sitemap')
def sitemap():
    return render_template("sitemap.html")


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/campaigns')
def campaigns():
    return render_template("campaigns.html")


@app.route('/documents')
def documents():
    return render_template("documents.html")


@app.route('/accounting')
def accounting():
    return render_template("accounting.html")


@app.route('/reports')
def reports():
    return render_template("reports.html")


@app.route('/saas')
def saas():
    return render_template("saas.html")


@app.route('/create_api_key')
def create_api_key():
    return render_template("create-api-key.html")


@app.route('/new_address')
def new_address():
    return render_template("new-address.html")


@app.route('/new_card')
def new_card():
    return render_template("new-card.html")


@app.route('/new_target')
def new_target():
    return render_template("new-target.html")


@app.route('/invite_friends')
def invite_friends():
    return render_template("invite-friends.html")


@app.route('/select_users')
def select_users():
    return render_template("select-users.html")


@app.route('/share_earn')
def share_earn():
    return render_template("share-earn.html")


@app.route('/upgrade_plan')
def upgrade_plan():
    return render_template("upgrade-plan.html")


@app.route('/view_users')
def view_users():
    return render_template("view-users.html")


@app.route('/create_account')
def create_account():
    return render_template("create-account.html")


@app.route('/create_app')
def create_app():
    return render_template("create-app.html")


@app.route('/create_campaign')
def create_campaign():
    return render_template("create-campaign.html")


@app.route('/create_project')
def create_project():
    return render_template("create-project.html")


@app.route('/offer_a_deal')
def offer_a_deal():
    return render_template("offer-a-deal.html")


@app.route('/top_up_wallet')
def top_up_wallet():
    return render_template("top-up-wallet.html")


@app.route('/two_factor_authentication')
def two_factor_authentication():
    return render_template("two-factor-authentication.html")


@app.route('/horizontal')
def horizontal():
    return render_template("horizontal.html")


@app.route('/select_location')
def select_location():
    return render_template("select-location.html")


@app.route('/vertical')
def vertical():
    return render_template("vertical.html")


@app.route('/charts')
def charts():
    return render_template("charts.html")


@app.route('/mixed')
def mixed():
    return render_template("mixed.html")


@app.route('/statistics')
def statistics():
    return render_template("statistics.html")


@app.route('/tables')
def tables():
    return render_template("tables.html")


@app.route('/main_page', methods=['POST', 'GET'])
def main_page():
    mycur.execute("select * from project_details")
    project_details_main = mycur.fetchall()
    conn.commit()
    return render_template("light-header_admin.html", project_details = project_details_main)

@app.route("/project_details_full/<project_name>")
def project_details_full(project_name):
    mycur.execute(f"select * from project_details where project_name = '{project_name}'")
    project_details_main = mycur.fetchall()
    conn.commit()
    return render_template("dark-header.html", project_details = project_details_main)


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
                      f" number_of_tasks) VALUES('{project_id}', '{name_project}', '{category}', "
                      f"'{framework}', '{days_details}', '{project_progress}', '{project_brief_short}', "
                      f"'{project_brief_big}', '{project_amount}', '{project_task}')")
        conn.commit()

        return redirect("main_page")  # Modify this according to your error handling

if __name__ == '__main__':
    app.run(debug=True)
