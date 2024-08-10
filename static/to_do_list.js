let addButtons = document.querySelectorAll("#addbutton");
let addTaskFields = document.querySelectorAll("#addtask");
let listToDos = document.querySelectorAll('.listToDo');
let items = document.querySelectorAll('li');

let lengthItem = items.length

for (let i = 0; i < lengthItem; i++) {
    items[i].addEventListener('click', () => items[i].remove())
}

let addButtonsLength = addButtons.length

for (let i = 0; i < addButtonsLength; i++) {
    addButtons[i].addEventListener("click", () => addTask(i))
}

function addTask(i) {
    const node = document.createElement("li");
    if (addTaskFields[i].value != '') {
        const textnode = document.createTextNode(addTaskFields[i].value);
        node.appendChild(textnode);
        listToDos[i].appendChild(node);
        node.addEventListener('click', () => node.remove());
        addTaskFields[i].value = '';
    }
    else {
        alert("Please a enter a task to the list!");
    }
}