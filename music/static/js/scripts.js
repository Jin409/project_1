

const linkSetColor = (color) => {
    const alist = document.querySelectorAll('a');
    for (let i=0; i < alist.length; i++) alist[i].style.color = color;
  };


const headSetColor3 = (color) => {
    const headlist = document.querySelectorAll('h3');
    for (let i=0; i < headlist.length; i++) headlist[i].style.color = color;
  };
const bodySetColor = (color) => {
      document.querySelector("body").style.color = color;
    };
    
    // body 배경색 바꾸기
    const bodySetBackgroundColor = (color) => {
      document.querySelector("body").style.backgroundColor = color;
    };
  
    const day_night_handler = (self) => {
      if (self.value == "야간모드로 바꾸기") {
        bodySetBackgroundColor("RGB(26,36,54)");
        bodySetColor("white");
        linkSetColor("powderblue");
        // textSetColor("powderblue");
        // headSetColor1("powerblue");
        // headSetColor2("powerblue");
        headSetColor3("white");
        // headSetColor4("powerblue");
        // headSetColor5("powerblue");
        self.value = "주간모드로 바꾸기";
      }
      else {
        bodySetBackgroundColor("white");
        bodySetColor("");
        linkSetColor("");
        // linkSetColor("blue");textSetColor("black"); 
        // headSetColor1("black");
        // headSetColor2("powerblue");
        headSetColor3("black");
        // headSetColor4("powerblue");
        // headSetColor5("powerblue");
        self.value = "야간모드로 바꾸기";
      }
    };