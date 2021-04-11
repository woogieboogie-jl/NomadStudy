from flask import Flask, render_template, request, redirect, send_file
from scraper_wework import collect_jobs_wework
from scraper_remote import collect_jobs_remote
from scraper_stack import collect_jobs_stack
from exporter import export_csv

db = {}
app = Flask("BLOCKCHAIN OPPORTUNNITIES")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/searched")
def searched():
  word = request.args.get("requested").lower().strip()
  if word == "":
    word = "blockchain"
  existing_request = db.get(word)
  if existing_request:
    jobs = existing_request
  else:
    remote = collect_jobs_remote(word)
    stack = collect_jobs_stack(word)
    wework = collect_jobs_wework(word)
    jobs = remote + stack + wework
    db[word] = jobs
  return render_template("searched.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)

@app.route("/export")
def export():
  try:
    requested = request.args.get("word")
    if requested == None:
      requested = "blockchain"
    print(requested)
    jobs = db.get(requested)
    export_csv(jobs, requested)
  except Exception:
    raise Exception()
    return redirect("/")
  return send_file(f"jobs_{requested}.csv", attachment_filename=f"jobs_{requested}.csv",as_attachment=True)

app.run(host="0.0.0.0")