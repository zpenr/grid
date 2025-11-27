let labels = document.getElementsByClassName('img-lebel');
for( let i = 0; i < labels.length; i++){
    labels[i].addEventListener('mousedown', () => make_visible(labels[i]));
    labels[i].addEventListener('mouseup', () => make_unvisible(labels[i]));
}

function make_visible(elem){
    elem.getElementsByTagName('img')[0].classList.add('visible');
}

function make_unvisible(elem){
    elem.getElementsByTagName('img')[0].classList.remove('visible');
}