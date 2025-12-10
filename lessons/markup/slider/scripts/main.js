let current_indx = 0;
let current_indx2 = 1;
items = document.getElementsByClassName('slider-item')
items[current_indx].style.display = 'flex';
items[current_indx2].style.display = 'flex';
function move(){
    if(event.target.getAttribute('id') == 'right'){
        current_indx++;
        current_indx2++;
    }
    else{
        current_indx--;
        current_indx2--;
    }
        

    for(let i = 0; i < items.length; i++){
        items[i].style.display = 'none';
    }
    if (current_indx >= items.length) {
        current_indx = 0;
    } else if (current_indx < 0) {
        current_indx = items.length - 1;
    }

    if (current_indx2 >= items.length) {
        current_indx2 = 0;
    } else if (current_indx2 < 0) {
        current_indx2 = items.length - 1;
    }
    items[current_indx].style.display = 'flex';
    items[current_indx].style.order = '1';
    items[current_indx2].style.display = 'flex';
    items[current_indx2].style.order = '2';
}