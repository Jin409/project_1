/*!
* Start Bootstrap - Resume v7.0.3 (https://startbootstrap.com/theme/resume)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const sideNav = document.body.querySelector('#sideNav');
    if (sideNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#sideNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

const bodySetColor = (color) =>{
    document.querySelector('body').style.color = color;
};


const bodySetBackgroundColor = (color) =>{

    document.querySelector('body').style.background.color = color;
};

const day_night_handler = (self) => {
    if (self.value=="야간모드로 바꾸기"){
        bodySetBackgroundColor("RGB(26,36,54)");
        bodySetColor("white");
        linkSetColor("powderblue");
        self.value="주간모드로 바꾸기";
    }
    else{
        bodySetBackgroundColor("white");
    bodySetColor("black");
    linkSetColor("blue");
    self.value = "야간모드로 바꾸기";
    }
    
}