from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import NotFound
from http import HTTPStatus

from models import db, Article
from .forms import ArticleForm

article_app = Blueprint(
    "article_app",
    __name__,
    url_prefix="/article"
)

@article_app.get("/", endpoint="article_list")
def get_article_list():
    articles = Article.query.order_by(Article.id_art).all()
    return render_template("article/art_list.html", articles=articles)
    
    
@article_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_article():
    form = ArticleForm()
    
    if request.method == "GET":
        return render_template("article/create.html", form=form)
    
    
    if not form.validate_on_submit():
        return (render_template("article/create.html", form=form), HTTPStatus.BAD_REQUEST)
    
    article = Article(code=form.data["code"], name=form.data["name"], status=form.data["status"])
    db.session.add(article)
    db.session.commit()
    flash(f"Article {article.code} - {article.name} was created")
    url = url_for("article_app.article_list")
    return redirect(url)


def get_article_or_rise(id_art: int):
    article = Article.query.get(id_art)
    if article:
        return article
    
    raise NotFound(f"Товар с id={id_art} не найден!")

@article_app.get("/<int:id_art>", endpoint="details")
def get_article_detail(id_art):
    article = get_article_or_rise(id_art)
    return render_template("article/art_details.html", article=article)


@article_app.route("/<int:id_art>", methods=["GET", "POST"], endpoint="delete")
def delete_article(id_art: int):
    article = get_article_or_rise(id_art)
    if request.method == "GET":
        return render_template("article/art_details.html", article=article)
    
    article_name = article.name
    db.session.delete(article)
    db.session.commit()
    flash(f"Deleted article: {article_name}")
    url = url_for("article_app.article_list")
    return redirect(url)