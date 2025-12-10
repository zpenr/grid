function change_visibility(){
    event.stopPropagation()
    event.target.firstElementChild.classList.toggle('visible');
}

function change_color(){
    let random_color = "rgb(" + Math.floor(Math.random()*256) + ',' + Math.floor(Math.random()*256) + ',' + Math.floor(Math.random()*256) + ')'
    event.stopPropagation()
    event.target.style.backgroundColor = random_color;
}