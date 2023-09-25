document.addEventListener("DOMContentLoaded", function () {
    const statusElement = document.getElementById("status");
    const startButton = document.getElementById("start");
    const stopButton = document.getElementById("stop");
    const cycleSelect = document.getElementById("cycle");
    const temperatureInput = document.getElementById("temperature");
    const spinSpeedInput = document.getElementById("spin-speed");
    const waterLevelInput = document.getElementById("water-level");

    let isRunning = false;
    let currentStep = 0;
    const steps = [
        { text: "Filling with water...", delay: 2000 },
        { text: "Washing...", delay: 3000 },
        { text: "Rinsing...", delay: 2000 },
        { text: "Spinning...", delay: 2500 },
        { text: "Finished", delay: 1000 },
    ];

    function updateStatus(step) {
        statusElement.textContent = steps[step].text;
        if (step < steps.length - 1) {
            setTimeout(() => {
                if (isRunning) {
                    currentStep++;
                    updateStatus(currentStep);
                }
            }, steps[step].delay);
        } else {
            isRunning = false;
        }
    }

    startButton.addEventListener("click", function () {
        if (!isRunning) {
            isRunning = true;
            currentStep = 0;
            updateStatus(currentStep);
        }
    });

    stopButton.addEventListener("click", function () {
        if (isRunning) {
            isRunning = false;
            statusElement.textContent = "Idle";
        }
    });
});
