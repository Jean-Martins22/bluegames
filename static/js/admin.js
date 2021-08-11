const listIcon = document.querySelector('.bx-list-ul');
const addcIcon = document.querySelector('.bx-plus');
const editIcon = document.querySelector('.bxs-edit-alt');
// const editLink = document.querySelector('.edit-href');
const deltIcon = document.querySelector('.bxs-trash-alt');


listIcon.addEventListener('click', () => {displayListgames()});

function displayListgames(){
    document.querySelector('.list-games').style.display = 'block';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'none'
};


addcIcon.addEventListener('click', () => {displayAddgames()});

function displayAddgames(){
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'block';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'none'
};

editIcon.addEventListener('click', () => {displayEditgames()});
// editLink.addEventListener('click', () => {displayEditgames()});

function displayEditgames(){
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'block';
    document.querySelector('.delete-games').style.display = 'none'
};

deltIcon.addEventListener('click', () => {displayDeletegames()});

function displayDeletegames(){
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'block'
};