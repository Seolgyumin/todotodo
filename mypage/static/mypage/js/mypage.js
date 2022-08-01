const addPersonaModal = document.getElementById("add-persona-modal");
const editPersonaModal = document.getElementById("edit-persona-modal");
const addCategoryModal = document.getElementById("add-category-modal");

const showAddPersonaModal = () => {
    addPersonaModal.classList.remove('hide');
}

const hideAddPersonaModal = () => {
    document.querySelector('div#add-persona-modal div#inner-add-persona-modal div.modal-complete object').contentDocument.getElementById('check-svg').setAttribute('fill-opacity', "0.4");
    document.querySelector('div#add-persona-modal div#inner-add-persona-modal div.modal-complete span').style= 'color: rgba(247, 167, 187, 0.4)';
    addPersonaModal.querySelector('input').value = "";
    addPersonaModal.classList.add('hide');
}

const handleResetAndCompleteButton = (obj) => {
    if (obj.value.length === 0) {
        obj.parentNode.parentNode.parentNode.querySelector('div.modal-complete object').contentDocument.getElementById('check-svg').setAttribute('fill-opacity', "0.4");
        obj.parentNode.parentNode.parentNode.querySelector('div.modal-complete span').style= 'color: rgba(247, 167, 187, 0.4)';
        obj.parentNode.querySelector('.name-input-reset-button').classList.add('hide');
    } else if (obj.value.length >= 1) {
        obj.parentNode.parentNode.parentNode.querySelector('div.modal-complete object').contentDocument.getElementById('check-svg').setAttribute('fill-opacity', "1");
        obj.parentNode.parentNode.parentNode.querySelector('div.modal-complete span').style= 'color: rgba(247, 167, 187, 1)';
        obj.parentNode.querySelector('.name-input-reset-button').classList.remove('hide');
    }
}

const resetInput = (obj) => {
    obj.parentNode.parentNode.parentNode.querySelector('div.modal-complete object').contentDocument.getElementById('check-svg').setAttribute('fill-opacity', "0.4");
    obj.parentNode.parentNode.parentNode.querySelector('div.modal-complete span').style= 'color: rgba(247, 167, 187, 0.4)';
    obj.parentNode.querySelector('input').value = "";
    obj.classList.add('hide');
}

const completeAddPersonaModal = async () => {
    const newNameInput = document.getElementById("new-persona-name-input");
    const personaName = newNameInput.value;
    
    if (personaName) {
        const data = new FormData();
        data.append('name', personaName);

        const response = await axios.post('createpersona/', data);
        const { personaId } = response.data;

        if (personaId) {
            document.getElementById('persona-list').appendChild(getNewPersonaElement(personaId, personaName));

            hideAddPersonaModal();
        }
    } else {

    }
}

const getNewPersonaElement = (personaId, personaName) => {
    const newPersona = document.createElement('div');
    newPersona.setAttribute('class', 'each-persona-container');
    newPersona.setAttribute('id', `each-persona-example-${personaId}`);

    const eachPersona = document.createElement('div');
    eachPersona.setAttribute('class', 'each-persona');
    eachPersona.setAttribute('onclick', `showEditPersonaModal(${personaId})`);

    const personaImg = document.createElement('img');
    personaImg.setAttribute('id', `${personaId}-imoji`)
    const personaNameSpan = document.createElement('span');
    personaNameSpan.setAttribute('id', `persona-name-${personaId}`);
    personaNameSpan.textContent = personaName;
    const arrowImg = document.createElement('img');
    const svgSrc = document.querySelector('.arrow-back-persona-details').getAttribute('src');
    arrowImg.setAttribute('src', svgSrc);

    eachPersona.appendChild(personaImg);
    eachPersona.appendChild(personaNameSpan);
    eachPersona.appendChild(arrowImg);

    const categoryList = document.createElement('div');
    categoryList.setAttribute('id', `${personaId}-category-list`);
    categoryList.setAttribute('class', 'category-list');

    const defaultCategory = document.createElement('div');
    defaultCategory.setAttribute('class', 'each-category');
    const defaultCategoryName = document.createElement('span');
    defaultCategoryName.setAttribute('class', 'category-name');
    defaultCategoryName.innerText = 'Routine'; // default Category = Routine

    defaultCategory.appendChild(defaultCategoryName);

    const accCategoryButton = document.createElement('div');
    accCategoryButton.setAttribute('class', 'each-category');
    accCategoryButton.setAttribute('id', `add-category-button-example-${personaId}`);
    accCategoryButton.setAttribute('onclick', `showAddCategoryModal(${personaId})`);
    accCategoryButton.innerHTML = "+";

    categoryList.appendChild(defaultCategory);
    categoryList.appendChild(accCategoryButton);

    newPersona.appendChild(eachPersona);
    newPersona.appendChild(categoryList);

    return newPersona;
}
//edit부터 이어서
const showEditPersonaModal = (personaId) => {
    editPersonaModal.querySelector('input').value = document.getElementById(`each-persona-${personaId}`).querySelector(`span#persona-name-${personaId}`).innerHTML;
    editPersonaModal.setAttribute('data-persona-id', personaId);
    editPersonaModal.classList.remove('hide');
}

const hideEditPersonaModal = () => {
    document.querySelector('div#edit-persona-modal div#inner-edit-persona-modal div.modal-complete object').contentDocument.getElementById('check-svg').setAttribute('fill-opacity', "0.4");
    document.querySelector('div#edit-persona-modal div#inner-edit-persona-modal div.modal-complete span').style= 'color: rgba(247, 167, 187, 0.4)';
    editPersonaModal.querySelector('input').value = "";
    editPersonaModal.removeAttribute('data-persona-id');
    editPersonaModal.classList.add('hide');
}

const completeEditPersonaModal = async () => {
    const personaId = editPersonaModal.getAttribute('data-persona-id');
    const priorNameElement = document.getElementById(`each-persona-${personaId}`).querySelector(`span#persona-name-${personaId}`);
    const updateName = document.querySelector('div#inner-edit-persona-modal input').value;
    if (updateName != priorNameElement.innerText) {
        const data = new FormData();
        data.append('name', updateName);

        const response = await axios.post(`editpersona/${personaId}/`, data);

        // if (response.data.success) {
        priorNameElement.innerText = updateName;
        hideEditPersonaModal();
        // }
    } else {
        hideEditPersonaModal();
    }
}

const deletePersona = async () => {
    const personaId = editPersonaModal.getAttribute('data-persona-id');

    const response = await axios.delete(`deletepersona/${personaId}/`);

    document.getElementById(`each-persona-${personaId}`).remove();
    hideEditPersonaModal();
}

let globalPersonaId = '';

const showAddCategoryModal = (personaId) => {
    addCategoryModal.classList.remove('hide');
    globalPersonaId = personaId;
}

const completeAddCategoryModal = async () => {
    const newCategoryNameInput = document.getElementById('new-category-name-input');

    if (newCategoryNameInput.value) {
        const data = new FormData();
        data.append('name', newCategoryNameInput.value);

        const response = await axios.post(`createcategory/${globalPersonaId}/`, data);
        const { personaId } = response.data;
        console.log(personaId + 'category added');
        const categoryList = document.getElementById(`${personaId}-category-list`);
        const addCategoryButton = document.getElementById(`add-category-button-${personaId}`);
        categoryList.insertBefore(getNewCategoryElement(newCategoryNameInput.value), addCategoryButton);

        hideCategoryModal();
    }
}

const getNewCategoryElement = (categoryName) => {
    const newCategory = document.createElement('div');
    newCategory.setAttribute('class', 'each-category');

    const newCategoryName = document.createElement('span');
    newCategoryName.setAttribute('class', 'category-name');
    newCategoryName.innerText = categoryName;

    newCategory.appendChild(newCategoryName);

    return newCategory;
}

const hideCategoryModal = () => {
    document.querySelector('div#add-category-modal div#inner-add-category-modal div.modal-complete object').contentDocument.getElementById('check-svg').setAttribute('fill-opacity', "0.4");
    document.querySelector('div#add-category-modal div#inner-add-category-modal div.modal-complete span').style= 'color: rgba(247, 167, 187, 0.4)';
    addCategoryModal.querySelector('input').value = "";
    addCategoryModal.classList.add('hide');
}
