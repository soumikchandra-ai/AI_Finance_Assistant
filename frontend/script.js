async function analyzeStock(){

    const symbol = document.getElementById("symbol").value;

    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "Analyzing with AI...";

    try{

        const response = await fetch(`/analysis/${symbol}`);

        const data = await response.json();

        resultDiv.innerHTML = `

            <h2>${data.stock_data.symbol}</h2>

            <p>
            <strong>Latest Close:</strong>
            ${data.stock_data.latest_close}
            </p>

            <p>
            <strong>Recommendation:</strong>
            ${data.stock_data.signals.recommendation}
            </p>

            <hr>

            <h3>AI Analysis</h3>

            <p>${data.ai_analysis}</p>
        `;
    }

    catch(error){

        resultDiv.innerHTML = `
            <p>Error fetching AI analysis</p>
        `;

        console.log(error);
    }
}

async function analyzePortfolio(){

    const stocks =
    document.getElementById("portfolioStocks")
    .value
    .split(",");

    const query = stocks
    .map(stock => `symbols=${stock.trim()}`)
    .join("&");

    const response =
    await fetch(`/portfolio?${query}`);

    const data = await response.json();

    document.getElementById("portfolioResult")
    .innerHTML = `

        <h3>Portfolio Metrics</h3>

        <p>
        Expected Return:
        ${data.portfolio_metrics.expected_return}
        </p>

        <p>
        Risk:
        ${data.portfolio_metrics.risk}
        </p>

        <hr>

        <h3>AI Portfolio Analysis</h3>

        <p>${data.ai_analysis}</p>
    `;
}