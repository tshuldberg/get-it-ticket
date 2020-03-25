document.querySelector('.dropdown_btn')
        .addEventListener('click', function(e){
            document.getElementById('dropDownMenu')
                    .classList.toggle('show');
        });

window.onclick = function(e) {
    if(!this.event.target.matches('.dropdown_btn')) {
        let dropDown = document.getElementById('dropDownMenu');
        if(dropDown.classList.contains('show')) {
            dropDown.classList.remove('show');
        }
    }
}