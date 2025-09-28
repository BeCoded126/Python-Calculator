// document.getElementById("0").innerHTML = "0";
// document.getElementById("1").innerHTML = "1";
// document.getElementById("2").innerHTML = "2";
// document.getElementById("3").innerHTML = "3";
// document.getElementById("4").innerHTML = "4";
// document.getElementById("5").innerHTML = "5";
// document.getElementById("6").innerHTML = "6";
// document.getElementById("7").innerHTML = "7";
// document.getElementById("8").innerHTML = "8";
// document.getElementById("9").innerHTML = "9";
// document.getElementById(".").innerHTML = ".";
fetch("calculate")
  .then((response) => console.log(response))
  .then((data) => console.log(data.name))
  .catch((error) => console.error(error));

console.log("JS CONNECTED");
