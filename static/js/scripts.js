function checkAnomaly() {
  const requests = document.getElementById("requests").value;
  const responseTime = document.getElementById("response_time").value;

  fetch("/check_anomaly", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      requests_per_minute: Number(requests),
      response_time: Number(responseTime),
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").textContent = `Result: ${data.status}`;
    })
    .catch((error) => console.error("Error:", error));
}
