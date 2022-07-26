const addPersonaModal = document.getElementById("add-persona-modal")
const updatePersonaModal = document.getElementById("update-persona-modal")
const addCategoryModal = document.getElementById("add-category-modal")

const showAddPersonaModal = () => {
    console.log('per-modal');
    addPersonaModal.classList.remove('hide');
}

const hideAddPersonaModal = () => {
    addPersonaModal.classList.add('hide');
}

const showUpdatePersonaModal = () => {
    updatePersonaModal.classList.remove('hide');
}

const hideUpdatePersonaModal = () => {
    updatePersonaModal.classList.add('hide');
}

const showAddCategoryModal = () => {
    addCategoryModal.classList.remove('hide');
}

const hideCategoryModal = () => {
    addCategoryModal.classList.add('hide');
}
// 자스 전부 다 미완성임 싹 지우고 다시 해도 됨 index.html 과 연결