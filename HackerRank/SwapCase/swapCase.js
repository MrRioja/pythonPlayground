// Problem: You are given a string and your task is to swap cases. In other words,
// convert all lowercase letters to uppercase letters and vice versa.
// Ex: Www.HackerRank.com => wWW.hACKERrANK.COM

export function swapCase(s) {
  return s
    .split("")
    .map((letter) =>
      /[A-Z]/g.exec(letter) ? letter.toLowerCase() : letter.toUpperCase()
    )
    .join("");
}
