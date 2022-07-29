const moveOnToAddPersona = () => {
  const nameInputBox = document.getElementById("input-name");
  const personaInput = document.getElementById("input-username");
  const personaDiv = document.getElementById("div-persona");
  const personaSpan = document.getElementById("span-username");
  const userName = nameInputBox.value;
  personaInput.innerText = userName + personaInput.dataset.text;
  personaDiv.classList.remove("hidden");
  personaSpan.innerText = userName + personaSpan.dataset.text;
};

const moveOnToAddEmoji = () => {
  const emojiDiv = document.getElementById("div-emoji");
  const completeButton = document.getElementById("complete");
  emojiDiv.classList.remove("hidden");
  completeButton.classList.remove("hidden");
};

const emojiImg = document.getElementsByClassName("emoji-img");

const handleClickEmoji = (e) => {
  if (e.target.classList[1] !== "clicked") {
    for (let i = 0; i < emojiImg.length; i++) {
      emojiImg[i].classList.remove("clicked");
    }
    e.target.classList.add("clicked");
    selectedEmoji(e);
  }
};

const init = () => {
  for (let i = 0; i < emojiImg.length; i++) {
    emojiImg[i].addEventListener("click", handleClickEmoji);
  }
};

init();

const selectedEmoji = (e) => {
  const selectedEmojiDiv = document.getElementById("div-selected-emoji");
  const emojiUrlInput = document.getElementById("select-emoji-url");
  const oldImg = document.getElementById("select-emoji-img");
  if (oldImg) {
    selectedEmojiDiv.removeChild(oldImg);
  }
  const newImg = document.createElement("img");
  selectedEmojiDiv.appendChild(newImg);
  newImg.setAttribute("src", e.target.src);
  newImg.setAttribute("id", "select-emoji-img");
  emojiUrlInput.value = e.target.src;
};

const goCongratsPage = async (e) => {
  const nameInputValue = document.getElementById("input-name").value;
  const personaNameInputValue =
    document.getElementById("input-persona-name").value;
  const selectedEmojiUrl = document.getElementById("select-emoji-img").src;
  if (nameInputValue && personaNameInputValue && selectedEmojiUrl) {
    const data = new FormData();
    data.append("username", nameInputValue);
    data.append("emoji", selectedEmojiUrl);
    data.append("persona_name", personaNameInputValue);

    try {
      const response = await axios.post(`/accounts/onboarding/`, data);
      if (response.data.success) {
        location.href = "/accounts/congrats/";
      }
    } catch (err) {
      console.log(err);
    }
  }
};
