const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');

function sectionDisplay(id){
  if (document.getElementById(id).style.display!='flex'){
    document.getElementById(id).style.display='flex';
  }
}

function sectionHide(id){
  if (document.getElementById(id).style.display!='none'){
    document.getElementById(id).style.display='none';
  }
}


searchButton.addEventListener('click', () => {
  const inputValue = searchInput.value;
  alert(inputValue);
});


function cartishow(){
  document.getElementById('shopping-cart').style.display='none';
}
