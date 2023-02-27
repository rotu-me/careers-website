from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Abuja',
    'salary': 'Rs. 12,00,000'
  },
   {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'America',
    'salary': 'Rs. 14,00,000'
  },
   {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'San Francisco, USA',
    'salary': 'Rs. 18,00,000'
  },
   {
    'id': 1,
    'title': 'Backend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
]

@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS,
                        company_name="Joviers")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)