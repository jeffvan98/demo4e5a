from os import environ
from flask import Blueprint, render_template

frontend_name = environ.get("FRONTEND_NAME", "Demo")

main_bp = Blueprint(
    "main", 
    __name__, 
    template_folder="templates", 
    static_folder="static")

@main_bp.route("/")
def index():    
    return render_template("index.html", frontend_name=frontend_name)

@main_bp.route("/explore")
def explore():
    return render_template("explore.html", frontend_name=frontend_name)

@main_bp.route("/about")
def about():
    return render_template("about.html", frontend_name=frontend_name)
