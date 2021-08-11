const listPage = document.querySelector('.list-games');
const addcPage = document.querySelector('.add-games');
const editPage = document.querySelector('.edit-games');
const deltPage = document.querySelector('.delete-games');


const listIcon = document.querySelector('.bx-list-ul');
const addcIcon = document.querySelector('.bx-plus');
const editIcon = document.querySelector('.bxs-edit-alt');
const deltIcon = document.querySelector('.bxs-trash-alt');


listIcon.addEventListener('click', () => {
    listPage.style.display = 'block';
    addcPage.style.display = 'none';
    editPage.style.display = 'none';
    deltPage.style.display = 'none';
});

addcIcon.addEventListener('click', () => {
    listPage.style.display = 'none';
    addcPage.style.display = 'block';
    editPage.style.display = 'none';
    deltPage.style.display = 'none';
});

editIcon.addEventListener('click', () => {
    listPage.style.display = 'none';
    addcPage.style.display = 'none';
    editPage.style.display = 'block';
    deltPage.style.display = 'none';
});

deltIcon.addEventListener('click', () => {
    listPage.style.display = 'none';
    addcPage.style.display = 'none';
    editPage.style.display = 'none';
    deltPage.style.display = 'block';
});