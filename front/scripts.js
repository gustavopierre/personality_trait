/*
  --------------------------------------------------------------------------------------
  Function to get values from form and send to API for prediction
  --------------------------------------------------------------------------------------
*/

function predictPersonality() {
  const data = {
    name: document.getElementById("newName").value,
    timeSpentAlone: parseInt(document.getElementById("newTimeSpentAlone").value),
    stageFear: parseInt(document.getElementById("newStageFear").value),
    socialEventAttendance: parseInt(document.getElementById("newSocialEventAttendance").value),
    goingOutside: parseInt(document.getElementById("newGoingOutside").value),
    drainedAfterSocializing: parseInt(document.getElementById("newDrainedAfterSocializing").value),
    friendsCircleSize: parseInt(document.getElementById("newFriendsCircleSize").value),
    postFrequency: parseInt(document.getElementById("newPostFrequency").value)
  };

  fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(result => {
      alert(`Resultado da predição: ${result.prediction === 0 ? "Introvertido" : "Extrovertido"}`);
    })
    .catch(error => {
      console.error("Prediction error:", error);
      alert("Error during prediction!");
    });
}

