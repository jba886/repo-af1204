import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Josiah Barry | Data Analytics Portfolio

    ---

    ## About Me

    Hi, I'm **Josiah Barry**, a student studying data analytics.
    This portfolio showcases my ability to work with real financial data
    using Python, Marimo, and data visualisation tools.

    ---

    ## Project Overview

    This dashboard analyses **Apple Inc. (AAPL)** stock data,
    exploring price trends, trading volume, and key financial metrics
    using interactive visualisations.
    """)
    return


if __name__ == "__main__":
    app.run()
