// Image switcher code

let myImage = document.querySelector('img');

myImage.onclick = () => {
  let mySrc = myImage.getAttribute('src');
  // TO DO: Change the image
}

// Personalized welcome message code

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');


setUserName = () => {
  let myName = prompt('Please enter your name.');
  // TO DO: Set the heading to be 'Javascript is cool, ' + name 
}

myButton.onclick = () => {
  setUserName();
}
