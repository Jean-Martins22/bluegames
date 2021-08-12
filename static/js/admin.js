const listIcon = document.querySelector('.list-click');
const addcIcon = document.querySelector('.add-click');

listIcon.addEventListener('click', () => {
    document.querySelector('.list-games').style.display = 'block';
    document.querySelector('.add-games').style.display = 'none';

    listIcon.style.backgroundColor = 'black';
    addcIcon.style.backgroundColor = '#191B1F';
});

addcIcon.addEventListener('click', () => {
    document.querySelector('.list-games').style.display = 'none';
    document.querySelector('.add-games').style.display = 'block';

    listIcon.style.backgroundColor = '#191B1F';
    addcIcon.style.backgroundColor = 'black';
});