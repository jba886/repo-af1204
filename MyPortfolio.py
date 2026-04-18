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
    return (go,)


@app.cell
def _(mo):
    # Interactive dropdown to select metric
    metric = mo.ui.dropdown(
        options=["Close", "Open", "High", "Low", "Volume"],
        value="Close",
        label="Select a metric to display:"
    )
    metric
    return (metric,)


@app.cell
def _(apple, go, metric):
    # Chart that updates based on dropdown selection
    selected = metric.value

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=apple.index,
        y=apple[selected]["AAPL"],
        mode="lines",
        name=selected,
        line=dict(color="royalblue", width=2)
    ))

    fig2.update_layout(
        title=f"Apple Inc. (AAPL) - {selected} (Past Year)",
        xaxis_title="Date",
        yaxis_title="Value",
        template="plotly_white"
    )

    fig2
    return


@app.cell
def _(apple, mo):
    # Summary statistics
    avg_price = apple["Close"]["AAPL"].mean()
    max_price = apple["Close"]["AAPL"].max()
    min_price = apple["Close"]["AAPL"].min()
    latest_price = apple["Close"]["AAPL"].iloc[-1]

    mo.md(f"""
    ## 📊 Apple Inc. (AAPL) — Key Statistics (Past Year)

    | Metric | Value |
    |--------|-------|
    | 📈 Latest Closing Price | ${latest_price:.2f} |
    | 📊 Average Closing Price | ${avg_price:.2f} |
    | 🔺 Highest Closing Price | ${max_price:.2f} |
    | 🔻 Lowest Closing Price | ${min_price:.2f} |
    """)
    return


if __name__ == "__main__":
    app.run()
