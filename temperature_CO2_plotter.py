import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def plot_co2(co2_data, ymin = -200, ymax= 10000, start_year=1751, end_year=2012):
    """
    plot co2 from 1751 to 2012 with matplotlib

    :param co2_data:
    :param ymin:
    :param ymax:
    :param start_year:
    :param end_year:
    :return: None
    """
    x_data = [x[0] for x in co2_data]
    y_data = [x[1] for x in co2_data]

    start_from = int(x_data[1])  # 1751
    end_at = int(x_data[-1])     # 2012
    # index to access year data from the list
    year_index = {key : key-start_from + 1 for key in range(start_from, end_at + 1)}
    start_idx = year_index[start_year]
    end_idx = year_index[end_year] + 1

    # plot
    plt.clf()
    plt.plot(x_data[start_idx:end_idx], y_data[start_idx:end_idx])
    plt.xlabel(x_data[0])
    plt.ylabel("CO2 (Million metric tons)")
    plt.ylim((int(ymin), int(ymax)))
    plt.savefig("static/co2result")
    return None


def plot_temperature(temp_data, month, ymin=None, ymax=None, start_year=1816, end_year=2012):
    """
    plot temperature from year 1816 to 2012 with matplotlib

    :param temp_data:
    :param month:
    :param ymin:
    :param ymax:
    :param start_year:
    :param end_year:
    :return: None
    """
    list_of_year = [int(x[0]) for x in temp_data[1:]]
    list_of_temp = [float(x[month]) for x in temp_data[1:]]
    if ymin is None or ymin == "default": ymin = min(list_of_temp) - 1
    else : ymin = ymin
    if ymax is None or ymax == "default": ymax = max(list_of_temp) + 1
    else : ymax = ymax

    start_from = int(list_of_year[0])   # 1816
    end_at = int(list_of_year[-1])      # 2012
    # index to access year data from the list
    year_index = {key: key - start_from for key in range(start_from, end_at + 1)}
    start_idx = year_index[start_year]
    end_idx = year_index[end_year]

    # plot
    plt.clf()
    x_label = temp_data[0][0]
    y_label = "Temperature (°C)"
    month_label = temp_data[0][month]
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(list_of_year[start_idx:end_idx], list_of_temp[start_idx:end_idx], label=month_label)
    plt.legend(loc='best')
    plt.ylim((int(ymin), int(ymax)))
    plt.savefig("static/tempresult")
    return None


def plot_co2_by_country(co2_country_data, lower_threshold = 0.0, upper_threshold = 10000, year = 2000):
    """
    plot CO2 by country on specific year

    :param co2_country_data:
    :param lower_threshold:
    :param upper_threshold:
    :param year:
    :return: None
    """
    subset = co2_country_data[["Country Code", str(year)]]
    res_low = subset.loc[subset[str(year)] > lower_threshold]
    res = res_low.loc[subset[str(year)] < upper_threshold]

    # plot
    plt.clf()
    plt.xlabel("Country Code")
    plt.ylabel("CO2")
    year_label = str(year)
    xn = range(len(res["Country Code"]))
    plt.plot(xn, res[str(year)], label=year_label)
    plt.legend(loc='best')
    plt.xticks(xn, res["Country Code"], rotation='vertical')
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.savefig("static/country_result")
    return None


if __name__ == "__main__":
    CO2_data = np.genfromtxt("co2.csv", delimiter=',', dtype="str")
    temp_data = np.genfromtxt("temperature.csv", delimiter=',', dtype="str")
    country_data = pd.read_csv("CO2_by_country.csv", quotechar='"')
    # for test
    #plot_co2(CO2_data)
    #plot_temperature(temp_data, 2)
    #plot_co2_by_country(country_data, 15, 20)