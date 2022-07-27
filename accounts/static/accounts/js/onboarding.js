
const moveOnToAddPersona = () => {
    const nameInputBox = document.getElementById("input-name");
    const personaInput = document.getElementById("input-username");
    const personaDiv = document.getElementById("div-persona");
    const personaSpan = document.getElementById("span-username");
    const userName = nameInputBox.value;
    personaInput.innerText = userName + personaInput.dataset.text;
    personaDiv.classList.remove("hidden");
    personaSpan.innerText = userName + personaSpan.dataset.text;
}

const moveOnToAddEmoji = () => {
    const emojiDiv = document.getElementById("div-emoji");
    const completeButton = document.getElementById("complete");
    emojiDiv.classList.remove("hidden");
    completeButton.classList.remove("hidden");
}

const emojiImg = document.getElementsByClassName("emoji-img");

const handleClickEmoji = (e) => {
    if (e.target.classList[1] !== "clicked") {
        for (let i = 0; i < emojiImg.length; i++) {
            emojiImg[i].classList.remove("clicked");
        }
        e.target.classList.add("clicked");
        selectedEmoji(e);
    }
}

const init = () => {
    for(let i = 0; i < emojiImg.length; i++) {
        emojiImg[i].addEventListener("click", handleClickEmoji);
    }
}

init();

const selectedEmoji = (e) => {
    const divSelectedEmoji = document.getElementById("div-selected-emoji");
    const oldImg = document.getElementById("select-emoji-img");
    if (oldImg) {
        divSelectedEmoji.removeChild(oldImg);
    }
    const newImg = document.createElement("img");
    divSelectedEmoji.appendChild(newImg);
    newImg.setAttribute("src", e.target.src);
    newImg.setAttribute("id", "select-emoji-img")
}

// const images = ["7294743.svg", "7309671.svg", "7309674.svg", "7309767.svg", "7309682.svg", "7309684.svg", "7300697.svg", "7309702.svg", "7309706.svg", "7309711.svg"]
// // const chosenImage = images{}

// const windowOnload = () => {
//     const emojiList = document.getElementById("emoji-list");

//     images.forEach(image => {
//         const bgImage = document.createElement("img");
//         bgImage.src = `http://localhost:8000/accounts/static/accounts/img/${image}`;
//         emojiList.appendChild(bgImage);
//     });
// }

// // window.onload = windowOnload;
