/*
  --------------------------------------------------------------------------------------
  Function to get values from form and send to API for prediction
  --------------------------------------------------------------------------------------
*/

function predictPersonality() {
  const formData = new FormData();
  formData.append('name', document.getElementById("newName").value);
  formData.append('timeSpentAlone', document.getElementById("newTimeSpentAlone").value);
  formData.append('stageFear', document.getElementById("newStageFear").value);
  formData.append('socialEventAttendance', document.getElementById("newSocialEventAttendance").value);
  formData.append('goingOutside', document.getElementById("newGoingOutside").value);
  formData.append('drainedAfterSocializing', document.getElementById("newDrainedAfterSocializing").value);
  formData.append('friendsCircleSize', document.getElementById("newFriendsCircleSize").value);
  formData.append('postFrequency', document.getElementById("newPostFrequency").value);

  fetch("http://localhost:5000/predict", {
    method: "POST",
    body: formData
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

