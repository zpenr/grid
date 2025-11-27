let container = document.createElement('div');
container.id = 'container';
container.className = 'theme-light';
document.body.appendChild(container);

let header = document.createElement('h2');
header.textContent = "Динамический список";
header.title = "Нажми, чтобы сменить тему";
header.addEventListener('click', toggleTheme);
container.appendChild(header);

let listElement = document.createElement('ul');
listElement.id = 'dynamic-list';
container.appendChild(listElement);

let addBtn = document.createElement('button');
addBtn.textContent = "Добавить пункты";
addBtn.className = 'btn';
addBtn.onclick = Input;
container.appendChild(addBtn);

const themeBtn = document.createElement('button');
themeBtn.textContent = "Сменить тему";
themeBtn.className = 'btn';
themeBtn.onclick = toggleTheme;
container.appendChild(themeBtn);

function Input() {
    while (true) {
        let userInput = prompt("Введите содержимое пункта списка (ESC или пустая строка для выхода):");
        if (userInput == null || userInput == "") {
            break;
        }
        let li = document.createElement('li');
        li.textContent = userInput;
        li.classList.add('list-item');
        listElement.appendChild(li);
    }
}

function toggleTheme() {
    if (container.classList.contains('theme-light')) {
        container.classList.remove('theme-light');
        container.classList.add('theme-dark');
    } else {
        container.classList.remove('theme-dark');
        container.classList.add('theme-light');
    }
}