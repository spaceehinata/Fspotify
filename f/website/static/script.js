function changeColor(button) {
    var buttons = document.getElementsByClassName('login-btn');

    // Remove 'active' class from all buttons
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('active');
    }

    // Add 'active' class to the clicked button
    button.classList.add('active');
}