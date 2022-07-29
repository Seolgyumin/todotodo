const getPersonaElement = (personaContent, personaId) => {
  const newPersonaElement = document.createElement("a");
  newPersonaElement.setAttribute("href", `todo/home/${personaId}/`);
  newPersonaElement.innerHTML = personaContent;
  return newPersonaElement;
};

const addPersona = async () => {
  const personacreateModal = document.getElementById("persona-create-modal");
  personacreateModal.classList.add("show");
  const personaInputElement = document.getElementById("persona-create-modal");
  if (personaInputElement.value) {
    const data = new FormData();
    data.append("content", personaInputElement.value);
    const response = await axios.post(`todo/createpersona/`, data);
    const personaElement = getPersonaElement(
      personaInputElement.value,
      response.data.personaId
    );
    document.getElementById("persona-list").appendChild(personaElement);
    personaInputElement.value = "";
  }
};

const showTodoInput = (categoryname, categoryid) => {
  const todoInputElement = document.getElementById(
    `${categoryname}-input-container`
  );
  todoInputElement.classList.add("show");
  const Box = document.getElementById(`${categoryname}-todo-list`);
  const newP = document.createElement("p");
  newP.innerHTML = `<div class="todo-input-container" id="${categoryname}-input-container"><input class="todo-checkbox" type="checkbox"/> <label for="todo-checkbox"></label><input class="todo-input todoname-text" id="${categoryname}-todo-input" type="text" placeholder="투두를 입력하세요"/></div>`;
  Box.prepend(newP);
  const inputbox = document.getElementById(`${categoryname}-todo-input`);
  inputbox.focus();
  inputbox.addEventListener("blur", function (e) {
    // e.stopPropagation()
    if (todoInputElement.classList.contains("show")) {
      if (e.target.id == inputbox.id) {
        addTodo(categoryname, categoryid);
        newP.innerHTML = "";
      }
    }
  });
};

const getTodoElement = (todoContent, todoId) => {
  const newTodoElement = document.createElement("a");
  newTodoElement.setAttribute("href", `todo/edittodo/${todoId}/`);
  newTodoElement.innerHTML = `<div class="todo-container" id="${todoContent}-container">
    <input class="todo-checkbox" onclick="completeTodo('${todoContent}','${todoId}') type="checkbox"/>
    <div class="todoname-text" id="${todoContent}-todoname"> ${todoContent} </div>
    <svg class="todo-detail" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M5.2 13.1998C4.86667 13.1998 4.58333 13.0831 4.35 12.8498C4.11667 12.6165 4 12.3331 4 11.9998C4 11.6665 4.11667 11.3831 4.35 11.1498C4.58333 10.9165 4.86667 10.7998 5.2 10.7998C5.53333 10.7998 5.81667 10.9165 6.05 11.1498C6.28333 11.3831 6.4 11.6665 6.4 11.9998C6.4 12.3331 6.28333 12.6165 6.05 12.8498C5.81667 13.0831 5.53333 13.1998 5.2 13.1998ZM12 13.1998C11.6667 13.1998 11.3833 13.0831 11.15 12.8498C10.9167 12.6165 10.8 12.3331 10.8 11.9998C10.8 11.6665 10.9167 11.3831 11.15 11.1498C11.3833 10.9165 11.6667 10.7998 12 10.7998C12.3333 10.7998 12.6167 10.9165 12.85 11.1498C13.0833 11.3831 13.2 11.6665 13.2 11.9998C13.2 12.3331 13.0833 12.6165 12.85 12.8498C12.6167 13.0831 12.3333 13.1998 12 13.1998ZM18.8 13.1998C18.4667 13.1998 18.1833 13.0831 17.95 12.8498C17.7167 12.6165 17.6 12.3331 17.6 11.9998C17.6 11.6665 17.7167 11.3831 17.95 11.1498C18.1833 10.9165 18.4667 10.7998 18.8 10.7998C19.1333 10.7998 19.4167 10.9165 19.65 11.1498C19.8833 11.3831 20 11.6665 20 11.9998C20 12.3331 19.8833 12.6165 19.65 12.8498C19.4167 13.0831 19.1333 13.1998 18.8 13.1998Z" fill="#919191"/>
    </svg>
    </div>`;
  var sheet = document.createElement("style");
  sheet.innerHTML =
    ".todo-container {margin-bottom: 12px;height: 50px;display: flex;align-items: center;} .todo-checkbox{width: 50px;height: 50px;cursor: pointer;} .todoname-text {margin-left: 16px;font-family:Pretendard;font-style: normal;font-weight: 400;font-size: 20px;letter-spacing: -0.165px;color: #333333;} .todo-detail {position: absolute;margin-right: 24px;right: 0px;}";
  document.body.appendChild(sheet);
  return newTodoElement;
};

const addTodo = async (categoryname, categoryid) => {
  const todoInputElement = document.getElementById(
    `${categoryname}-todo-input`
  );
  if (todoInputElement.value) {
    const data = new FormData();
    data.append("name", todoInputElement.value);
    let yourDate = new Date();
    yourDate.toISOString().split("T")[0];
    data.append("end_date", yourDate.toISOString().split("T")[0]);
    const response = await axios.post(`/todo/createtodo/${categoryid}/`, data);
    const todoElement = getTodoElement(
      todoInputElement.value,
      response.data.todoId
    );
    document.getElementById(`${categoryname}-todo-list`).prepend(todoElement);
    todoInputElement.value = "";
  }
  () => {
    todoInputElement.classList.remove("show");
  };
};

const completeTodo = async (todoname, todoid) => {
  const todoComplete = document.getElementById(`${todoname}-todoname`);
  todoComplete.classList.add("complete");
  todoComplete.innerHTML = `${todoname}`;
  const data = new FormData();
  const response = await axios.post(`/todo/completetodo/${todoid}/`, data);
  response;
};

const editTodo = async (todoid) => {
  const commentInputElement = document.getElementById("");
  if (commentInputElement.value) {
    const data = new FormData();
    data.append("content", commentInputElement.value);
    const response = await axios.post(`/todo/edittodo/${todoid}/`);
  }
};

const showWeekDate = (personaid) => {
  const weekdateElement = document.getElementById("week-date");
  weekdateElement.classList.remove("hide");
  const monthdateElement = document.getElementById("month-date");
  monthdateElement.classList.add("hide");
  const weeklytextElement = document.getElementById("weekly-text");
  weeklytextElement.classList.add("bold");
  const monthlytextElement = document.getElementById("monthly-text");
  monthlytextElement.classList.remove("bold");
  console.log(
    monthdateElement,
    weekdateElement,
    weeklytextElement,
    monthlytextElement
  );
  //   updateDiv(personaid);
};

const showMonthDate = (personaid) => {
  const monthdateElement = document.getElementById("month-date");
  monthdateElement.classList.remove("hide");
  const weekdateElement = document.getElementById("week-date");
  weekdateElement.classList.add("hide");
  const weeklytextElement = document.getElementById("weekly-text");
  weeklytextElement.classList.remove("bold");
  const monthlytextElement = document.getElementById("monthly-text");
  monthlytextElement.classList.add("bold");
  console.log(
    monthdateElement,
    weekdateElement,
    weeklytextElement,
    monthlytextElement
  );
};

const showTodoDeleteModal = (categoryname, todoname) => {
  const TodoElement = document.getElementById(`${todoname}-delete-modal`);
  TodoElement.classList.add("show");
};

//   updateDiv(personaid);

// function updateDiv(personaid) {
//   $("#calendar-container").load(`/todo/home/${personaid}/ #calendar-container`);
// }
// personaContent에서 사진만 처리해줘야함

const hideModal = () => {
  const personacreateModal = document.getElementById("persona-create-modal");
  personacreateModal.classList.remove("show");
};
