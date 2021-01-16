from flask import Flask, redirect, url_for, render_template, request
from inv import prod, Ingredient, Product
import json


app = Flask(__name__)

cart = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return render_template("results.html")
    else:
        return render_template("tally.html")

@app.route("/results", methods=["POST","GET"])
def results():
    result_name = request.form["data"]
    result_name2 = json.loads(result_name)
    for i in result_name2:
        prodname = list(i)[0]
        prodval= (i[prodname])
        def shopping():
            together = 0
            purchase = prodname
            many_purchase = (int(prodval))
            totals = prod[purchase].totals(prod[purchase].Ingredient, prod[purchase].ratio, prod[purchase].cost)
            together += prod[purchase].total * many_purchase
            print(f"You sold {many_purchase} units of the {prod[purchase].name} for {round(together, 2)}.")
            cart.append(round(together,2))
        shopping()

    return render_template("results.html", crt=round(sum(cart),2))



if __name__ == "__main__":
    app.run(debug=True)

