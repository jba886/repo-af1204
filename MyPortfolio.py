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


@app.cell
def _():
    import yfinance as yf
    import pandas as pd

    # Download Apple stock data for the past year
    apple = yf.download("AAPL", period="1y")

    # Show the first few rows
    apple.head()
    return (apple,)


@app.cell
def _(apple):
    import plotly.graph_objects as go

    # Create interactive stock price chart
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=apple.index,
        y=apple["Close"]["AAPL"],
        mode="lines",
        name="Closing Price",
        line=dict(color="royalblue", width=2)
    ))

    fig.update_layout(
        title="Apple Inc. (AAPL) - Stock Closing Price (Past Year)",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_white"
    )

    fig
    return


if __name__ == "__main__":
    app.run()
