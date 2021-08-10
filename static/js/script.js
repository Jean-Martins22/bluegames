const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
searchButton.addEventListener('click', () => {
  const inputValue = searchInput.value;
  alert(inputValue);
});


function cartishow(){
  document.getElementById('shopping-cart').style.display='none';
}
