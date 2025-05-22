form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const data = {};
  formData.forEach((v, k) => { data[k] = v; });

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    const result = await response.json();

    resultDiv.style.display = 'block';
    if (result.churn) {
      resultDiv.textContent = `⚠️ Customer likely to CHURN (Probability: ${(result.churn_probability*100).toFixed(2)}%)`;
      resultDiv.className = 'result churn';
    } else {
      resultDiv.textContent = `✅ Customer likely to STAY (Probability: ${(result.churn_probability*100).toFixed(2)}%)`;
      resultDiv.className = 'result no-churn';
    }
  } catch (error) {
    resultDiv.style.display = 'block';
    resultDiv.textContent = '❌ Error predicting churn. Try again.';
    resultDiv.className = 'result churn';
    console.error(error);
  }
});
