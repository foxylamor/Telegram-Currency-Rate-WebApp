function send() {
    const fromCurrency = document.getElementById("from").value;
    const toCurrency = document.getElementById("to").value;
    const amount = document.getElementById("amount").value;
    
    if (!amount || isNaN(amount) || amount <= 0) {
        alert("Enter a valid amount");
        return;
    }

    const data = {
        from: fromCurrency,
        to: toCurrency,
        amount: amount
    };

    Telegram.WebApp.sendData(JSON.stringify(data));
    Telegram.WebApp.close();
}
