// Problem: You are given a string and your task is to swap cases. In other words,
// convert all lowercase letters to uppercase letters and vice versa.
// Ex: Www.HackerRank.com => wWW.hACKERrANK.COM

function swapCase(s) {
  return s
    .split("")
    .map((letter) =>
      /[A-Z]/g.exec(letter) ? letter.toLowerCase() : letter.toUpperCase()
    )
    .join("");
}

const string = "Www.HackerRank.com"; // wWW.hACKERrANK.COM
// const string = "Pythonist 2"; // pYTHONIST 2

console.log(swapCase(string));
