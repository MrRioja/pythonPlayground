// Problem: https://www.hackerrank.com/challenges/staircase/problem
// Sua base e altura são iguais a N. Ele é desenhado usando #símbolos e espaços. A última linha não é precedida de espaços.
// Escreva um programa que imprima uma escada de tamanho N.
// Ex: N = 4:
//    #
//   ##
//  ###
// ####

export function staircase(n) {
  let staircase = "";

  for (let index = 0; index < n; index++) {
    if (index > 0) {
      staircase += "\n";
    }

    for (let aux = 0; aux < n; aux++) {
      if (aux + 1 >= n - index) {
        staircase += "#";
      } else {
        staircase += " ";
      }
    }
  }
  return staircase;
}
