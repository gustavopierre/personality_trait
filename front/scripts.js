/*
  --------------------------------------------------------------------------------------
  Função para obter diagnóstico de personalidade via GET
  --------------------------------------------------------------------------------------
*/
const newDiagnose = async (event) => {
  event.preventDefault();

  let inputPatient = document.getElementById("newInput").value;
  let inputTimeSpentAlone = document.getElementById("newTimeSpentAlone").value;
  let inputStageFear = document.getElementById("newStageFear").value;
  let inputSocialEventAttendance = document.getElementById("newSocialEventAttendance").value;
  let inputGoingOutside = document.getElementById("newGoingOutside").value;
  let inputDrainedAfterSocializing = document.getElementById("newDrainedAfterSocializing").value;
  let inputFriendsCircleSize = document.getElementById("newFriendsCircleSize").value;
  let inputPostFrequency = document.getElementById("newPostFrequency").value;

  // Validações básicas
  if (inputPatient === '') {
    alert("The 'Name' field cannot be empty!");
    return;
  }
  
  if (isNaN(inputTimeSpentAlone) || isNaN(inputStageFear) || isNaN(inputSocialEventAttendance) || 
      isNaN(inputGoingOutside) || isNaN(inputDrainedAfterSocializing) || isNaN(inputFriendsCircleSize) || 
      isNaN(inputPostFrequency)) {
    alert("These fields must be numeric: Time Spent Alone, Stage Fear, Social Event Attendance, Going Outside, Drained After Socializing, Friends Circle Size, Post Frequency.");
    return;
  }

  try {
    // Monta a URL com os parâmetros para a requisição GET
    const params = new URLSearchParams({
      name: inputPatient,
      time_spent_alone: inputTimeSpentAlone,
      stage_fear: inputStageFear,
      social_event_attendance: inputSocialEventAttendance,
      going_outside: inputGoingOutside,
      drained_after_socializing: inputDrainedAfterSocializing,
      friends_circle_size: inputFriendsCircleSize,
      post_frequency: inputPostFrequency
    });

    const url = `http://127.0.0.1:5000/diagnose?${params.toString()}`;
    
    // Faz a requisição GET para obter o diagnóstico
    const response = await fetch(url, {
      method: 'GET'
    });
    
    const result = await response.json();
    
    // Mostra o resultado do diagnóstico
    const diagnostico = result.outcome === 1 ? "EXTROVERT" : "INTROVERT";
    alert(`Diagnose to ${inputPatient}: ${diagnostico}`);
    
    // Limpa o formulário após o diagnóstico
    document.getElementById("newName").value = "";
    document.getElementById("newTimeSpentAlone").value = "";
    document.getElementById("newStageFear").value = "";
    document.getElementById("newSocialEventAttendance").value = "";
    document.getElementById("newGoingOutside").value = "";
    document.getElementById("newDrainedAfterSocializing").value = "";
    document.getElementById("newFriendsCircleSize").value = "";
    document.getElementById("newPostFrequency").value = "";
    
  } catch (error) {
    console.error('Erro ao obter diagnóstico:', error);
    alert("Error obtaining diagnosis. Please check if the API is running and try again.");
  }
}
