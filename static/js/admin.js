const listIcon = document.querySelector('.list-click');
const addcIcon = document.querySelector('.add-click');
const editIcon = document.querySelector('.edit-click');
const deltIcon = document.querySelector('.delete-click');


listIcon.addEventListener('click', () => {displayListgames()});

function displayListgames(){
    document.querySelector('.list-games').style.display = 'block';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'none';
    listIcon.style.backgroundColor = 'black';
    addcIcon.style.backgroundColor = '#191B1F';
    editIcon.style.backgroundColor = '#191B1F';
    deltIcon.style.backgroundColor = '#191B1F'
};

function displayAddgames(){
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'block';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'none';
    listIcon.style.backgroundColor = '#191B1F';
    addcIcon.style.backgroundColor = 'black';
    editIcon.style.backgroundColor = '#191B1F';
    deltIcon.style.backgroundColor = '#191B1F'
};

editIcon.addEventListener('click', () => {displayEditgames()});
// editLink.addEventListener('click', () => {displayEditgames()});

function displayEditgames(){
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'block';
    document.querySelector('.delete-games').style.display = 'none';
    listIcon.style.backgroundColor = '#191B1F'
    addcIcon.style.backgroundColor = '#191B1F'
    editIcon.style.backgroundColor = 'black'
    deltIcon.style.backgroundColor = '#191B1F'
};

function displayDeletegames(){
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'block';
    listIcon.style.backgroundColor = '#191B1F'
    addcIcon.style.backgroundColor = '#191B1F'
    editIcon.style.backgroundColor = '#191B1F'
    deltIcon.style.backgroundColor = 'black'
};
