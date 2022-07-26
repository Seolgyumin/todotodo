const getPersonaElement = (personaContent, personaId) => {
    const newPersonaElement = document.createElement('a');
    newPersonaElement.setAttribute('href', `todo/home/${personaId}/`);
    newPersonaElement.innerHTML = personaContent; 
    return newPersonaElement;
}

const addPersona = async() => {
    showModal();
    const personaInputElement = document.getElementById("persona-create-modal");
    if(personaInputElement.value) {
        const data = new FormData();
        data.append("content", personaInputElement.value);
        const response = await axios.post(`todo/createpersona/`, data);
        const personaElement = getPersonaElement(personaInputElement.value, response.data.personaId);
        document.getElementById("persona-list").appendChild(personaElement);
        personaInputElement.value = '';
    }
}


const showTodoInput = (categoryname, categoryid) => {
    const todoInputElement = document.getElementById(`${categoryname}-todo-input`);
    todoInputElement.classList.add("show");
    todoInputElement.focus();
    todoInputElement.addEventListener('blur', function(e){
        // e.stopPropagation()
        if(todoInputElement.classList.contains('show')) {
            if(e.target.id == todoInputElement.id) {
                addTodo(categoryname, categoryid);
            }
        }
    });
}

const getTodoElement = (todoContent, todoId) => {
    const newTodoElement = document.createElement('a');
    newTodoElement.setAttribute('href', `todo/edittodo/${todoId}/`);
    newTodoElement.innerHTML = todoContent; 
    return newTodoElement;
}

const addTodo = async(categoryname, categoryid) => {
    const todoInputElement = document.getElementById(`${categoryname}-todo-input`);
    if(todoInputElement.value) {
        const data = new FormData();
        data.append("name", todoInputElement.value);
        let yourDate = new Date()
        yourDate.toISOString().split('T')[0]
        data.append("end_date", yourDate.toISOString().split('T')[0]);
        const response = await axios.post(`/todo/createtodo/${categoryid}/`, data);
        const todoElement = getTodoElement(todoInputElement.value, response.data.todoId);
        document.getElementById(`${categoryname}-todo-list`).appendChild(todoElement);
        todoInputElement.value = '';
    }
    () => {
        todoInputElement.classList.remove("show");
    }
}



// personaContent에서 사진만 처리해줘야함

const personacreateModal = document.getElementById("persona-create-modal");

const showModal = () => {
    personacreateModal.classList.add("show");
};

const hideModal = () => {
    personacreateModal.classList.remove("show");
};



