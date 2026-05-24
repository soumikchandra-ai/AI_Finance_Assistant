let priceChart;
let rsiChart;
let macdChart;
async function analyzeStock(){
    document.getElementById("loader").style.display = "block";
    const symbol = document.getElementById("symbol").value;
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Analyzing with AI...";
    try{
        const response = await fetch(`/analysis/${symbol}`);
        const data = await response.json();
        if(data.error){
            resultDiv.innerHTML = `<p>${data.error}</p>`;
            return;
        }
        const chartData = data.stock_data.chart_data;
        const dates = chartData.dates;
        const closePrices = chartData.close;
        const rsiValues = chartData.rsi;
        const macdValues = chartData.macd;
        const macdSignal = chartData.macd_signal;
        if(priceChart){
            priceChart.destroy();
        }
        const ctx1 =
        document.getElementById("priceChart");
        priceChart = new Chart(ctx1, {
            type: "line",
            data: {
                labels: dates,
                datasets: [{
                    label: "Stock Price",
                    data: closePrices,
                    borderWidth: 0.4
                }]
            }
        });
        if(rsiChart){
            rsiChart.destroy();
        }
        const ctx2 =
        document.getElementById("rsiChart");
        rsiChart = new Chart(ctx2, {
            type: "line",
            data: {
                labels: dates,
                datasets: [{
                    label: "RSI",
                    data: rsiValues,
                    borderWidth: 0.4
                }]
            }
        });
        if(macdChart){
            macdChart.destroy();
        }
        const ctx3 =
        document.getElementById("macdChart");
        macdChart = new Chart(ctx3, {
            type: "line",
            data: {
                labels: dates,
                datasets: [
                    {
                        label: "MACD",
                        data: macdValues,
                        borderWidth: 0.4
                    },
                    {
                        label: "Signal Line",
                        data: macdSignal,
                        borderWidth: 0.4
                    }
                ]
            }
        });
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
            <div class="ai-analysis">${typeof marked.parse === 'function' ? marked.parse(data.ai_analysis) : marked(data.ai_analysis)}</div>
            `;
        document.getElementById("loader").style.display = "none";
    }
    
    catch(error){
        document.getElementById("loader").style.display = "none";
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
        <div class="ai-analysis">${marked.parse(data.ai_analysis)}</div>`;
}
async function sendMessage(){
    const input =
    document.getElementById("chatInput");
    const chatBox =
    document.getElementById("chatBox");
    const message = input.value;
    if(message.trim() === ""){
        return;
    }
    // USER MESSAGE
    chatBox.innerHTML += `
        <div class="message user-message">
            ${message}
        </div>
    `;
    input.value = "";
    // LOADING MESSAGE
    chatBox.innerHTML += `
        <div class="message bot-message">
            Thinking...
        </div>
    `;
    try{
        const response = await fetch("/chat",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });
        const data = await response.json();
        // REMOVE THINKING
        chatBox.lastElementChild.remove();
        // BOT RESPONSE
        chatBox.innerHTML += `
            <div class="message bot-message">
                ${marked.parse(data.response)}
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    catch(error){
        chatBox.innerHTML += `
            <div class="message bot-message">
                Error generating response.
            </div>
        `;
        console.log(error);
    }
}
function generateReport(){
    const symbol =
    document.getElementById("symbol").value;
    if(symbol.trim() === ""){
        return;
    }
    window.open(
        `/generate-report/${symbol}`,
        "_blank"
    );
}