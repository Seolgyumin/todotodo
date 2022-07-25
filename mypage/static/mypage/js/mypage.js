const addPersonaButton = document.getElementById('add-persona-button')
addPersonaButton.onclick = (e) => handleAddPersona(e);

const handleAddPersona = (e) => {
    e.addPersona();
}

// 자스 전부 다 미완성임 싹 지우고 다시 해도 됨 index.html 과 연결