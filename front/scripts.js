/*
  --------------------------------------------------------------------------------------
  Function to get values from form and send to API for prediction
  --------------------------------------------------------------------------------------
*/

function predictPersonality() {
  const data = {
    name: document.getElementById("newName").value,
    time_spent_alone: document.getElementById("newTimeSpentAlone").value,
    stage_fear: document.getElementById("newStageFear").value,
    social_event_attendance: document.getElementById("newSocialEventAttendance").value,
    going_outside: document.getElementById("newGoingOutside").value,
    drained_after_socializing: document.getElementById("newDrainedAfterSocializing").value,
    friends_circle_size: document.getElementById("newFriendsCircleSize").value,
    post_frequency: document.getElementById("newPostFrequency").value
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
      alert(`Prediction result: ${result.prediction}`);
    })
    .catch(error => {
      console.error("Prediction error:", error);
      alert("Error during prediction!");
    });
}

