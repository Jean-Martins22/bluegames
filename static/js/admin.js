const listIcon = document.querySelector('.bx-list-ul');
const addcIcon = document.querySelector('.bx-plus');
const editIcon = document.querySelector('.bxs-edit-alt');
const deltIcon = document.querySelector('.bxs-trash-alt');


listIcon.addEventListener('click', () => {
    document.querySelector('.list-games').style.display = 'block';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'none';
});

addcIcon.addEventListener('click', () => {
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'block';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'none';
});

editIcon.addEventListener('click', () => {
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'block';
    document.querySelector('.delete-games').style.display = 'none';
});

deltIcon.addEventListener('click', () => {
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'none';
    document.querySelector('.edit-games').style.display = 'none';
    document.querySelector('.delete-games').style.display = 'block';
});