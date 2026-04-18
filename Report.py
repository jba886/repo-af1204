import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # AF1204 Individual Project Report
    ### Josiah Barry

    ---

    ## 1. Introduction

    This report documents the development of my personal portfolio webpage,
    built using Python, Marimo, and real financial data from Apple Inc. (AAPL).
    The portfolio demonstrates the data literacy skills I have acquired
    throughout the AF1204 module, including data collection, preparation,
    visualisation, and interactive dashboard design.

    ---

    ## 2. Project Overview

    The portfolio webpage features an interactive dashboard that analyses
    Apple Inc. (AAPL) stock data over the past year. The dashboard allows
    users to explore key financial metrics including closing price, opening
    price, daily highs and lows, and trading volume through interactive
    visualisations and a dynamic dropdown selector.

    ---

    ## 3. Data Collection and Preparation

    Real financial data was collected using the **yfinance** Python library,
    which provides access to Yahoo Finance stock market data. The dataset
    contains daily stock information for Apple Inc. (AAPL) over a 12-month
    period, including open, close, high, low prices and trading volume.
    Data was loaded into a **pandas** DataFrame, allowing for efficient
    manipulation and analysis.

    ---

    ## 4. Interactive Dashboard Features

    The dashboard includes the following interactive features:

    - **Stock Price Chart**: An interactive line chart built using Plotly
    showing Apple's closing price over the past year, allowing users to
    hover over data points to see exact values.

    - **Metric Selector**: A dropdown menu built using Marimo's UI components
    allowing users to switch between different metrics (Close, Open, High,
    Low, Volume) and see the chart update dynamically.

    - **Key Statistics Table**: A summary table displaying the latest closing
    price, average price, highest price, and lowest price over the past year.

    ---

    ## 5. Technical Skills Demonstrated

    This project demonstrates the following skills acquired during the module:

    - **Python programming** — writing clean, structured code in Marimo notebooks
    - **Data collection** — using yfinance API to retrieve real financial data
    - **Data visualisation** — creating interactive charts using Plotly
    - **Marimo** — building reactive notebooks that export to interactive webpages
    - **GitHub** — version control with regular commits and GitHub Pages deployment

    ---

    ## 6. Conclusion

    This portfolio webpage successfully demonstrates my ability to collect,
    prepare, analyse and visualise real financial data using Python and
    modern data tools. The interactive dashboard provides an engaging way
    to explore Apple Inc. stock performance, and the project as a whole
    reflects the core skills developed throughout the AF1204 module.
    """)
    return


if __name__ == "__main__":
    app.run()
