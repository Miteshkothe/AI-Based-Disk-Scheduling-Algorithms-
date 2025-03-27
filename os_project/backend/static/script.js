// async function schedule() {
//     let requests = document.getElementById('requests').value.split(',').map(Number);
//     let head = parseInt(document.getElementById('head').value);
//     let algorithm = document.getElementById('algorithm').value;

//     let response = await fetch('/schedule', {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ requests, head, algorithm })
//     });

//     let data = await response.json();
//     document.getElementById('output').innerHTML = "Schedule: " + JSON.stringify(data.schedule);
// }
document.getElementById("schedule-btn").addEventListener("click", function () {
    const requestsInput = document.getElementById("requests").value;
    const headInput = document.getElementById("head").value;
    const algorithm = document.getElementById("algorithm").value;

    if (!requestsInput || !headInput) {
        alert("Please enter disk requests and head position.");
        return;
    }

    const requests = requestsInput.split(",").map(Number);
    const head = Number(headInput);

    fetch("http://127.0.0.1:5000/schedule", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ requests, head, algorithm })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = 
            `Sequence: ${data.schedule.sequence}\nSeek Time: ${data.schedule.seek_time}`;
    })
    .catch(error => console.error("Error:", error));
});

