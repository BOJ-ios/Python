from flask import Flask, render_template, request, redirect, send_file
from extractor.kr_indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.file import save_to_file

app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
    return render_template("home.html", name="MinGyu")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    print(request.args)
    if keyword == None or keyword == '':
        return render_template("/")
    else:
        if keyword in db:
            jobs = db[keyword]
        else:
            indeed = extract_indeed_jobs(keyword)
            wwr = extract_wwr_jobs(keyword)
            jobs = indeed + wwr
            db[keyword] = jobs
        return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    print(request.args)
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword=keyword")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", mimetype='text/csv', as_attachment=True)


app.run()
