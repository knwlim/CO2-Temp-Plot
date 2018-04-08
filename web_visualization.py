from flask import Flask
from flask import render_template
from flask import request
from temperature_CO2_plotter import plot_co2, plot_temperature, plot_co2_by_country
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('main.html')


@app.route('/co2', methods=['POST'])
def co2_plot():
    ymin = request.form["ymin"]
    if ymin == "default" : ymin = -200
    ymax = request.form["ymax"]
    if ymax == "default" : ymax = 10000
    start_year = int(request.form["starty"])
    end_year = int(request.form["endy"])
    CO2_data = np.genfromtxt("co2.csv", delimiter=',', dtype="str")
    plot_co2(CO2_data, ymin, ymax, start_year, end_year)

    return render_template('plot_co2.html', start_year=start_year, end_year=end_year,
                           ymin=ymin, ymax=ymax)


@app.route('/temp', methods=['POST'])
def temp_plot():
    ymin = request.form["ymin"]
    ymax = request.form["ymax"]
    start_year = int(request.form["starty"])
    end_year = int(request.form["endy"])
    month = int(request.form["month"])
    temp_data = np.genfromtxt("temperature.csv", delimiter=',', dtype="str")
    plot_temperature(temp_data, month, ymin, ymax, start_year, end_year)

    return render_template('plot_temp.html', start_year=start_year, end_year=end_year,
                           ymin=ymin, ymax=ymax, month=month)

@app.route('/country', methods=['POST'])
def country_plot():
    year = int(request.form["year"])
    low_thres = int(request.form["low_thres"])
    upper_thres = int(request.form["upper_thres"])
    country_data = pd.read_csv("CO2_by_country.csv", quotechar='"')
    plot_co2_by_country(country_data,  low_thres,upper_thres, year)

    return render_template('plot_country.html', year=year, low_thres=low_thres,
                           upper_thres=upper_thres)

if __name__ == "__main__":
    app.run()